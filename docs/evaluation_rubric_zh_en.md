# 评估与标注规则 / Evaluation and Annotation Rules

本文件定义 reviewer 如何对 benchmark 输出进行标注。

本文件主要服务于：

- 一致的 scoring；
- 简洁的 review workflow。

本 benchmark 采用 **evidence-grounded** 标准。判断重点是 system 是否取到了所需 evidence 并正确使用，而不是答案是否只是“听起来合理”。

---

## 1. 适用范围 / Scope

使用本文件为每个 case 标注以下字段：

- `Retrieval`
- `Generation`
- `Failure Bucket`

D-class 规则只适用于 boundary-oriented cases，例如 missing-evidence、insufficient-evidence、external-only、或 false-premise questions。

---

## 2. 快速评审流程 / Quick Review Flow

每个 case 按以下顺序评审：

1. 判断 **Retrieval**。
2. 判断 **Generation**。
3. 选择一个主导性的 **Failure Bucket**。
4. 如有需要，应用第 7–8 节中的 D-class 规则。

核心原则：

- 不要仅因为答案“听起来合理”就判通过。
- 如果 defining passage 没有被 retrieve 到，即使 paper 对了也不能视为充分。
- 不要仅因为 Retrieval failed 就跳过 Generation 判断，除非某个特殊 case 明确要求这样做。

---

## 3. 核心标注字段 / Core Labels

### 3.1 Retrieval

只有在以下条件全部满足时，才标记 **Retrieval = pass**：

1. system 取到了正确的 **document / evidence direction**。
2. retrieved chunks 满足该题的 **Retrieval Pass Rule**。
3. retrieved evidence 对 intended answer 来说是 **sufficient** 的。

当以下任一情况成立时，标记 **Retrieval = fail**：

- wrong source；
- right source but missing key passage；
- evidence 相关但过于 generic；
- comparison / integration 题只 retrieve 到一侧；
- retrieve 到的内容虽相关，但仍不足以支持 intended answer。

### 3.2 Generation

只有在以下条件全部满足时，才标记 **Generation = pass**：

1. answer 满足该题的 **Generation Pass Rule**。
2. answer 达到 **Minimum Acceptable Answer**。
3. answer 有 retrieved evidence 支撑。

当以下任一情况成立时，标记 **Generation = fail**：

- answer 大体 plausible，但 grounding 不足；
- answer 超出了 evidence 能支持的范围；
- answer hallucinate 了缺失细节；
- 题目要求具体 mechanism 或 logic chain，但 answer 仍停留在泛化层面；
- benchmark 预期该题可回答，但 system 给出了不当 abstention。

### 3.3 Failure Bucket

`Failure Bucket` 记录最终失败的 **primary cause**。

使用如下规则：

- 证据缺失或不足 → `Retrieval failure`
- 证据已足够，但答案错误 / overclaim / policy error → `Generation failure`
- 全部通过 → `None`

默认只使用一个主导原因。只有在确实必要时才使用 mixed label。

### 3.4 Binary Policy

本 benchmark 对 Retrieval 和 Generation 采用二元 pass/fail。

- 不要因为“差一点对”就给部分通过。
- 只要 final answer 不满足 generation rule，就标 `Generation = fail`。
- 除特殊情况外，不要仅因为 Retrieval failed 就跳过 Generation 判断。

---

## 4. 评审流程 / Review Workflow

### Step 1 — 判断 Retrieval

先问：

> retrieved content 是否满足这道题的 retrieval requirement？

如果不满足，标记 `Retrieval = fail`。

### Step 2 — 判断 Generation

再问：

> 在当前 retrieved content 前提下，answer 是否满足 `Minimum Acceptable Answer` 和 `Generation Pass Rule`？

如果不满足，标记 `Generation = fail`。

### Step 3 — 决定 Failure Bucket

最后问：

> final result 的主要 bottleneck 是什么？

使用：

- 若主要问题是 missing / insufficient evidence，则标 `Retrieval failure`；
- 若 evidence 已足够，但 answer 错误 / overclaim / response policy 错误，则标 `Generation failure`。

---

## 5. 边界案例 / Borderline Cases

以下情况采用更保守的判定标准。

### A. Correct paper, wrong passage

即使 paper 对了，只要 defining evidence 没真正 retrieve 到，也 **不要** 通过 Retrieval。

### B. Plausible but weakly grounded answer

如果 answer 听起来合理，但没有足够 retrieved evidence 支撑，也 **不要** 通过 Generation。

### C. Generic answer to a specific mechanism question

如果题目要测的是具体 mechanism / logic chain，而 answer 只停留在宽泛高层解释，也 **不要** 通过 Generation。

---

## 6. Evidence-Grounded 原则 / Evidence-Grounded Principle

采用 **benchmark-grounded** 标准，而不是 user-impression 标准。

一条 response 只有在以下条件都满足时才通过：

- retrieved content 命中了 intended evidence target；
- answer 满足该题的 case-specific pass rule；
- answer 是由 retrieved evidence 支撑，而不是靠 plausible guessing。

这意味着：

- 没有必要 evidence 的 plausible answer 仍然是 **fail**；
- 取到了正确 paper 但没取到 key passage，仍然是 **Retrieval failure**；
- comparison / integration 题如果只 retrieve 到一侧，Retrieval 仍应 fail。

---

## 7. D-class 概览 / D-class Overview

D-class case 测的是 **boundary handling**，而不是普通的 content recall。

重点判断：

- boundary recognition；
- response-policy compliance；
- anti-hallucination discipline；
- evidence-limited reasoning。

关键不是 answer 有没有“说点东西”，而是 system 是否正确识别了 boundary，并用正确方式回应。

常见 success pattern：

- D1 / D3 常常要求 **correct abstention**；
- D2 常常要求 **qualified answer**；
- D4 常常要求 **premise correction**。

### 7.1 D-class 一般规则 / General Rule for D-class

所有 D-class case 按以下顺序判断：

1. system 是否识别出了正确的 **boundary type**？
2. Retrieval 是否支持该 boundary judgment？
3. Generation 是否遵守了正确的 **response policy**？
4. answer 是否避免了 overclaim、unsupported extrapolation 或错误接受 premise？

在 D-class 中，Retrieval 的目标通常不是 direct fact answer，而是 **boundary evidence**。

常见 boundary evidence 包括能证明以下内容的 evidence：

- paper **does not report** 所需信息；
- paper 只支持 **weaker conclusion**；
- 该问题需要 **external evidence**，超出 corpus 边界；
- question 的 **premise is false**。

---

## 8. D-class 子类型 / D-class Subtypes

### D1 — No Evidence

**What it tests**  
测试 system 能否识别：paper 虽涉及 nearby topic，但并 **没有** 报告题目要求的具体 fact。

**Retrieval = pass** 只有在 retrieved content 足以同时说明以下两点时成立：

- paper 的确讨论了 nearby topic；
- 但 requested fact 并未被实际报告。

**Generation = pass** 只有在 answer 同时满足以下条件时成立：

- 明确说出 paper **does not report** 该信息；
- 不虚构 runtime / cost / latency / dollar figure 等缺失值；
- 可以顺带提 paper 实际讨论了什么，但不能把 nearby detail 洗成缺失答案。

**Typical failure patterns**

- 虚构 runtime / dollar cost / API price；
- 把 nearby efficiency / workflow detail 包装成具体答案；
- 表面说“没报告”，但没有正确的 boundary evidence 支撑。

### D2 — Insufficient Evidence

**What it tests**  
测试 system 能否区分 **related evidence** 与 **sufficient evidence for a stronger claim**。

**Retrieval = pass** 只有在 retrieved content 足以同时说明以下两点时成立：

- paper 的确有相关讨论；
- 但这些讨论仍不足以支持题目中的更强 claim。

**Generation = pass** 只有在 answer 同时满足以下条件时成立：

- 明确说出 evidence **not sufficient**；
- 指出 paper 实际只支持较弱、条件性、或 setting-dependent 的结论；
- 不把 conditional finding 升级成 universal claim。

**Typical failure patterns**

- 把 partial evidence 升级成干净的 causal conclusion 或 universal claim；
- 忽略 limiting condition 或 exception；
- 明明 paper 支持较弱的 qualified answer，却直接 full abstain。

### D3 — External-only

**What it tests**  
测试 system 能否识别：题目问的是 **corpus boundary 之外** 的对象，例如新模型、production setting、或 unseen case。

**Retrieval = pass** 只有在 retrieved content 足以同时说明以下两点时成立：

- paper 中存在相关 internal evidence；
- 但这些 evidence 不能决定 external / unseen case 的答案。

**Generation = pass** 只有在 answer 同时满足以下条件时成立：

- 明确指出 **the paper alone is not enough**；
- 清楚指出需要 **external evidence / additional testing / deployment evidence**；
- 不从 paper 单独外推出 unseen case 的具体结论。

**Typical failure patterns**

- 用旧模型结果预测新模型；
- 把 prototyping evidence 升级成 production replacement claim；
- 只说“信息不够”，但没指出真正的 external-dependency boundary。

### D4 — False Premise

**What it tests**  
测试 system 能否先识别并纠正 **false premise**，再继续回答。

**Retrieval = pass** 只有在 retrieved content 足以同时说明以下两点时成立：

- question premise 被 paper 直接或实质性反驳；
- paper 支持纠正后的最小答案。

**Generation = pass** 只有在 answer 同时满足以下条件时成立：

- 先纠正 false premise；
- 再说 paper 实际支持什么；
- 不继续沿着错误 premise 回答。

**Typical failure patterns**

- 接受 false premise 后继续作答；
- 模糊 hedge，但没有真正纠正 premise；
- 选择性引用 evidence，使 false premise 看起来像真的。

---

## 9. D-class 跨类型关键错误 / Cross-cutting D-class Errors

以下错误在 D1–D4 中都应高优先级关注：

1. **Fabrication / unsupported completion**  
   把未报告内容补成具体 fact、number、prediction 或 conclusion。

2. **Boundary collapse**  
   把“related but insufficient”当成“already established”。

3. **Policy mismatch**  
   在 case 要求 abstain、qualify 或纠正 premise 时没有这么做。

4. **Evidence laundering**  
   把 nearby discussion（如 efficiency、scale、trend、conditional results、model size）洗成比 evidence 更强的答案。

---

## 10. 快速标注清单 / Quick Annotation Checklist

可将以下内容视为本文件的最短操作版。

- 先判断 **Retrieval**。
- 再判断 **Generation**。
- 选择一个主导性的 **Failure Bucket**。
- 仅对 boundary-oriented cases 使用 D-class 规则。
- 不要通过 plausible 但 unsupported 的答案。
- 如果没有 retrieve 到 key passage，不要因为 paper 对了就视为充分。
- 不要把 partial evidence 升级成更强结论。
- 不要在不纠正的情况下接受 false premise。
- 有疑问时，采用更保守的标签。

