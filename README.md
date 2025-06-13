# Swarm intelligence for new materials 🧬🔬

## Description

This project implements and explores a novel hybrid swarm intelligence algorithm to optimize neural network parameters for predicting material properties, specifically focusing on crystal structure energies. The approach aims to enhance the efficiency and accuracy of traditional neural network models in the field of computational materials science, aiding in the discovery and design of new materials.

The core methodology is inspired by the paper "Swarm intelligence for new materials", which proposes an improved genetic algorithm (GA) by integrating Particle Swarm Optimization (PSO) and Bayesian optimization techniques.

---

## 🎯 Motivation

Traditional neural network training methods for materials science applications often suffer from:
* Low efficiency and accuracy.
* A tendency to get stuck in local optima.
* Difficulty in converging effectively, leading to models with low predictive power.

This project addresses these challenges by employing a sophisticated optimization strategy to find better neural network parameters, leading to more stable and precise models.

---

## 📓 Notebooks

Explore the material-specific experiments in the following Jupyter notebooks:

* 📘 [CaTiO₃.ipynb](CaTiO3.ipynb)
* 📗 [TiO₂.ipynb](TiO2.ipynb)
* 📕 [VO₂.ipynb](VO2.ipynb)

---

## 📊 Data

The original paper uses datasets for materials like Si, $TiO_2$, $VO_2$, and $CaTiO_3$, with energies calculated by their group. The dataset used in this project should be compatible with the input expected by the neural network (e.g., structural descriptors like Chebyshev polynomials). A link to the dataset used in the paper is available: https://data.mendeley.com/datasets/gr3c7m44jn/2.

---

## 📜 Reference

This project is based on the methods and ideas presented in the following research paper:

* Liu, Z., Guo, J., Chen, Z., Wang, Z., Sun, Z., Li, X., & Wang, Y. (2022). Swarm intelligence for new materials. *Computational Materials Science*, 214, 111699. [https://doi.org/10.1016/j.commatsci.2022.111699](https://doi.org/10.1016/j.commatsci.2022.111699)
