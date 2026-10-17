# Title:DeepSeek-V3 Technical Report

- URL: https://arxiv.org/abs/2412.19437
- 提交日期: 27 Dec 2024 (v1), last revised 18 Feb 2025 (this version, v2)
- 作者署名: 论文正文署名 “DeepSeek-AI”（公司集体署名）；arXiv 元数据作者列表包含 Wenfeng Liang
- 性质: 公司级技术报告，可归因于梁文锋领导，但不是其个人执笔
- 抓取日期: 2026-10-17

## 摘要（逐字，英文原文）

Abstract:We present DeepSeek-V3, a strong Mixture-of-Experts (MoE) language model with 671B total parameters with 37B activated for each token. To achieve efficient inference and cost-effective training, DeepSeek-V3 adopts Multi-head Latent Attention (MLA) and DeepSeekMoE architectures, which were thoroughly validated in DeepSeek-V2. Furthermore, DeepSeek-V3 pioneers an auxiliary-loss-free strategy for load balancing and sets a multi-token prediction training objective for stronger performance. We pre-train DeepSeek-V3 on 14.8 trillion diverse and high-quality tokens, followed by Supervised Fine-Tuning and Reinforcement Learning stages to fully harness its capabilities. Comprehensive evaluations reveal that DeepSeek-V3 outperforms other open-source models and achieves performance comparable to leading closed-source models. Despite its excellent performance, DeepSeek-V3 requires only 2.788M H800 GPU hours for its full training. In addition, its training process is remarkably stable. Throughout the entire training process, we did not experience any irrecoverable loss spikes or perform any rollbacks. The model checkpoints are available at this https URL.

## 备注

- 本文件保存的是 arXiv 官方摘要页的完整摘要，未改写。
- 技术报告正文中的方法、消融与结论属于 DeepSeek 团队集体工作；引用为“公司级文本”。
