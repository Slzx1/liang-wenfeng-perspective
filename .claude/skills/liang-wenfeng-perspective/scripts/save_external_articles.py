# -*- coding: utf-8 -*-
import os, re
from bs4 import BeautifulSoup

OUT = r"D:\Projects\Liang-WenFeng\release\articles"
FETCH = r"C:\Users\LZX\AppData\Local\Temp\fetch"
os.makedirs(OUT, exist_ok=True)


def extract(path):
    html = open(path, encoding="utf-8", errors="ignore").read()
    soup = BeautifulSoup(html, "lxml")
    for t in soup(["script", "style", "noscript", "svg", "nav", "footer", "header", "form"]):
        t.decompose()
    title = soup.title.get_text(strip=True) if soup.title else ""
    cands = soup.find_all(["article", "main"])
    if not cands:
        cands = soup.find_all("div", class_=re.compile(r"(content|article|post|text|body)", re.I))
    best = max(cands, key=lambda c: len(c.get_text())) if cands else soup.body or soup
    paras = []
    for el in best.find_all(["h1", "h2", "h3", "h4", "p", "li", "blockquote"]):
        txt = el.get_text(" ", strip=True)
        txt = re.sub(r"\s+", " ", txt)
        if len(txt) > 20 and txt not in paras:
            paras.append(txt)
    return title, paras


def clean_body(title, paras, skip_patterns):
    start = 0
    key = re.sub(r"[^\w\u4e00-\u9fff]", "", title)[:12]
    for i, p in enumerate(paras[:40]):
        pk = re.sub(r"[^\w\u4e00-\u9fff]", "", p)
        if key and (key in pk or pk[:12] in key):
            start = i
            break
    out = []
    for p in paras[start:]:
        if any(re.search(pat, p) for pat in skip_patterns):
            continue
        out.append(p)
    return out


items = [
    dict(f="laojin.html", date="2026-04-02", src="晚点LatePost（经老金出海全文转述）", title="V4发布前的DeepSeek：特质、组织和梁文锋的独特目标", url="https://www.latepost.com/news/dj_detail?id=3489", typ="二手深度报道（原文LatePost，程曼祺）", note="转述页：https://www.laojinchuhai.com/zh/classics/deepseek-v4-before-latepost-2026；与已存LatePost原文互为参照"),
    dict(f="leiphone.html", date="2026-05-31", src="雷峰网", title="排名第九国内第二：DeepSeek V4凭什么让人又爱又恨", url="https://www.leiphone.com/category/industrynews/YpMEgldEnok4fRSn.html", typ="媒体评测（含批评）", note="V4基准排名、用户失望、中文场景复测"),
    dict(f="nfzm.html", date="2025-05-25", src="南方周末", title="梁文锋：俯身做真正的创新", url="https://view.inews.qq.com/k/20250525A06IL500", typ="人物特写（二手）", note="少见的梁文锋成长与创新观梳理"),
    dict(f="xinhuanghe.html", date="2026-08-06", src="中国新闻周刊（新黄河转载）", title="再次炸场，梁文锋的克制与代价", url="https://www.jinantimes.com.cn/news-67-5299068.html", typ="人物特写（含实习研究员一手回忆）", note="记者杨智杰；实习生池羽化名受访"),
    dict(f="jiemian_cap.html", date="2026-06-17", src="界面新闻", title="DeepSeek融资500亿：量化大佬梁文锋的反资本实验", url="https://m.jiemian.com/article/14614151.html", typ="财经分析（偏中性/赞叹）", note="84%受益股份、100%表决权、外部资本无投票权"),
    dict(f="huxiu_terms.html", date="2026-07-25", src="虎嗅", title="DeepSeek的悖论：一家不想赚钱的AI公司如何留住500亿投资人", url="https://www.huxiu.com/article/4877809.html", typ="深度分析（批评性）", note="幻觉、过度思考、开源护城河、三条负循环"),
    dict(f="stcn_4h2.html", date="2026-07-24", src="第一财经（证券时报转载）", title="梁文锋4小时投资会讲话流出：DeepSeek为什么不做更赚钱的公司", url="https://stcn.com/article/detail/4037119.html", typ="泄露实录报道（未经官方确认）", note="3.4万字纪要；第一财经求证未获回应；关键引语来源"),
    dict(f="21jing_6x.html", date="2026-07-24", src="21世纪经济报道", title="梁文锋内部分享曝光：开源不影响6倍利润", url="https://www.21jingji.com/article/20260724/herald/3668c4f33f3beb9033f52d71f554fee7.html", typ="泄露实录报道（未经官方确认）", note="6倍利润、10个月回本、开源最强模型"),
    dict(f="tmt_xianyue.html", date="2026-04-24", src="钛媒体", title="梁文锋的惊险一跃：当DeepSeek撞上算力账单与组织重构", url="https://www.tmtpost.com/7963833.html", typ="分析评论（批评性）", note="国产化迁移、人才流失、组织重构、5亿美元单轮训练估算"),
    dict(f="tmt_bawang.html", date="2026-06-17", src="钛媒体", title="太狂了！自掏200亿，梁文锋立下霸王条款", url="https://www.tmtpost.com/8035737.html", typ="分析评论（褒贬混合）", note="融资治理条款、幻方现金流、控制权"),
    dict(f="neican.html", date="2026-07-23", src="AI内参", title="克制的幻象与资本的贪婪：梁文锋的AI双重奏", url="https://www.neican.ai/insights/article-20260723181003349-0/", typ="评论（强批评）", note="指理想主义为品牌营销、创始人意志独裁、幻方收益反差"),
    dict(f="stcn_altman.html", date="2026-04-24", src="证券时报", title="梁文锋，终于活成了山姆·奥特曼的样子", url="https://www.stcn.com/article/detail/3803013.html", typ="分析评论（批评性）", note="理想主义转向融资、人才战、IPO"),
    dict(f="36kr_champagne.html", date="2026-06-18", src="36氪", title="起跑线还没过呢，香槟就开了", url="https://www.36kr.com/p/3858277427352577", typ="评论（强批评）", note="500亿美元估值/收入倍数、霸王条款、技术团队流失"),
    dict(f="36kr_sell.html", date="2026-09-30", src="36氪", title="不如卖给梁文锋", url="https://www.36kr.com/p/4028265517584768", typ="产业分析（中性偏批评）", note="具身智能投资、Coding见顶、GPT-6压力"),
    dict(f="em_ipo.html", date="2026-09-17", src="东方财富/中国经营报", title="DeepSeek被传筹备上市：商业化仍面临考验", url="https://finance.eastmoney.com/a/202609173877652085.html", typ="财经分析（审慎）", note="估值、营收4.75亿、API真实需求疑问"),
    dict(f="guandian.html", date="2026-10-15", src="观点网", title="DeepSeek的数字天平：站在5000亿估值与5小时宕机之间", url="https://www.guandian.cn/article/20261015/613697.html", typ="财经评论（批评性）", note="年内18次服务异常、算力增速8.3%、估值与产能脱节"),
    dict(f="sina_highflyer2021.html", date="2021-12-29", src="新浪财经", title="千亿私募道歉：幻方量化业绩大幅回撤", url="https://finance.sina.com.cn/stock/hyyj/2021-12-29/doc-ikyakumx7021987.shtml", typ="当时报道（一手引述公司致歉）", note="2021年历史最大回撤、暂停申购、免赎回费"),
    dict(f="em_laoshu.html", date="2025-11-25", src="东方财富/界面新闻", title="涉幻方量化？IT人员老鼠仓领1.77亿元罚单", url="https://fund.eastmoney.com/a/202511253574018544.html", typ="调查报道（监管文书为基础）", note="浙江证监局处罚；文书未点名幻方，媒体比对股权"),
    dict(f="caixin_nature.html", date="2025-09-18", src="财新", title="DeepSeek登上《自然》封面：梁文锋团队详解大模型如何试错自主学习", url="https://science.caixin.com/2025-09-18/102363859.html", typ="科学报道（正面/中性）", note="R1论文通讯作者梁文锋；同行评审"),
    dict(f="thepaper_97.html", date="2026-04-27", src="澎湃新闻", title="梁文锋留住97%员工", url="https://m.thepaper.cn/newsDetail_forward_33101044", typ="媒体分析（正面/中性）", note="V4报告作者名单10人离职；离职率对比"),
    dict(f="ithome_v4authors.html", date="2026-04-25", src="IT之家", title="DeepSeek-V4技术报告公开作者名单：多位核心骨干离职去大厂", url="https://www.ithome.com/0/944/264.htm", typ="事实报道", note="王炳宣、魏浩然、郭达雅等10人标注离职"),
    dict(f="21jing_ipo.html", date="2026-07-16", src="21世纪经济报道", title="DeepSeek或冲刺A股IPO：4800亿估值引行业热议", url="https://m.21jingji.com/article/20260716/herald/9d99c55c939b1e2c3ec3d177978c1b60.html", typ="财经分析（审慎）", note="估值三个月翻七倍、上市风险"),
    dict(f="chinatimes_lowcost.html", date="2026-05-05", src="中时新闻网", title="AI前沿解密：DeepSeek V4低成本神话的现实界线", url="https://www.chinatimes.com/opinion/20260505002286-262110", typ="评论（批评性）", note="V4市场反应平稳、产品化/多模态/API稳定性短板"),
    dict(f="time_liang.html", date="2025-08-29", src="TIME", title="Liang Wenfeng: The 100 Most Influential People of 2025", url="https://time.com/collections/100-most-influential-people-2025/7273745/liang-wenfeng/", typ="国际人物榜评（正面）", note="Charlie Campbell撰；6000亿美元市值蒸发叙事"),
    dict(f="businesstimes_halt.html", date="2026-07-26", src="Business Times/Bloomberg", title="DeepSeek suspends fundraising after founder's alleged US-China AI comments go viral", url="https://www.businesstimes.com.sg/startups-tech/deepseek-suspends-fundraising-after-founders-alleged-us-china-ai-comments-go-viral-sources", typ="国际调查报道（匿名信源）", note="融资暂停、纪要外泄、未核实"),
    dict(f="smh_nerd.html", date="2025-01-29", src="Sydney Morning Herald/Bloomberg", title="The 40-year-old reclusive nerd behind DeepSeek eyes massive fortune", url="https://www.smh.com.au/business/companies/meet-the-40-year-old-nerd-behind-deepseek-20250129-p5l7wy.html", typ="国际人物特写（中性）", note="幻方2021回撤、资产缩水三分之一、梁的量化背景"),
    dict(f="financialpost_richest.html", date="2026-07-14", src="Bloomberg（Financial Post转载）", title="DeepSeek's Liang tops list of richest AI founders", url="https://financialpost.com/personal-finance/high-net-worth/deepseeks-liang-richest-ai-founder", typ="国际财经报道（中性）", note="360亿美元净资产、78%持股、全球最富AI模型创始人"),
    dict(f="csis_allen.html", date="2025-03-07", src="CSIS", title="DeepSeek, Huawei, Export Controls, and the Future of the U.S.-China AI Race", url="https://www.csis.org/analysis/deepseek-huawei-export-controls-and-future-us-china-ai-race", typ="智库报告（竞争视角）", note="承认真实突破、驳“纯偷窃/宣传”、成本与芯片分析"),
    dict(f="csis_hawkish.html", date="2025-04-16", src="CSIS Futures Lab", title="Hawkish AI? Uncovering DeepSeek's Foreign Policy Biases", url="https://www.csis.org/analysis/hawkish-ai-uncovering-deepseeks-foreign-policy-biases", typ="智库评测（批评性）", note="DeepSeek-V3在外交危机场景偏鹰派/升级"),
    dict(f="semianalysis_debates.html", date="2025-01-27", src="SemiAnalysis", title="DeepSeek Debates: Chinese Leadership On Cost, True Training Cost, Closed Model Margin Impacts", url="https://newsletter.semianalysis.com/p/deepseek-debates", typ="半导体研究（强批评成本叙事）", note="5亿美元硬件、16亿美元服务器CapEx、5万Hopper"),
    dict(f="nature_r1.html", date="2025-09-17", src="Nature", title="DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning", url="https://www.nature.com/articles/s41586-025-09422-z", typ="同行评审论文（正面/中性）", note="梁文锋通讯作者；首个登Nature封面的前沿大模型论文"),
    dict(f="scmp_cost.html", date="2026-05-20", src="South China Morning Post", title="DeepSeek's cost-saving AI may lead to inaccuracy in model performance: research", url="https://www.scmp.com/tech/tech-trends/article/3370550/deepseeks-cost-saving-ai-may-lead-inaccuracy-model-performance-research", typ="国际科技报道（批评性）", note="V4长上下文“周期性盲区”，未同行评审"),
    dict(f="hindustan_economist.html", date="2026-01-23", src="The Economist（Hindustan Times转载）", title="Chinese AI is a risk for Europe. So is shunning it", url="https://www.economist.com/china/2026/01/22/chinese-ai-is-a-risk-for-europe-so-is-shunning-it", typ="国际评论（中性偏正面）", note="中国开放权重领先、欧洲两难、数据安全顾虑"),
    dict(f="row_openai.html", date="2026-02-12", src="Rest of World", title="OpenAI accuses DeepSeek of malpractice ahead of AI launch", url="https://restofworld.org/2026/openai-deepseek-distillation-dispute-us-china/", typ="国际调查报道（批评/争议）", note="OpenAI致美国众议院中国委员会备忘录；蒸馏指控"),
    dict(f="row_founders.html", date="2025-01-30", src="Rest of World", title="DeepSeek's low-cost AI model challenges OpenAI's dominance", url="https://restofworld.org/2025/deepseek-ai-model-openai-dominance-challenge/", typ="国际报道（多元评价）", note="全球南方创业者视角；成本、数据透明度、IP争议"),
    dict(f="row_talent.html", date="2025-02-10", src="Rest of World", title="China's AI talent fueled DeepSeek's rise, challenging U.S. dominance", url="https://restofworld.org/2025/china-ai-talent-deepseek-rise-us-dominance/", typ="国际报道（中性）", note="本土人才、实习生文化、与字节薪酬对比"),
    dict(f="tc_v4.html", date="2026-04-24", src="TechCrunch", title="DeepSeek previews new AI model that 'closes the gap' with frontier models", url="https://techcrunch.com/2026/04/24/deepseek-previews-new-ai-model-that-closes-the-gap-with-frontier-models/", typ="国际科技报道（中性）", note="V4参数、价格、3-6个月差距、蒸馏指控背景"),
    dict(f="wired_bytedance.html", date="2025-12-01", src="WIRED", title="ByteDance and DeepSeek Are Placing Very Different AI Bets", url="https://wired.com/story/deepseek-goes-high-while-bytedance-goes-wide/", typ="国际科技分析（对比）", note="DeepSeek go high vs 字节 go wide；R2缺席"),
    dict(f="foreignpolicy_hawkish.html", date="2025-03-04", src="Foreign Policy", title="AI Agents Show Escalation Bias in National Security Scenarios", url="https://foreignpolicy.com/2025/03/04/ai-bias-national-security-study/", typ="国际政策评论（批评性）", note="AI代理在危机中偏升级；DeepSeek被纳入讨论"),
    dict(f="csis_deepdive.html", date="2025-04-08", src="CSIS", title="DeepSeek: A Deep Dive (Congressional Testimony)", url="https://www.csis.org/analysis/deepseek-deep-dive", typ="美国国会证词（竞争视角）", note="Gregory Allen；成本、H800、出口管制"),
    dict(f="recruit_ft.html", date="2025-02-03", src="Financial Times（Recruit Engineering转述）", title="Have we hit peak tech bro?（DeepSeek founder as anti-tech bro）", url="https://www.ft.com/content/cd2966ed-c458-4485-87a8-a483b79b8457", typ="国际评论（正面/中性）", note="付费墙；仅能获取转述摘要，非全文"),
    dict(f="ex_employee.html", date="2025-09-15", src="网易（转述外媒对前员工采访）", title="前员工谈梁文锋：他视我们为专家，一起学习，下放管理权，没有996", url="https://m.163.com/dy/article/JPAV4R8H0519U3I5.html", typ="二手转述（十余名前员工匿名采访）", note="原始媒体未标明；匿名前员工Liu等；可信度中等"),
]

skip = [r"^36氪Auto", r"^企业号 企服点评", r"^创投发布", r"^项目推荐", r"^资讯 推荐", r"^首页$", r"^登录$", r"^搜索$"]
for it in items:
    path = os.path.join(FETCH, it["f"])
    if not os.path.exists(path):
        print("MISSING", it["f"])
        continue
    title, paras = extract(path)
    body = clean_body(title, paras, skip)
    text = "\n\n".join(body)
    md = (
        f"# {it['title']}\n\n- URL: {it['url']}\n- 来源: {it['src']}\n"
        f"- 发布日期: {it['date']}\n- 抓取日期: 2026-10-17\n- 类型: {it['typ']}\n"
        f"- 备注: {it['note']}\n\n---\n\n{text}\n"
    )
    src_short = it["src"].split("（")[0].replace("/", "-")
    fn = f"{it['date']}-{src_short}-{it['title'][:40]}.md"
    fn = re.sub(r'[\\/:*?"<>|]', "-", fn)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(md)
    print("SAVED", fn, len(text))
