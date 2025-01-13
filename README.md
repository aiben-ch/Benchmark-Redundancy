<div align="center">
    
    
 <div>

  
  <h1>Redundancy Principles for MLLMs Benchmarks</h1>
  
_Where Redundancy Exists? and Why Evaluate Redundancy?_

  <div>
      <a href="https://zzc-1998.github.io/" target="_blank">Zicheng Zhang</a><sup>1,2</sup><sup>*</sup>,
      <a href="" target="_blank">Xiangyu Zhao</a><sup>1,2</sup><sup>*</sup>,
      <a href="" target="_blank">Xinyu Fang</a><sup>1,3</sup>,
      <a href="https://github.com/lcysyzxdxc" target="_blank">Chunyi Li</a><sup>1,2</sup>,
      <a href="https://scholar.google.ca/citations?user=Tq2hoMQAAAAJ&hl=en" target="_blank">Xiaohong Liu</a><sup>2</sup>,
  </div>

<div>
     <a href="https://minxiongkuo.github.io/" target="_blank">Xiongkuo Min</a><sup>2</sup>,
     <a href="" target="_blank">Haodong Duan</a><sup>1</sup><sup>#</sup>,
     <a href="" target="_blank">Kai Chen</a><sup>1</sup><sup>#</sup>,
      <a href="https://ee.sjtu.edu.cn/en/FacultyDetail.aspx?id=24&infoid=153&flag=153" target="_blank">Guangtao Zhai</a><sup>1</sup><sup>#</sup>
      
  </div>
  <div>
  <sup>1</sup>Shanghai AI Lab, <sup>1</sup>Shanghai Jiaotong University,  <sup>2</sup>Nanyang Technological University
       </div>   
<div>
<sup>*</sup>Equal contribution. <sup>#</sup>Corresponding authors. 
   </div>
  <a href=""><strong>Paper</strong></a> |
  <a href=""><strong>Project Page</strong></a> |
 <a href=""><strong>Github</strong></a> |
  <div style="width: 100%; text-align: center; margin:auto;">
      <img style="width:60%" src="ceaser.png">
  </div>
  
<div align="left">
    
The rapid growth of MLLM benchmarks has inevitably led to significant redundancy among benchmarks. 
Therefore, it is crucial to take a step back and critically assess the current state of redundancy and propose targeted principles for constructing effective MLLM benchmarks.
Specifically, we focus on redundancy from three key perspectives:
**1) Redundancy of benchmark capability dimensions**, 
**2) Redundancy in the number of test questions**, 
and **3) Cross-benchmark redundancy within specific domains**.
 


  
## Redundancy Framework
    


<table>
  <tr>
    <td><img src="framework.png" alt="Description" style="width: 1200px;"></td>
    <td style="padding-left: 60px;">
      <h3>Dimensions Redundancy</h3>
      <p>$$\rho(X_i) = \frac{1}{m-1} \sum_{\substack{j=1 \\ j \neq i}}^m \text{CORR}(R_i, R_j),$$ </p>
      <p>where $$\\\text{CORR}(R_i, R_j)$$ is the correlation coefficient between the rankings $$R_i$$ and $$R_j$$. The rankings $$R_i$$ and $$R_j$$ are the performance ranking of MLLMs on i-th and j-th dimensions of the benchmark.</p>
        <hr>
        <h3>Instances Redundancy</h3>
      <p>$$\rho(A\%) = \text{CORR}(R_{A\%}, R_{\text{GT}})$$,</p>
      <p></p> where $$R_{A\%}$$ is the MLLM ranking based on the sampled $$A\%$$ instances, and $$R_{\text{GT}}$$ is the MLLM ranking based on all instances within the MLLM benchmark.
        <hr>
        <h3>Cross-Benchmark Redundancy</h3>
      <p>$$\rho(Y_i) = \frac{1}{l-1} \sum_{\substack{j=1 \\ j \neq i}}^l \text{CORR}(K_i, K_j), $$</p>
    <p>where $$\text{CORR}(K_i, K_j)$$ is the correlation coefficient between the rankings $$K_i$$ and $$K_j$$. The rankings $$R_i$$ and $$R_j$$ are the performance ranking of MLLMs on i-th and j-th benchmarks of the specific domain.</p>
    </td>
  </tr>
</table>


# Redundancy Results
<h3>PDF Viewer</h3>
<iframe src="example.pdf" width="100%" height="600px" style="border: none;"></iframe>


## Contact

Please contact any of the first authors of this paper for queries.

- Zicheng Zhang, `zzc1998@sjtu.edu.cn`, @zzc-1998


## Citation

If you find our work interesting, please feel free to cite our paper:

```bibtex

```
