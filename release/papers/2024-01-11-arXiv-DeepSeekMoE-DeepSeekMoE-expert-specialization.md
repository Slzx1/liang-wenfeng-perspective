# Title:DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models

- URL: https://arxiv.org/abs/2401.06066
- 提交日期: 11 Jan 2024
- 作者署名: 论文正文署名 “DeepSeek-AI”（公司集体署名）；arXiv 元数据作者列表包含 Wenfeng Liang
- 性质: 公司级技术报告，可归因于梁文锋领导，但不是其个人执笔
- 抓取日期: 2026-10-17

## 摘要（逐字，英文原文）

Abstract:In the era of large language models, Mixture-of-Experts (MoE) is a promising architecture for managing computational costs when scaling up model parameters. However, conventional MoE architectures like GShard, which activate the top-$K$ out of $N$ experts, face challenges in ensuring expert specialization, i.e. each expert acquires non-overlapping and focused knowledge. In response, we propose the DeepSeekMoE architecture towards ultimate expert specialization. It involves two principal strategies: (1) finely segmenting the experts into $mN$ ones and activating $mK$ from them, allowing for a more flexible combination of activated experts; (2) isolating $K_s$ experts as shared ones, aiming at capturing common knowledge and mitigating redundancy in routed experts. Starting from a modest scale with 2B parameters, we demonstrate that DeepSeekMoE 2B achieves comparable performance with GShard 2.9B, which has 1.5 times the expert parameters and computation. In addition, DeepSeekMoE 2B nearly approaches the performance of its dense counterpart with the same number of total parameters, which set the upper bound of MoE models. Subsequently, we scale up DeepSeekMoE to 16B parameters and show that it achieves comparable performance with LLaMA2 7B, with only about 40% of computations. Further, our preliminary efforts to scale up DeepSeekMoE to 145B parameters consistently validate its substantial advantages over the GShard architecture, and show its performance comparable with DeepSeek 67B, using only 28.5% (maybe even 18.2%) of computations.

## 备注

- 本文件保存的是 arXiv 官方摘要页的完整摘要，未改写。
- 技术报告正文中的方法、消融与结论属于 DeepSeek 团队集体工作；引用为“公司级文本”。
