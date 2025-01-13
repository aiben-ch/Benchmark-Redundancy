import os
import json
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from scipy.stats import spearmanr, pearsonr
import matplotlib.cm as cm
import argparse

def calculate_r2(x, y):
    x = np.array(x).reshape(-1, 1) if len(np.array(x).shape) == 1 else np.array(x)
    y = np.array(y)

    if x.shape[0] != y.shape[0]:
        raise ValueError("The number of samples in x and y must be the same.")

    model = LinearRegression()
    model.fit(x, y)
    y_pred = model.predict(x)
    return r2_score(y, y_pred)

def calculate_metrics(bench_score, top_k):
    overall_scores = bench_score.get('Overall', [])
    if not overall_scores:
        raise ValueError("The 'Overall' key is missing or empty in bench_score.")

    # Sort indices by 'Overall' scores in descending order
    if top_k < 0:
        sorted_indices = np.argsort(overall_scores)[::-1][top_k:]
    else:
        sorted_indices = np.argsort(overall_scores)[::-1][:top_k]

    filtered_bench_score = {
        key: [values[i] for i in sorted_indices]
        for key, values in bench_score.items()
    }

    metrics_keys = [key for key in filtered_bench_score.keys() if key != 'Overall']
    num_keys = len(metrics_keys)

    srcc_matrix = np.zeros((num_keys, num_keys))
    plcc_matrix = np.zeros((num_keys, num_keys))
    r2_matrix = np.zeros((num_keys, num_keys))

    for i, key_i in enumerate(metrics_keys):
        for j, key_j in enumerate(metrics_keys):
            if i <= j:
                list_i = filtered_bench_score[key_i]
                list_j = filtered_bench_score[key_j]

                srcc, _ = spearmanr(list_i, list_j)
                srcc_matrix[i, j] = srcc
                srcc_matrix[j, i] = srcc

                plcc, _ = pearsonr(list_i, list_j)
                plcc_matrix[i, j] = plcc
                plcc_matrix[j, i] = plcc

                r2 = calculate_r2(list_i, list_j)
                r2_matrix[i, j] = r2
                r2_matrix[j, i] = r2

    return filtered_bench_score, metrics_keys, srcc_matrix, plcc_matrix, r2_matrix

def get_matrix(data, bench, top_k):
    bench_score = {}

    for lmm in data.keys():
        item = data[lmm]
        if bench in item.keys():
            bench_item = item[bench]
            for sub_key in bench_item.keys():
                if any(keyword in sub_key for keyword in ["official", "dir_name", "Dir Name", "AR", "CP", "FP-C", "FP-S", "RR", "LR"]):
                    continue
                bench_score.setdefault(sub_key, []).append(bench_item[sub_key])

    return calculate_metrics(bench_score, top_k=top_k)

def plot_similarity_analysis(matrix, matrix_type, bench, save_folder, keys, vmin, vmax, top_k):
    formatted_keys = ["\n".join(key.split()) for key in keys]

    plt.figure(figsize=(12, 10))
    sns.heatmap(matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True, vmin=vmin, vmax=vmax, 
                xticklabels=formatted_keys, yticklabels=formatted_keys)

    heatmap_output_path = f"{save_folder}/{bench}_{matrix_type}_{top_k}_heatmap.pdf"
    plt.tight_layout()
    plt.savefig(heatmap_output_path)
    plt.close()

    avg_similarity = pd.Series(np.abs(matrix).mean(axis=1), index=keys)

    plt.figure(figsize=(14, 8))
    avg_similarity.plot(kind='line', marker='o', linestyle='-', color='b')
    plt.ylabel("Average Values", fontsize=12)
    plt.xticks(ticks=range(len(keys)), labels=formatted_keys, rotation=90, ha='right', fontsize=10)
    plt.grid(True)
    for x, y in enumerate(avg_similarity):
        plt.text(x, y + 0.003, f"{y:.4f}", fontsize=10, ha='center', va='bottom')

    lineplot_output_path = f"{save_folder}/{bench}_{matrix_type}_{top_k}_avg_similarity_lineplot.pdf"
    plt.tight_layout()
    plt.savefig(lineplot_output_path)
    plt.close()

    plt.figure(figsize=(14, 8))
    colors = cm.Blues(np.linspace(0.5, 0.7, len(avg_similarity)))
    avg_similarity.plot(kind='bar', color=colors)
    plt.ylabel("Average Values", fontsize=12)
    plt.xticks(ticks=range(len(keys)), labels=formatted_keys, rotation=90, ha='right', fontsize=12)
    plt.grid(axis='y')

    barplot_output_path = f"{save_folder}/{bench}_{matrix_type}_{top_k}_avg_similarity_barplot.pdf"
    plt.tight_layout()
    plt.savefig(barplot_output_path)
    plt.close()

def main(args):
    with open(args.input_file, 'r') as f:
        data = json.load(f)['results']

    if not os.path.exists(args.save_folder):
        os.makedirs(args.save_folder)

    filtered_bench_score, keys, srcc_matrix, plcc_matrix, r2_matrix = get_matrix(data, args.bench, top_k=args.top_k)

    plot_similarity_analysis(matrix=srcc_matrix, matrix_type="SRCC", bench=args.bench, save_folder=args.save_folder, 
                             keys=keys, vmin=args.vmin, vmax=args.vmax, top_k=args.top_k)

    plot_similarity_analysis(matrix=plcc_matrix, matrix_type="PLCC", bench=args.bench, save_folder=args.save_folder, 
                             keys=keys, vmin=args.vmin, vmax=args.vmax, top_k=args.top_k)

    plot_similarity_analysis(matrix=r2_matrix, matrix_type="R2", bench=args.bench, save_folder=args.save_folder, 
                             keys=keys, vmin=args.vmin, vmax=args.vmax, top_k=args.top_k)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Benchmark similarity analysis.")
    parser.add_argument("--input_file", type=str, required=True, help="Path to the input JSON file.")
    parser.add_argument("--bench", type=str, required=True, help="Benchmark name.")
    parser.add_argument("--save_folder", type=str, default="results", help="Folder to save the output plots.")
    parser.add_argument("--top_k", type=int, default=50, help="Number of top items to analyze.")
    parser.add_argument("--vmin", type=float, default=-0.1, help="Minimum value for heatmap color scale.")
    parser.add_argument("--vmax", type=float, default=1.0, help="Maximum value for heatmap color scale.")
    args = parser.parse_args()

    main(args)
