# API定价页-V4.1-Flash与V4-Pro

- URL: https://api-docs.deepseek.com/quick_start/pricing
- 抓取日期: 2026-10-17
- 来源: DeepSeek官方
- 证据级别: 一手
- 说明: DeepSeek官方API定价页，抓取时点价格。

---

Models & Pricing | DeepSeek API Docs

Skip to main content
On this page
Models & Pricing

Model prices are listed in units of per 1M tokens. A token, the smallest unit of text that the model recognizes, can be a word, a number, or even a punctuation mark. We bill model usage based on the total number of input and output tokens by the model.

Model Details
​

MODEL
deepseek-flash
(1)
deepseek-v4-pro
BASE URL (OpenAI Format)
https://api.deepseek.com
BASE URL (Anthropic Format)
https://api.deepseek.com/anthropic
MODEL VERSION
DeepSeek-V4.1-Flash
DeepSeek-V4-Pro-0813
THINKING MODE
Supports both non-thinking and thinking (default) modes
See 
Thinking Mode
 for how to switch
CONTEXT LENGTH
1M
MAX OUTPUT
MAXIMUM: 384K
FEATURES
Json Output
✓
✓
Tool Calls
✓
✓
Responses API
✓
✓
Anthropic API
✓
✓
Chat Prefix Completion（Beta）
✓
✓
FIM Completion（Beta）
Non-thinking mode only
Non-thinking mode only
Vision
✓
Not supported
PRICING
(2)
1M INPUT TOKENS
(CACHE HIT)
OFF-PEAK
$0.003
$0.022
PEAK
$0.006
$0.044
1M INPUT TOKENS
(CACHE MISS)
OFF-PEAK
$0.15
$0.66
PEAK
$0.3
$1.32
1M OUTPUT TOKENS
OFF-PEAK
$0.6
$1.98
PEAK
$1.2
$3.96
Concurrency Limit
(3)
2500
500

(1) Use 
deepseek-flash
 as the model name. The legacy names 
deepseek-v4-flash
 and 
deepseek-v4-flash-vision-exp
 are still accepted, but the corresponding models have been retired, their requests are served by the DeepSeek-V4.1-Flash model and billed at the Flash price.
(2) Off-peak rates are half of the peak rates. Peak hours are 01:00 - 04:00 and 06:00 - 10:00 UTC, Monday through Friday, excluding Chinese public holidays. All other hours are off-peak, including weekends and Chinese public holidays in full.
(3) For more details on concurrency limits, please refer to 
Rate Limit & Isolation
.

Search & Fetch Pricing
​

Search and Fetch are standalone APIs billed per request.

API
Unit
Price
Search
Per 1,000 successful requests
$0.75
Fetch
Per 1,000 successful requests
$0.75

Web search in Claude Code and Codex:
 Search requests made through Claude Code's built-in Web Search tool or Codex's 
web_search
 feature will not incur Search API request fees during the first two weeks after the Search API launch. Standard Search API pricing applies after that period; the billing start date will be announced separately.

See the 
Search & Fetch guide
 for API usage and complete billing rules.

Deduction Rules
​

For model usage, the expense = number of tokens × price. Search and Fetch are charged per successful request at the rates above.
The corresponding fees will be directly deducted from your topped-up balance or granted balance, with a preference for using the granted balance first when both balances are available.

Product prices may vary and DeepSeek reserves the right to adjust them. We recommend topping up based on your actual usage and regularly checking this page for the most recent pricing information.
Model Details
Search & Fetch Pricing
Deduction Rules
