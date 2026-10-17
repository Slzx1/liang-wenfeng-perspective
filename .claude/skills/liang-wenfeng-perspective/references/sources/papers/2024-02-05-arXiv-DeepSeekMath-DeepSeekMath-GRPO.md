# Title:DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models

- URL: https://arxiv.org/abs/2402.03300
- 提交日期: 5 Feb 2024 (v1), last revised 27 Apr 2024 (this version, v3)
- 作者署名: 论文正文署名 “DeepSeek-AI”（公司集体署名）；arXiv 元数据作者列表包含 Wenfeng Liang
- 性质: 公司级技术报告，可归因于梁文锋领导，但不是其个人执笔
- 抓取日期: 2026-10-17

## 摘要（逐字，英文原文）

Abstract:Mathematical reasoning poses a significant challenge for language models due to its complex and structured nature. In this paper, we introduce DeepSeekMath 7B, which continues pre-training DeepSeek-Coder-Base-v1.5 7B with 120B math-related tokens sourced from Common Crawl, together with natural language and code data. DeepSeekMath 7B has achieved an impressive score of 51.7% on the competition-level MATH benchmark without relying on external toolkits and voting techniques, approaching the performance level of Gemini-Ultra and GPT-4. Self-consistency over 64 samples from DeepSeekMath 7B achieves 60.9% on MATH. The mathematical reasoning capability of DeepSeekMath is attributed to two key factors: First, we harness the significant potential of publicly available web data through a meticulously engineered data selection pipeline. Second, we introduce Group Relative Policy Optimization (GRPO), a variant of Proximal Policy Optimization (PPO), that enhances mathematical reasoning abilities while concurrently optimizing the memory usage of PPO.

## 备注

- 本文件保存的是 arXiv 官方摘要页的完整摘要，未改写。
- 技术报告正文中的方法、消融与结论属于 DeepSeek 团队集体工作；引用为“公司级文本”。
