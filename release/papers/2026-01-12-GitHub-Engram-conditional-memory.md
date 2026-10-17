# Engram: Conditional Memory via Scalable Lookup — A New Axis of Sparsity for LLMs

- URL: https://github.com/deepseek-ai/Engram
- 仓库创建: 2026-01-12
- 性质: 公司级研究代码与论文，非梁文锋个人执笔
- 抓取日期: 2026-10-17

## README 原文（节选）

## 1. Introduction
This repository contains the official implementation for the paper: **[Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models](Engram_paper.pdf)**.
> **Abstract:** While Mixture-of-Experts (MoE) scales capacity via conditional computation, Transformers lack a native primitive for knowledge lookup. To address this, we explore **conditional memory** as a complementary sparsity axis, instantiated via **Engram**, a module that modernizes classic $N$-gram embeddings for $\mathcal{O}(1)$ lookup.
**Key Contributions:**
- **Sparsity Allocation:** We formulate the trade-off between neural computation (MoE) and static memory (Engram), identifying a U-shaped scaling law that guides optimal capacity allocation.
- **Empirical Verification:** Under strict iso-parameter and iso-FLOPs constraints, the Engram-27B model demonstrates consistent improvements over MoE baselines across knowledge, reasoning, code and math domains.
- **Mechanistic Analysis:** Our analysis suggests that Engram relieves early layers from static pattern reconstruction, potentially preserving effective depth for complex reasoning.
- **System Efficiency:** The module employs deterministic addressing, enabling the offloading of massive embedding tables to host memory with minimal inference overhead.
## 2. Architecture
The Engram module augments the backbone by retrieving static $N$-gram memory and fusing it with dynamic hidden states. The architecture is shown below ([drawio provided](drawio/Engram.drawio)):
## 3. Evaluation
### Scaling Law
---
### Large Scale Pre-training
---
### Long-context Training
## 4. Case Study of Engram
## 5. Quick Start
We recommend using Python 3.8+ and PyTorch.
```bash
pip install torch numpy transformers sympy
```
We provide a standalone implementation to demonstrate the core logic of the Engram module:
```bash
python engram_demo_v1.py
```
> ⚠️ **Note:** The provided code is a demonstration version intended to illustrate the data flow. It mocks standard components (like Attention/MoE/mHC) to focus on the Engram module.
## 6. License
The use of Engram models is subject to [the Model License](LICENSE).
## 7. Contact
If you have any questions, please raise an issue or contact us at [service@deepseek.com](mailto:service@deepseek.com).
