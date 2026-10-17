# Title:DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence

- URL: https://arxiv.org/abs/2606.19348
- 提交日期: 26 Apr 2026
- 作者署名: 论文正文署名 “DeepSeek-AI”（公司集体署名）；arXiv 元数据作者列表包含 Wenfeng Liang
- 性质: 公司级技术报告，可归因于梁文锋领导，但不是其个人执笔
- 抓取日期: 2026-10-17

## 摘要（逐字，英文原文）

Abstract:We present a preview version of DeepSeek-V4 series, including two strong Mixture-of-Experts (MoE) language models -- DeepSeek-V4-Pro with 1.6T parameters (49B activated) and DeepSeek-V4-Flash with 284B parameters (13B activated) -- both supporting a context length of one million tokens. DeepSeek-V4 series incorporate several key upgrades in architecture and optimization: (1) a hybrid attention architecture that combines Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA) to improve long-context efficiency; (2) Manifold-Constrained Hyper-Connections (mHC) that enhance conventional residual connections; (3) and the Muon optimizer for faster convergence and greater training stability. We pre-train both models on more than 32T diverse and high-quality tokens, followed by a comprehensive post-training pipeline that unlocks and further enhances their capabilities. DeepSeek-V4-Pro-Max, the maximum reasoning effort mode of DeepSeek-V4-Pro, redefines the state-of-the-art for open models, outperforming its predecessors in core tasks. Meanwhile, DeepSeek-V4 series are highly efficient in long-context scenarios. In the one-million-token context setting, DeepSeek-V4-Pro requires only 27% of single-token inference FLOPs and 10% of KV cache compared with DeepSeek-V3.2. This enables us to routinely support one-million-token contexts, thereby making long-horizon tasks and further test-time scaling more feasible. The model checkpoints are available at this https URL.

## 备注

- 本文件保存的是 arXiv 官方摘要页的完整摘要，未改写。
- 技术报告正文中的方法、消融与结论属于 DeepSeek 团队集体工作；引用为“公司级文本”。
