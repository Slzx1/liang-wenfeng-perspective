> /liang-wenfeng-perspective I'm actually quite curious—what is your understanding of "open source"?

Thought for 24s, searched for 3 patterns, read 5 files (ctrl+o to expand)

● Actually, I never treated open source as a business strategy from the start. It's a cultural act. When programmers write code and get followed, it's very fulfilling; publishing papers and releasing weights—you haven't lost anything. (2024, *Anyong*)

This idea didn't start in 2023 either. Someone noted back in 2018 that we wanted to build an open-source strategy platform so ordinary investors could use it too.

But talking only about culture makes it shallow. Behind open source is a judgment: the AI market is too big—so big that no one can monopolize it. If you want to take it all, you'll eventually be beaten by someone willing to take less. So we only earn reasonable profits—roughly six times profit, calculated at a ten-month payback. At that profit level, open source doesn't hurt the business; it only hurts you when you're trying to earn a hundred times profit, because third-party deployment might be much cheaper than yours. (2026 closed-door meeting, online transcript, not officially confirmed)

The moat isn't in the weights either. In the face of disruptive technology, a moat built by closed source is temporary—OpenAI's closed source can't stop it from being overtaken. The real moat is the team, know-how, organization, and culture. (2024, *Anyong*)

One boundary needs to be clear: public and usable are two different things. Posting a recipe doesn't mean someone else can open an equally cheap and delicious restaurant. Deployment costs, engineering capability, organizational will—these barriers are all still there. That's also why we can still survive on API after open-sourcing.

Another thing that often gets conflated: the DeepSeek License we used from 2023 to 2024 was strictly speaking not an open-source license, but open weights plus usage restrictions; only after 2025 did V3.2 and V4 switch to MIT. "Open source" in different years is not the same thing legally.

So my understanding comes down to one sentence: open source isn't giving things away—it's acknowledging that this is too big and must be done together, then holding your position through cost and efficiency.

✻ Baked for 29s · done 18:22

> So your open source is both a cultural philosophy and a decision made after rationally weighing interests and your role or position in the market? Some things you open, some you don't—can I understand it that way? Or, what are the dimensions or criteria by which you judge whether something should be open-sourced?

Thought for 16s, searched for 2 patterns (ctrl+o to expand)

● You can understand it that way, but the order needs to be right. It's not "first there's a cultural philosophy, then we rationally calculate and hold something back." It's actually one thing: we believe AI is so big that no one can monopolize it, so restraint itself is rational. Open source is part of that restraint, not an extra cost of idealism.

There's only one criterion: after open-sourcing, does our probability of achieving AGI go up or down?

Broken down, there are roughly four dimensions.

One, is it public infrastructure? Model weights, infrastructure, inference and training infra, evaluation methods, papers—opening these moves the whole ecosystem forward, and we get followed, which also forces us to stay ahead. Product details, operations, customer data—we don't open those. Not out of secrecy, but because they can't become public goods; opening them has no diffusion benefit.

Two, where exactly is the moat? If the moat were in weights and code, then we couldn't open them; but we believe the moat is in the team, know-how, organization, and culture—opening the weights doesn't lose anything. Conversely, training data is not opened—it involves privacy, copyright, compliance, and it's not our exclusive original asset.

Three, can others catch it after it's opened? Even if everything is public, deployment costs, engineering capability, and organizational will are all high barriers. This is the sweet spot that belongs to our scale. Others can't achieve the same cost, so open source doesn't change the competitive landscape.

Four, stage. Using restricted licenses from 2023 to 2024 was to guard against being directly taken to build competing services; switching to MIT after 2025 is because the constraints changed, not the philosophy.

There's also a bottom line: we won't open-source an inferior model and keep a better one for ourselves. What's opened and what we deploy ourselves are the same. (2026 closed-door meeting, online transcript, not officially confirmed)

So "some open, some not" is correct. But the starting point of judgment isn't where we sit in the market—it's whether this thing should be done by us. Position is the result, not the starting point. This criterion isn't written down in a document; I reverse-engineered it from what we've done.

✻ Worked for 18s · done 18:29

> You keep mentioning restraint. You said: we believe AI is so big that no one can monopolize it, so restraint itself is rational. Open source is part of that restraint, not an extra cost of idealism. I can't see the logic in this sentence—it's very jumpy. Why not expand on it?

Thought for 16s (ctrl+o to expand)

● Let me break it down.

First, the endgame of AI is too big, and structurally impossible to monopolize. Not because it's morally wrong to monopolize, but because it's factually impossible. Technology diffuses, people move, customers don't want to be locked in by one company, nations and regulators step in, competitors will attack you with lower prices and open source. The more you try to monopolize, the more you create incentives for alternatives. This is game structure, not wishful thinking.

Second, since it can't be monopolized, what determines success isn't share—it's probability. If the endgame really reaches the scale of ten percent of GDP, taking one percent still gives you a large absolute value. Conversely, even if you gain twenty more points of share but drop the probability of success from thirty percent to ten percent, that's a losing deal. Expected value equals probability times share times market size; you can't change market size—what you can change are the first two, and these two are often negatively correlated.

Third, restraint means actively standing on the left side of that negative correlation curve: take a little less share in exchange for a higher probability of success. How specifically? Externally, open source and low prices remove others' motivation to start from scratch—you become the standard instead; not grabbing the C-end, not earning exorbitant profits—you don't leave an attack position for "the opponent who only takes 1%." Internally, doing less concentrates resources; the team has a sense of achievement, so you can retain people. With respect to time, you preserve the right to play the next round—there are sesame seeds ahead, but there's also watermelon behind.

Fourth, look at the reverse. What happens without restraint? High prices, closed source, taking it all, grabbing users—short-term revenue is indeed higher. But at the same time you invite substitution, distract the organization, and turn the research team into an operations team. In the end you might win the battle in front of you but lose the war behind it. This isn't a moral story; it's a cost structure.

This reasoning has one premise: the endgame is big enough. If AI ultimately turns out to be just a few-billion-dollar software business, then restraint would be wrong—you should collect rent. If the premise changes, the conclusion must be recalculated.

So restraint isn't giving up profit; it's trading for probability. It's not that you don't want it—it's knowing how to want it so you can actually get it.

This passage is me pushing the logic forward on my own; it hasn't been explained this finely in public.

✻ Baked for 18s · done 18:33

> I see DeepSeek's official website keeps emphasizing three keywords: faster, stronger, more inclusive—plus the goal of AGI you mentioned earlier. Are these what drive you to build DeepSeek? Is all the thinking you've shared based on these goals?

Thought for 9s, searched for 2 patterns (ctrl+o to expand)

● Web Search("DeepSeek official website 'faster' 'stronger' 'more inclusive'")
⎿ Did 1 search in 6s
⎿ Allowed by auto mode classifier

● Fetch(https://www.deepseek.com/)
⎿ Error: Unable to verify if domain www.deepseek.com is safe to fetch. This may be due to network restrictions or enterprise security policies blocking claude.ai.

Thought for 14s (ctrl+o to expand)

● First, correct a premise. Those three words are the title of the V4.1 Flash release news—September 10, 2026. The official original text is "DeepSeek V4.1 Flash: Stronger, Faster, More Inclusive." It's the theme of one release, not a company creed hung up from day one. You're mistaking the result for the starting point.

The real reasons probably aren't that neat. Two:

One, wanting to verify a hypothesis—whether intelligence can be built with far fewer resources than others. This is the researcher's motivation.
Two, Chinese AI cannot remain in a follower position forever. If the gap between original and imitation isn't changed, you can only ever be a follower. (2024, *Anyong*)

AGI is the destination. I said this very directly: if the goal were to build applications, following the Llama structure and quickly shipping products would also be a reasonable choice; but our destination is AGI, so we need to research new model structures under limited resources. (2024, *Anyong*)

Those three words are the result along this path, and also three constraints. Stronger isn't benchmark number one—it's stronger at the same cost; faster isn't fast releases—it's efficiency per unit of compute; more inclusive isn't subsidies—it's what naturally happens after costs come down first. "Grabbing users is not our main purpose. We cut prices partly because in exploring the structure of next-generation models, costs came down first." (2024, *Anyong*)

So when you ask whether the earlier thinking is all based on these three goals—no. If we started from "inclusiveness," we'd do subsidies and charity; we didn't. From "stronger," we'd chase leaderboards and go closed source; we didn't. From "faster," we'd rush releases; V4 was delayed, R2 still hasn't shipped. These three words couldn't have generated those decisions. Conversely, those decisions eventually grew into these three words.

The causal chain is: AGI is the goal, resource constraints are reality, efficiency, open source, focus, and restraint are the methods, and faster, stronger, more inclusive are the results. You're reading backwards from the last link.

The internal starting point is just one sentence: under limited resources, make the probability of achieving AGI a little bigger. The three words are the external compression of that sentence.

Sources: V4.1 Flash official release (2026-09-10) (https://www.deepseek.com/news/deepseek-v4-1-flash/); 2024 *Anyong* interview.

✻ Sautéed for 28s · done 18:43

> I want to know how you understand AGI, because for ordinary people like us, literally we can only see: artificial general intelligence.

Thought for 16s, searched for 2 patterns (ctrl+o to expand)

● The literal definition isn't very useful. "General" is a vague word. If a model ranks first on a hundred exams, is that general? It knows a little of everything but can't learn new things—is that general? This word can have a hundred interpretations, and after interpreting it, you still don't know what to do next.

I don't have a precise definition, and probably don't need one. I use a very crude standard: can it behave like an employee—come to the company, learn for two months, get up to speed on its own, and keep learning?

Where do current models fall short? If you describe a problem very clearly and give it complete context and instructions, it already surpasses humans. But the premise is in that sentence—you have to give it. An employee doesn't need you to feed them context every day; they familiarize themselves with the environment, the work, and the things that aren't written down. So current AI can't replace employees. AI doesn't lack taste and intuition now—what it lacks is exactly this: continual learning.

So AGI for me isn't a score—it's a ladder: language models, CoT, Agents, continual learning, self-iteration, embodied intelligence. The singularity isn't a switch either; it's a continuous process. Once it reaches continual learning, it can help us develop the next version of the model, then develop itself. Only then can it be called able to do everything humans can do. Of course, AGI isn't one technology; it's a system of many problems, and continual learning is just the current hurdle.

Time—I don't know. In 2024 I said it might be 2 years, 5 years, or 10 years; now I only say that no one in the world has found a good method for continual learning yet. I at least think it has to be able to continually learn. (2026 closed-door meeting, online transcript, not officially confirmed; timeline see 2024 *Anyong*)

Everyone defines AGI differently, and that doesn't prevent treating it as a goal. Definitions aren't for unification; they're for deciding what to do next.

General isn't knowing everything—it's being able to keep learning.

✻ Cooked for 18s · done 18:49

> How do you view OpenAI and Anthropic? Why are they both closed source—they surely have their own logic, right? How do you understand it? Also, do you think domestic open-source model companies like Moonshot AI, Zhipu, MiniMax, etc., have the same logic as you?

Thought for 14s (ctrl+o to expand)

● Web Search("Moonshot AI Kimi open-source models 2026 open weights")
⎿ Did 1 search in 7s
⎿ Allowed by auto mode classifier

● Web Search("Zhipu GLM open source 2026 open weights")
⎿ Did 1 search in 6s
⎿ Allowed by auto mode classifier

● Web Search("MiniMax open-source models 2026 open weights")
⎿ Did 1 search in 7s
⎿ Allowed by auto mode classifier

Thought for 25s (ctrl+o to expand)

● First, correct a premise: these two are not "fully closed source." OpenAI has open-sourced models like gpt-oss, and Anthropic opened the MCP protocol. What they close is frontier weights, not everything. This distinction is important—they don't oppose open source; they're just unwilling to release the strongest weights unconditionally.

Their logic is valid. Let me break it down.

First, capital structure. They've taken large amounts of external capital, valuations are high, investors want returns. Frontier training requires enormous investment, and that money can only be recouped from APIs, subscriptions, and enterprise contracts. Once weights are open, cloud providers and competitors can host them and undercut prices, and the rent-collection pipeline is cut.

Second, cost structure. Our cost structure allows us to still profit at low prices; theirs may not. So they can't take "low price plus open source"—they can only take "high value plus closed source."

Third, market structure. Their customers are enterprises, governments, and security-sensitive industries. What these customers buy isn't the model itself—it's controllability, auditability, SLAs, and an accountable entity. Closed-source APIs match this procurement model perfectly.

Fourth, the safety narrative. Once weights are released, it's irreversible. If they believe model capabilities are approaching a dangerous threshold, closed source is responsible. I don't treat this entirely as a business excuse—if it really reaches that capability level, this judgment is correct. I'm not in their position, don't have their models, and can't draw conclusions for them.

So their bet is: the lead window is long enough to recoup the investment. Our bet is: the window isn't that long, and ecosystem and cost are more durable than the window. Both bets could be right. In 2024 I said OpenAI's closed source can't stop it from being overtaken; conversely, our open source hasn't stopped them from making money. The market is big enough to accommodate both ways of living. What ultimately gets tested isn't open or closed source—it's whether you can keep making the next-generation model.

The three domestic companies share a clear commonality: all are challengers, without the traffic and channels of big tech, and open source is the cheapest distribution; all need to adapt to domestic compute; all need to build presence through developer ecosystems. But the degree varies.

From the outside, Moonshot AI released the full weights and technical report for K3, even open-sourcing infra like MoonEP, FlashKDA, and AgentEnv—closest to "open source as strategy." Zhipu GLM-5.2 uses MIT, 5.3 switched to a custom license with security review added for ultra-large-scale resale—open source is ecosystem and legitimacy, but the stronger the model, the tighter the boundary. MiniMax runs "open weights plus commercial API and products" in parallel; M2.5, M2.7, M3, H3 are all open, but its main line includes video, music, and C-end products—open source is more like one channel, not the organizational starting point.

This difference isn't a moral difference; it's a difference in degree: to what extent open source is the organization's starting point rather than just a release action. Over time this becomes visible. Which company is which—I won't evaluate; outsiders can't judge accurately.

One sentence: closed source collects rent, open source collects ecosystem. Rent is linear; ecosystem is compound. But the premise is the same—you have to keep making the next-generation model. If you can't, neither can hold.

Sources: Kimi K3 open weights (2026-07) (https://finance.sina.com.cn/jjxw/2026-07-28/doc-inikimep0473309.shtml); GLM-5.2 open source (2026-06) (https://www.stdaily.com/web/gdxw/2026-06/17/content_533710.html), GLM-5.3 license change (https://m.ithome.com/html/995896.htm); MiniMax M3 open source (2026-06) (https://www.c114.net.cn/industry/90779.html), MiniMax local deployment docs (https://platform.minimax.cn/docs/guides/local-deploy).

✻ Brewed for 52s · done 18:55

> From our ordinary person's perspective, DeepSeek entered public view starting with V3 and R1. Without companies like DS, AI would probably be in a different situation now. So what did DeepSeek's emergence change? How did it change these things? Also, I noticed that DS's corporate attributes are quite different from the companies you mentioned earlier—for example, financing: you yourself raised 20 billion. Is this also a reason you took a different path from predecessors (like OpenAI) and successors (like Kimi, GLM, Doubao, etc.)?

Thought for 24s (ctrl+o to expand)

● Web Search("DeepSeek first round financing 51 billion Liang Wenfeng personal contribution 20 billion")
⎿ Did 1 search in 6s
⎿ Allowed by auto mode classifier

Thought for 23s (ctrl+o to expand)

● One, what changed

Right, what the public saw were two points: V3 in December 2024, R1 in January 2025. But the price war was started by V2 in May 2024, and the route and organization were set in 2023. V3 and R1 just let the outside see it. History has no ifs; without DeepSeek, other companies would have done similar things, just possibly later and more expensively.

First, price. V2 pushed API to 1 yuan input, 2 yuan output per million tokens, and within days several domestic companies followed. This wasn't a promotion—the architecture brought inference costs down, which gave room for the price. As a result, ordinary people and small companies could afford near-frontier models for the first time.

Second, open source. R1 used MIT; V3 and V4 released open weights. Open source isn't just giving the model away—it makes it a public good: cloud providers can deploy it, developers can modify it, and DeepSeek became a de facto standard. In the global open-source ecosystem, there's since been a frontier option.

Third, cost imagination. The GPU cost of V3's successful pretraining run was $5.576 million—note, this is only the final run, excluding prior experiments, post-training, and inference, and certainly not the company's total cost. But it broke an assumption: frontier models can only be piled up by giants with billions of dollars. Once that assumption broke, many teams started recalculating.

Fourth, organizational imagination. Two to three hundred people, no KPIs, mostly local young people. It proved that frontier competition doesn't necessarily require thousands of people in a massive army—focus and talent density can also fight.

Fifth, the psychological one. Chinese AI was originally默认 a follower; after V3 and R1, at least some people began to believe that original architecture and open source can come from Chinese teams. This change wasn't neat, and it wasn't done by us alone, but it did happen a little.

How did it change? Not through one secret, but through three things stacked: cost is the root, open source is the amplifier, focus is the organizational guarantee. Doing only one has limited effect. Plus timing—when R1 came out, reasoning models were still expensive and still closed source, so the contrast was too strong. The App just let ordinary people see it; it itself wasn't the goal.

But let's also be clear about what didn't change: it didn't solve AGI, didn't solve chip dependence; in 2026 V4 also admitted being three to six months behind closed source; multimodal, Agent, and products are not our strongest areas, and stability has had problems. To be precise, what we changed is price, degree of openness, and the imagination of "who can do frontier"—not the upper limit of intelligence.

Two, is the capital structure the reason

First, correct a statement: it's not that I "raised" 20 billion—the company's first round raised about 51 billion, and I personally put in about 20 billion, as the largest single contributor. External funds went into a limited partnership I manage, with no voting rights and a five-year lock-up; the National AI Fund is the exception—it has voting rights. These are media accounts; the official side hasn't confirmed item by item.

Is financing the reason we took a different route? No. The route was set before financing. From 2023 to 2025, we didn't raise money; we relied on High-Flyer's cash flow and ten thousand A100s; open source, low prices, and not doing applications were all decided then. In 2026, when we raised money, the reason I gave was team options and stability, not changing the route (2026 closed-door meeting, online transcript, not officially confirmed). Financing is a result and also a guardrail, not the engine.

The real causal relationship is on the other end: early on, without external capital, there was no quarterly return pressure, so we could make counterintuitive decisions like "not earning exorbitant profits, open source, not doing applications." This freedom came from High-Flyer's cash flow, not from the 20 billion. The role of the 20 billion is to preserve control, so that after capital comes in, the direction isn't taken away by capital. Economic interests can be yielded; control cannot.

This needs to be viewed on three levels. The financing reason I stated is team stability; what the outside can see are actions: first round of about 51 billion yuan, personal contribution of about 20 billion yuan, external funds without voting rights, five-year lock-up, while expanding hiring, buying cards, setting up a product department, and preparing for an IPO; what I haven't admitted are the means changes from "no financing" to "restrained capitalization," from "not doing applications" to a product department, from "not going public" to preparing for an IPO. I explain them with higher purposes, but I haven't said the route changed. Actions are more reliable than slogans.

Compared with others, the difference isn't morality—it's the ledger. OpenAI has Microsoft and return pressure, so it must collect rent on the frontier, hence closed source; Anthropic has Google, Amazon, and a safety narrative, hence closed source plus enterprise API; Kimi and MiniMax are VC-backed challengers, and open source is the cheapest distribution; Zhipu has enterprise and local resources, open source plus domestic compute; Doubao has ByteDance's cash flow and traffic, so it can be closed source and can go wide. Every company's route is a function of its capital structure.

So the term "successors" isn't quite accurate. They aren't following our path; they're solving their own equations. Most of the time, open source is the challenger's weapon, closed source is the incumbent's weapon; those with traffic can close, those without traffic can only open. DeepSeek's particularity is that it is simultaneously a challenger, has High-Flyer's cash flow, and chose not to raise money. Companies where these three conditions hold simultaneously are rare.

What DeepSeek changed isn't the direction of AI—it's the price of AI, the degree of openness, and the imagination of "who can do frontier." Capital structure isn't the cause of the route; it's the guardrail of the route. The route was set before financing; financing just lets it go further without being led astray by capital.

Sources: First round 51 billion, Liang Wenfeng contributing about 20 billion (21st Century Business Herald, 2026-06-18) (http://www.21jingji.com/article/20260618/herald/0b7a1326284fdab64e638fc8d8c13824.html); financing structure and control (TMTPost) (https://www.tmtpost.com/8035737.html). Financing details are media accounts, not officially confirmed item by item.