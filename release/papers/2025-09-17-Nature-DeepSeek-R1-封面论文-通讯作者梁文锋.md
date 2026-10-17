# DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning（Nature 封面论文）

- URL: https://www.nature.com/articles/s41586-025-09422-z
- 期刊: Nature 645, 633–638 (2025)
- Received: 2025-02-14; Accepted: 2025-07-17; Published: 2025-09-17
- 作者: Daya Guo, Dejian Yang, Haowei Zhang, ... Wenfeng Liang, ...（DeepSeek-AI 团队，按字母序）
- 通讯作者: **Wenfeng Liang（梁文锋）** — 原文 “Correspondence to Wenfeng Liang”
- 性质: **梁文锋为通讯作者的个人署名论文**（团队集体工作），是本项目最重要的一手学术文本
- 抓取日期: 2026-10-17

## 摘要（逐字，英文原文）

Abstract
General reasoning represents a long-standing and formidable challenge in artificial intelligence (AI). Recent breakthroughs, exemplified by large language models (LLMs)
1
,
2
and chain-of-thought (CoT) prompting
3
, have achieved considerable success on foundational reasoning tasks. However, this success is heavily contingent on extensive human-annotated demonstrations and the capabilities of models are still insufficient for more complex problems. Here we show that the reasoning abilities of LLMs can be incentivized through pure reinforcement learning (RL), obviating the need for human-labelled reasoning trajectories. The proposed RL framework facilitates the emergent development of advanced reasoning patterns, such as self-reflection, verification and dynamic strategy adaptation. Consequently, the trained model achieves superior performance on verifiable tasks such as mathematics, coding competitions and STEM fields, surpassing its counterparts trained through conventional supervised learning on human demonstrations. Moreover, the emergent reasoning patterns exhibited by these large-scale models can be systematically used to guide and enhance the reasoning capabilities of smaller models.




## 关键事实（据论文页面与公开报道）

- 论文主张：仅用纯强化学习（pure RL）即可激励 LLM 的推理能力，无需人工标注的推理轨迹。
- 涌现行为：self-reflection（自我反思）、verification（验证）、dynamic strategy adaptation（动态策略调整）。
- 训练基座：DeepSeek-V3 Base；使用 GRPO；仅以最终答案正确性为奖励。
- 期刊定位：据 Nature 与中文媒体报道，这是首个经过完整独立同行评审并登上 Nature 封面的大语言模型研究；审稿意见要求减少拟人化表述、澄清“开源”含义、补充数据污染防护。
- 竞争利益声明：作者声明无竞争利益，且不会就论文内容申请专利。

## 备注

- 本文件只保存摘要与书目信息，未复制论文全文（版权限制）。
- 这是对“论文不是梁本人署名”这一预设的直接反证：至少 Nature 版 R1 论文明确标注梁文锋为通讯作者。
