# -*- coding: utf-8 -*-
import os, re
from bs4 import BeautifulSoup

OUT = r"D:\Projects\Liang-WenFeng\release\articles"
FETCH = r"C:\Users\LZX\AppData\Local\Temp\fetch"


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


def clean_body(title, paras):
    start = 0
    key = re.sub(r"[^\w\u4e00-\u9fff]", "", title)[:12]
    for i, p in enumerate(paras[:40]):
        pk = re.sub(r"[^\w\u4e00-\u9fff]", "", p)
        if key and (key in pk or pk[:12] in key):
            start = i
            break
    return paras[start:]


items = [
    dict(f="tencent_10points.html", date="2026-04-28", src="腾讯云开发者社区", title="细数DeepSeek V4给我留下的10个不爽的点", url="https://cloud.tencent.cn/developer/article/2661667", typ="用户/开发者批评（情绪化）", note="个人开发者视角；价格、下架V3、无多模态、限频、Token消耗；可信度低但反映真实用户情绪"),
    dict(f="donews_altman2.html", date="2026-06-20", src="DoNews", title="梁文锋不想当Sam Altman", url="https://www.donews.com/article/detail/5164/103667.html", typ="评论（中性）", note="控制权、融资条款、与任正非/马云/张一鸣对比"),
    dict(f="c114_idealist2.html", date="2026-07-24", src="C114/光通信Pro", title="理想主义者梁文锋：克制与野心并不相悖，愿景和现实却难弥合", url="https://www.c114.net.cn/industry/103481.html", typ="评论（褒贬混合）", note="克制战略、团队流失、现实张力"),
    dict(f="zaobao_probe.html", date="2026-09-23", src="联合早报", title="据报中国调查DeepSeek和月之暗面数据安全问题", url="https://www.zaobao.com/news/china/story20260923-9719718", typ="国际新闻（转述The Information/彭博）", note="CAC约谈、Anthropic指控、美国三机构公告"),
    dict(f="sina_mofcom.html", date="2026-09-10", src="环球时报/新浪财经", title="中方反驳美AI蒸馏指责：商务部称于事无凭于法无据", url="https://finance.sina.com.cn/jjxw/2026-09-10/doc-inirhvxe7958756.shtml", typ="中国官方回应（立场鲜明）", note="外交部/商务部表态；专家反驳；需与美方公告对读"),
    dict(f="liang_angry.html", date="2026-07-26", src="网易（转述彭博）", title="梁文锋生气了：DeepSeek暂停第二轮融资", url="https://www.163.com/dy/article/L2PLMV8N05568W0A.html", typ="二手转述（彭博匿名信源）", note="纪要外泄触发的融资暂停"),
    dict(f="tan_org.html", date="2026-07-23", src="网易/谭亮", title="梁文锋的组织实验：愿景驱动、无组织、共识校验", url="https://www.163.com/dy/article/L2R8KHFA05568W0A.html", typ="组织分析（偏正面）", note="作者谭亮，组织研究者；对“无组织”叙事的分析"),
]

for it in items:
    path = os.path.join(FETCH, it["f"])
    if not os.path.exists(path):
        print("MISSING", it["f"])
        continue
    title, paras = extract(path)
    body = clean_body(title, paras)
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
