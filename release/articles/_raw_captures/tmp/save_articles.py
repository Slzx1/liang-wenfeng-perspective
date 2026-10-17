# -*- coding: utf-8 -*-
import os, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
base = r'D:/Projects/Liang-WenFeng/release/tmp/'
outdir = r'D:/Projects/Liang-WenFeng/release/articles/'
os.makedirs(outdir, exist_ok=True)
items = [
('highflyer_history','2026-10-17-幻方官网-幻方历程.md','https://www.high-flyer.cn/history/','幻方量化官网','访问日期 2026-10-17','幻方历程（2008-2022）','官方一手'),
('hzdaily_jan20','2025-01-22-都市快报-梁文锋成总理座上宾.md','https://hzdaily.hangzhou.com.cn/dskb/2025/01/22/article_detail_2_20250122A021.html','都市快报','2025-01-22','这家杭州科技公司创始人为何成为总理的“座上宾”','主流媒体'),
('tidenews_thesis','2025-02-13-潮新闻-梁文锋硕士论文公开.md','https://tidenews.com.cn/news.html?id=3043280','潮新闻（浙江日报）','2025-02-13','首次曝光！15年前，梁文锋在浙大硕士论文中写了什么','主流媒体/校方配合'),
('zaobao_feb17','2025-02-17-联合早报-习近平民营企业座谈会梁文锋握手.md','https://www.zaobao.com.sg/realtime/china/story20250217-5890523','联合早报','2025-02-17','习近平：民营经济发展前景广阔 正是民企大显身手之时','主流媒体（央视截图）'),
('stcn_nature','2025-09-18-证券时报-DeepSeek登Nature封面.md','https://www.stcn.com/article/detail/3345648.html','证券时报','2025-09-18','DeepSeek，打破历史！中国AI的“Nature时刻”','主流媒体'),
('ds_v32_official','2025-12-01-DeepSeek官方-V3.2正式版.md','https://api-docs.deepseek.com/zh-cn/news/news251201/','DeepSeek API Docs','2025-12-01','DeepSeek V3.2 正式版：强化 Agent 能力，融入思考推理','官方一手'),
('xinhua_nature10','2025-12-09-新华社-Nature2025十大人物梁文锋.md','https://english.news.cn/20251209/3504815f2720463a8562238e22523310/c.html','新华社英文','2025-12-09','DeepSeek founder Liang Wenfeng named to Nature influential 2025 list','官方通讯社'),
('legis1_ndaa','2025-12-18-Legis1-FY2026NDAA禁用DeepSeek条款.md','https://legis1.com/news/fy2026-ndaa-cybersecurity-ai-1-embeds-governance','Legis1','2025-12-18','FY2026 NDAA Embeds Cyber and AI Governance Rules','专业法律/政策媒体'),
('thepaper_mhc','2026-01-04-澎湃-梁文锋署名mHC论文.md','https://m.thepaper.cn/newsDetail_forward_32307568','澎湃新闻·湃客（大数据文摘）','2026-01-04','下一代模型呼之欲出？！DeepSeek的新年礼物mHC是个啥？','行业媒体（论文可查）'),
('latepost_v4','2026-04-02-晚点LatePost-V4发布前的DeepSeek.md','https://www.latepost.com/news/dj_detail?id=3489','晚点LatePost','2026-04-02','V4 发布前的 DeepSeek：特质、组织和梁文锋的独特目标','一线深度报道'),
('ds_260424','2026-04-24-DeepSeek官方-V4预览版.md','https://api-docs.deepseek.com/zh-cn/news/news260424','DeepSeek API Docs','2026-04-24','DeepSeek-V4 预览版：迈入百万上下文普惠时代','官方一手'),
('ql1d_capital','2026-04-28-齐鲁晚报-DeepSeek注册资本1500万梁文锋持股34.md','https://www.ql1d.com/general/27541124.html','齐鲁晚报·齐鲁壹点','2026-04-28','DeepSeek注册资本增至1500万元，创始人梁文锋持股比例由1%升至34%','主流媒体（企查查数据）'),
('stcn_may_finance','2026-05-12-证券时报-DeepSeek500亿首轮融资.md','https://stcn.com/article/detail/3904065.html','证券时报','2026-05-12','DeepSeek 500亿元首轮融资震动投资圈！投后估值或超过3500亿元','主流财经媒体'),
('sina_gaokao2026','2026-06-10-新浪财经-梁文锋高考状元照.md','https://finance.sina.com.cn/wm/2026-06-10/doc-iniaxkrt1273470.shtml','新浪财经（21ic电子网）','2026-06-10','梁文锋高考状元照曝光！超清华分数线，选择了浙大','转载/自媒体，细节待核'),
('hangzhou_finance','2026-06-16-杭州网-DeepSeek完成500亿融资.md','https://news.hangzhou.com.cn/jjxw/content/2026-06/16/content_9240492_2.htm','杭州网/潮新闻','2026-06-16','DeepSeek完成500亿融资，腾讯、京东、宁德时代、网易等入股','主流媒体'),
('21jj_june_finance','2026-06-17-21世纪经济报道-DeepSeek完成510亿融资.md','https://www.21jingji.com/article/20260617/herald/8dcb42cb34717c8adc5b01e8b4584255.html','21世纪经济报道','2026-06-17','传DeepSeek完成500亿元融资','主流财经媒体'),
('c114_leak','2026-07-23-36氪-梁文锋4小时118问实录.md','https://www.c114.net.cn/industry/103193.html','36氪/腾讯科技（C114转载）','2026-07-23','4小时、11个话题、118次回答，梁文锋内部交流回应一切','泄露实录，未经官方确认'),
('donews_pause','2026-07-26-DoNews-DeepSeek暂停第二轮融资.md','https://www.donews.com/news/detail/1/6646814.html','DoNews（引彭博社）','2026-07-26','消息：梁文锋对闭门谈话纪要外泄不满，DeepSeek暂停第二轮融资','外媒转述，未经官方确认'),
('hk01_wealth','2026-08-12-HK01-梁文锋身价395亿美元.md','https://www.hk01.com/即時中國/60379197/','香港01','2026-08-12','DeepSeek梁文锋身价暴增38.5倍 挤进全球前50富','主流媒体（BestBrokers数据）'),
('ds_260813','2026-08-13-DeepSeek官方-V4Pro正式版.md','https://api-docs.deepseek.com/zh-cn/news/news260813','DeepSeek API Docs','2026-08-13','DeepSeek-V4-Pro 正式版上线','官方一手'),
('eastmoney_aug_capital','2026-08-26-南方财经-DeepSeek3年增资15倍.md','https://finance.eastmoney.com/a/202608263854456436.html','南方财经网','2026-08-26','杭州深度求索人工智能基础技术研究有限公司3年增资15倍','主流财经媒体（天眼查数据）'),
('ds_260910','2026-09-10-DeepSeek官方-V4.1Flash.md','https://api-docs.deepseek.com/zh-cn/news/news260910','DeepSeek API Docs','2026-09-10','DeepSeek V4.1 Flash：更强、更快、更普惠','官方一手'),
('sfccn_cfo','2026-09-24-南方财经-严文韬出任DeepSeekCFO.md','https://www.sfccn.com/2026/9-24/1MMDE0MDdfMjI1MTU1MA.html','南方财经网/国际金融报','2026-09-24','DeepSeek补上CFO一席，严文韬将操盘上市？','主流财经媒体'),
('36kr_revenue','2026-09-28-36氪-DeepSeek年化营收10亿美元.md','https://eu.36kr.com/zh/p/3998096784562053','36氪（Tech商业）','2026-09-28','DeepSeek在IPO前夕将年营收翻番至10亿美元','行业媒体（引The Information）'),
('ithome_ascend','2026-09-30-IT之家-DeepSeek开源昇腾组件.md','https://m.ithome.com/html/1008604.htm','IT之家','2026-09-30','DeepSeek 开源面向华为昇腾算力平台的基础设施组件','主流科技媒体'),
('eastmoney_round2','2026-10-09-21世纪经济报道-DeepSeek二轮融资或达千亿.md','https://finance.eastmoney.com/a/202610093890076259.html','21世纪经济报道','2026-10-09','DeepSeek新一轮融资或达千亿 “豪赌”国产算力预训练','主流财经媒体'),
('ifeng_round2','2026-10-13-凤凰网-DeepSeek二轮融资增至1000亿.md','https://tech.ifeng.com/c/8xBUB27gPIa','凤凰网科技（引《财经》）','2026-10-13','消息称DeepSeek二轮融资增至1000亿元，投前估值约5000亿元','主流媒体'),
('guandian_oct15','2026-10-15-观点网-DeepSeek5000亿估值与5小时宕机.md','https://www.guandian.cn/article/20261015/613697.html','观点网','2026-10-15','DeepSeek的数字天平：站在5000亿估值与5小时宕机之间','行业媒体，部分数据待核'),
('21jj_highflyer2025','2026-01-14-21世纪经济报道-幻方2025收益56.6.md','https://m.21jingji.com/article/20260114/herald/c28662157ae4f0d9f2c7c944101a35ad_zaker.html','21世纪经济报道','2026-01-14','幻方量化去年收益率56.6%，为DeepSeek提供超级弹药','主流财经媒体'),
('ds_260821','2026-08-21-DeepSeek官方-V4FlashVisionExp.md','https://api-docs.deepseek.com/zh-cn/news/news260821','DeepSeek API Docs','2026-08-21','V4-Flash-Vision-Exp 上线，开启多模态 API 服务','官方一手'),
]
for tmp, fn, url, src, date, title, conf in items:
    p = base + tmp + '.txt'
    if not os.path.exists(p):
        print('MISSING', p)
        continue
    txt = open(p, encoding='utf-8', errors='ignore').read()
    txt = txt[:20000]
    header = "# %s\n\n- URL: %s\n- 来源: %s\n- 发布日期: %s\n- 抓取日期: 2026-10-17\n- 可信度: %s\n\n---\n\n" % (title, url, src, date, conf)
    open(outdir + fn, 'w', encoding='utf-8').write(header + txt)
    print('WROTE', fn, len(txt))
