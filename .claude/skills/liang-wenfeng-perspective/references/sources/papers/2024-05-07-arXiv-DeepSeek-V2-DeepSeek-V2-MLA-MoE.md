# Title:DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model

- URL: https://arxiv.org/abs/2405.04434
- 提交日期: 7 May 2024 (v1), last revised 19 Jun 2024 (this version, v5)
- 作者署名: 论文正文署名 “DeepSeek-AI”（公司集体署名）；arXiv 元数据作者列表包含 Wenfeng Liang
- 性质: 公司级技术报告，可归因于梁文锋领导，但不是其个人执笔
- 抓取日期: 2026-10-17

## 摘要（逐字，英文原文）

Abstract:We present DeepSeek-V2, a strong Mixture-of-Experts (MoE) language model characterized by economical training and efficient inference. It comprises 236B total parameters, of which 21B are activated for each token, and supports a context length of 128K tokens. DeepSeek-V2 adopts innovative architectures including Multi-head Latent Attention (MLA) and DeepSeekMoE. MLA guarantees efficient inference through significantly compressing the Key-Value (KV) cache into a latent vector, while DeepSeekMoE enables training strong models at an economical cost through sparse computation. Compared with DeepSeek 67B, DeepSeek-V2 achieves significantly stronger performance, and meanwhile saves 42.5% of training costs, reduces the KV cache by 93.3%, and boosts the maximum generation throughput to 5.76 times. We pretrain DeepSeek-V2 on a high-quality and multi-source corpus consisting of 8.1T tokens, and further perform Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) to fully unlock its potential. Evaluation results show that, even with only 21B activated parameters, DeepSeek-V2 and its chat versions still achieve top-tier performance among open-source models.

## 备注

- 本文件保存的是 arXiv 官方摘要页的完整摘要，未改写。
- 技术报告正文中的方法、消融与结论属于 DeepSeek 团队集体工作；引用为“公司级文本”。
