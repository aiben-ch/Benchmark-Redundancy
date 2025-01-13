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
 


  
## A-Bench Construction
    
Two key diagnostic subsets are defined: **A-Bench-P1** → high-level semantic understanding, and **A-Bench-P2** → low-level quality perception. For high-level semantic understanding, **A-Bench-P1** targets three critical areas: *Basic Recognition, Bag-of-Words Pitfalls Discrimination*, and *Outside Knowledge Realization*, which are designed to progressively test the LMM’s capability in AIGI semantic understanding, moving from simple to complex prompt-related content. For low-level quality perception, **A-Bench-P2** concentrates on *Technical Quality Perception, Aesthetic Quality Evaluation*, and *Generative Distortion Assessment*, which are designed to cover the common quality issues and AIGI-specific quality problems. 

Specifically, a comprehensive dataset of 2,864 AIGIs sourced from various T2I models is compiled, including 1,408 AIGIs for **A-Bench-P1** and 1,456 for **A-Bench-P2**. Each AIGI is paired with a question-answer set annotated by human experts.
We are open to **submission-based evaluation** for **A-Bench**. The details for submission are in the **Evaluate your model on A-Bench** Section.

  <div style="width: 100%; text-align: center; margin:auto;">
      <img style="width:100%" src="examples.png">
  </div>

  


## Contact

Please contact any of the first authors of this paper for queries.

- Zicheng Zhang, `zzc1998@sjtu.edu.cn`, @zzc-1998


## Citation

If you find our work interesting, please feel free to cite our paper:

```bibtex

```
