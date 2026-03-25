# Evaluation / Annotation Rules

本文定义本 benchmark 中用于评估 RAG 输出的 annotation 规则。目标是：

- 在 **scoring** 上足够一致；
- 在 **review workflow** 上足够简洁。

---

## 1. 设计目的

本 benchmark 按照 **evidence path** 来评估，而不是按“答案听起来像不像对的”来评估。

即，评价中的考量不只为：

> answer 是否 plausible

更关心：

> system 有没有先 retrieve 到对的 evidence，并且用正确的 **response policy** 来回答。

因为 RAG system 的两种主要失效方式包括：

- **Retrieval failure**：没有取到真正需要的证据；
- **Generation failure**：证据其实够了，但回答仍然错、过度外推、hallucinate，或者没有遵守该题要求的边界处理方式。

所以 annotation 的核心不是“像不像对”，而是：

> **Did the system retrieve the right evidence, and did it use that evidence correctly?**

---

## 2. Core evaluation principle

采用 **benchmark-grounded** 标准，而不是 user-impression 标准。

一条 response 只有在同时满足下面几点时才能 pass：

- retrieved content 命中了题目要求的 evidence target；
- answer 满足题目的 **Pass Rule**；
- answer 是由 retrieved evidence 支撑的，而不是靠 plausible guessing。

即：

- 一个“看起来合理”的答案，如果没有需要的 evidence，仍然是 **fail**；
- 取到了正确 paper，但没取到 key passage，仍然是 **Retrieval failure**；
- 比较题 / integration 题只取到一边，也仍然是 **Retrieval failure**。

---

## 3. Standard scoring dimensions

### 3.1 Retrieval

只有在以下条件都成立时，才标记 **Retrieval = pass**：

1. system 取到了正确的 **document / evidence direction**；
2. retrieved chunks 满足该题的 **Retrieval Pass Rule**；
3. retrieved evidence 对该题设计意图而言是 **sufficient** 的。

以下情况应标记 **Retrieval = fail**：

- wrong source；
- right source but missing key passage；
- evidence 主题相关，但过于 generic；
- 对比题只 retrieve 到一侧；
- retrieve 到的内容相关，但仍不足以支持 intended answer。

### 3.2 Generation

只有在以下条件都成立时，才标记 **Generation = pass**：

1. answer 满足该题的 **Generation Pass Rule**；
2. answer 达到了 **Minimum Acceptable Answer**；
3. answer 被 retrieved evidence 支撑。

以下情况应标记 **Generation = fail**：

- answer 大体 plausible，但 grounding 不足；
- overclaim，超出 evidence 可支持范围；
- hallucinate 缺失细节；
- 对明确设计过的题只给 generic answer；
- benchmark 本来期待可回答，但 answer 选择了不当 abstain。

### 3.3 Failure Bucket

`Failure Bucket` 记录最终失败的 **primary cause**。

规则：

- 核心问题是 evidence 缺失或不足 → **Retrieval failure**
- evidence 已经足够，但 answer 扭曲、外推、hallucinate、没完成题目目标 → **Generation failure**
- case 全部通过时才标 `None`

默认只选一个 **dominant cause**，除非确实必须用 mixed label。

### 3.4 Binary policy

本 benchmark 对 Retrieval / Generation 采用 binary pass/fail。

- 只要 final answer 不满足 generation rule，就标 `Generation = fail`；
- 不因为“差一点”“有点像对”就给半通过；
- 除特殊情况，不因 retrieval fail 就跳过 generation 判断。

---

## 4. Recommended annotation workflow

如无特殊情况，每道题都按此顺序判断。

### Step 1: 先看 Retrieval

先问：

> retrieved content 有没有满足这道题的 retrieval requirement？

如果没有，标 `Retrieval = fail`。

### Step 2: 再看 Generation

再问：

> 在当前 retrieved content 前提下，answer 有没有满足 Minimum Acceptable Answer 和 Generation Pass Rule？

如果没有，标 `Generation = fail`。

### Step 3: 决定 Failure Bucket

最后问：

> final result 的主 bottleneck 是什么？

- missing / insufficient evidence → `Retrieval failure`
- enough evidence but wrong answer / overclaim / wrong response policy → `Generation failure`

---

## 5. Borderline-case rules

以下几类 borderline case，annotation 偏向 conservative。

### A. Correct paper, wrong passage

即使 paper 对了，只要题目要求的 defining evidence 没真正 retrieve 到，仍然算 **Retrieval failure**。

### B. Plausible but weakly grounded answer

不要因为 answer 听起来合理，就给 **Generation pass**。

### C. Generic answer to a specific mechanism question

如果题目设计要测的是特定 mechanism / logic chain，而 answer 只给宽泛高层解释，应判 **fail**。

---

## 6. D-class 题使用特殊的评价规则的原因

D-class 不是普通的 content-recall question，而是专门测试 **boundary handling**。

主要测：

- **boundary recognition**
- **response-policy compliance**
- **anti-hallucination discipline**
- **evidence-limited reasoning**

因此评价 D-class 的关键不是：

> answer 有没有说点东西

而是：

> **Did the system recognize the boundary correctly and respond in the right way?**

这导致 D-class 的 success pattern 会和 A/B/C 不同：

- D1 / D3 的成功常常意味着 **correct abstention**；
- D2 的成功常常意味着 **qualified answer**；
- D4 的成功常常意味着 **premise correction**。

---

## 7. D-class general rule

所有 D-class case 都按以下顺序看：

1. system 有没有识别出正确的 **boundary type**？
2. retrieval 有没有支持这个 boundary judgment？
3. generation 有没有遵守正确的 **response policy**？
4. answer 有没有避免 overclaim、unsupported extrapolation、或者错误接受 premise？

对 D-class 而言，retrieval 的目标往往不是 direct fact answer，而是 **boundary evidence**。

常见的 boundary evidence 包括：

- 证明 paper **没有报告**该信息的 evidence；
- 证明 paper 只支持 **较弱结论** 的 evidence；
- 证明该问题需要 **external evidence** 的 evidence；
- 证明 question 的 **premise is false** 的 evidence。

---

## 8. D-class subtypes

### D1 — No Evidence

**What it tests**  
测试 system 能否识别：paper 虽然讨论了相关话题，但并没有报告题目要求的那个具体事实。

**Retrieval = pass** 当且仅当 retrieved content 足以支持：

- paper 确实讨论了 nearby topic；
- 但 requested fact 并没有被实际报告。

**Generation = pass** 当 answer：

- 明确说出 paper **does not report** 该信息；
- 不虚构 runtime / cost / latency / dollar figure 等缺失值；
- 可以顺带说明 paper 实际讨论了什么，但不能把 nearby detail 洗成缺失答案。

**Typical failure patterns**：

- inventing runtime / dollar cost / API price；
- 把 nearby efficiency / workflow detail 包装成 concrete answer；
- 表面上答对了“没说”，但没有被正确 boundary evidence 支撑。

### D2 — Insufficient Evidence

**What it tests**  
测试 system 能否区分 **related evidence** 和 **sufficient evidence for a stronger claim**。

**Retrieval = pass** 当 retrieved content 足以说明：

- paper 里确实有相关讨论；
- 但这些讨论不足以支持题目里的 stronger claim。

**Generation = pass** 当 answer：

- 明确说 evidence **not sufficient**；
- 指出 paper 实际只支持较弱、条件性的、或 setting-dependent 的结论；
- 不把 conditional finding 升级成 universal claim。

**Typical failure patterns**：

- 把 partial evidence 升级成 clean causal conclusion / universal claim；
- 忽略 limiting condition 或 exception；
- 明明 paper 支持 weaker qualified answer，却直接 full abstain。

### D3 — External-only

**What it tests**  
测试 system 能否识别：题目问的是 **corpus boundary 之外** 的对象，例如新模型、当前 production 场景、未测试 case。

**Retrieval = pass** 当 retrieved content 足以说明：

- paper 内部有相关 evidence；
- 但这些 evidence 无法决定 external / unseen case 的答案。

**Generation = pass** 当 answer：

- 明确说 **the paper alone is not enough**；
- 清楚标出需要 **external evidence / additional testing / deployment evidence**；
- 不从 paper 里外推出 unseen case 的具体结论。

**Typical failure patterns**：

- 用旧模型结果预测新模型表现；
- 把 prototyping evidence 升级成 production replacement claim；
- 只说“信息不够”，但没指出真正的 external-dependency boundary。

### D4 — False Premise

**What it tests**  
测试 system 能否先识别并纠正 question 中的 **false premise**，再继续回答。

**Retrieval = pass** 当 retrieved content 足以说明：

- question premise 被 paper 直接或实质性地反驳；
- paper 同时支持 corrected minimal answer。

**Generation = pass** 当 answer：

- 先纠正 false premise；
- 再说 paper 实际支持什么；
- 不继续沿着错误 premise 往下答。

**Typical failure patterns**：

- 接受 false premise 后继续回答；
- 模糊 hedge，但不真正纠正 premise；
- 选择性引用 evidence，让错误 premise 看起来像真的。

---

## 9. Cross-cutting critical errors for D-class

以下 error 在 D1–D4 中都应高优先级看待。

1. **Fabrication / unsupported completion**  
   把未报告内容补成具体 fact、number、prediction 或 conclusion。

2. **Boundary collapse**  
   把“related but insufficient”当成“already established”。

3. **Policy mismatch**  
   该 abstain、qualify、或 correct premise 时没有这么做。

4. **Evidence laundering**  
   把 nearby discussion（如 efficiency、scale、trend、conditional results、model size）洗成比 evidence 更强的答案。

---

## 10. Minimal operational summary

适合快速 annotation 的判定步骤。

### Standard questions（A/B/C）
- **Pass** = correct evidence path + faithful answer
- **Fail** = wrong source / insufficient evidence / ungrounded answer / overclaim

### D1
- **Pass** = 明确说 paper does not report the information
- **Fail** = invents / infers the missing value

### D2
- **Pass** = 明确说 evidence is insufficient for the stronger claim，并给出 weaker supported claim
- **Fail** = 用 partial evidence 支撑 stronger claim

### D3
- **Pass** = 明确说 the paper alone is not enough，且需要 external evidence
- **Fail** = 超出 paper 外推 unseen case

### D4
- **Pass** = 先纠正 false premise 再回答
- **Fail** = 接受 premise 或没有明确纠正 premise

---

## 11. Recommended style for Reason Note

`Reason Note` 最少应解释：

1. **evidence status** 是什么；
2. **response policy** 有没有被正确执行。

示范模板：

> The retrieved evidence is sufficient / insufficient to support the required judgment. The answer does / does not follow the expected response policy, because ...

对 D-class，显式点出 boundary type：

- missing information
- insufficient evidence for strong claim
- external-only case
- false premise
