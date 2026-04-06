# Evaluation / Annotation Rules

This document defines how reviewers should annotate benchmark outputs.

It is designed for:

- consistent scoring;
- a simple review workflow.

The benchmark is **evidence-grounded**. Judge whether the system retrieved the required evidence and used it correctly, not whether the answer merely sounds plausible.

---

## 1. Scope

Use this document to assign:

- `Retrieval`
- `Generation`
- `Failure Bucket`

Use the D-class rules only for boundary-oriented cases, such as missing-evidence, insufficient-evidence, external-only, or false-premise questions.

---

## 2. Quick Review Flow

Review each case in this order:

1. Judge **Retrieval**.
2. Judge **Generation**.
3. Assign one dominant **Failure Bucket**.
4. If needed, apply the D-class rules in Sections 7–8.

Core policy:

- Do not pass an answer just because it sounds reasonable.
- Do not treat the correct paper as sufficient if the defining passage was not retrieved.
- Do not skip the Generation judgment just because Retrieval failed, unless a special case explicitly requires it.

---

## 3. Core Labels

### 3.1 Retrieval

Mark **Retrieval = pass** only when all are true:

1. The system retrieved the correct **document / evidence direction**.
2. The retrieved chunks satisfy the case-specific **Retrieval Pass Rule**.
3. The retrieved evidence is **sufficient** for the intended answer.

Mark **Retrieval = fail** when any of the following applies:

- wrong source;
- right source but missing key passage;
- evidence is related but too generic;
- a comparison / integration question retrieves only one side;
- retrieved content is related but still insufficient for the intended answer.

### 3.2 Generation

Mark **Generation = pass** only when all are true:

1. The answer satisfies the case-specific **Generation Pass Rule**.
2. The answer reaches the **Minimum Acceptable Answer**.
3. The answer is supported by retrieved evidence.

Mark **Generation = fail** when any of the following applies:

- the answer is broadly plausible but weakly grounded;
- the answer overclaims beyond what the evidence supports;
- the answer hallucinates missing details;
- the case requires a specific mechanism or logic chain but the answer stays generic;
- the benchmark expects an answerable response but the system gives an improper abstention.

### 3.3 Failure Bucket

`Failure Bucket` records the **primary cause** of the final failure.

Use:

- missing or insufficient evidence → `Retrieval failure`
- enough evidence, but wrong answer / overclaim / policy error → `Generation failure`
- full pass → `None`

Use one dominant cause by default. Use a mixed label only when truly necessary.

### 3.4 Binary Policy

This benchmark uses binary pass/fail for Retrieval and Generation.

- Do not give partial credit for “almost correct” answers.
- If the final answer does not meet the generation rule, mark `Generation = fail`.
- Except for special cases, do not skip Generation just because Retrieval failed.

---

## 4. Review Workflow

### Step 1 — Judge Retrieval

Ask:

> Does the retrieved content satisfy this case’s retrieval requirement?

If not, mark `Retrieval = fail`.

### Step 2 — Judge Generation

Ask:

> Given the retrieved content, does the answer satisfy the Minimum Acceptable Answer and the Generation Pass Rule?

If not, mark `Generation = fail`.

### Step 3 — Assign Failure Bucket

Ask:

> What is the main bottleneck in the final result?

Use:

- `Retrieval failure` for missing / insufficient evidence;
- `Generation failure` for wrong answer / overclaim / wrong response policy despite sufficient evidence.

---

## 5. Borderline Cases

Apply a conservative standard in these cases.

### A. Correct paper, wrong passage

Do **not** pass Retrieval if the paper is correct but the defining evidence was not actually retrieved.

### B. Plausible but weakly grounded answer

Do **not** pass Generation if the answer sounds reasonable but is not adequately supported by retrieved evidence.

### C. Generic answer to a specific mechanism question

Do **not** pass Generation if the case targets a specific mechanism / logic chain and the answer stays at a broad high level.

---

## 6. Evidence-Grounded Principle

Use a **benchmark-grounded** standard, not a user-impression standard.

A response passes only when:

- the retrieved content hits the intended evidence target;
- the answer satisfies the case-specific pass rule;
- the answer is supported by retrieved evidence rather than plausible guessing.

Implications:

- a plausible answer without the required evidence is still a **fail**;
- retrieving the correct paper without the key passage is still a **Retrieval failure**;
- comparison / integration questions still fail Retrieval if only one side is retrieved.

---

## 7. D-class Overview

D-class cases evaluate **boundary handling**, not standard content recall.

Judge:

- boundary recognition;
- response-policy compliance;
- anti-hallucination discipline;
- evidence-limited reasoning.

The key question is whether the system recognized the boundary correctly and responded in the right way.

Typical success patterns:

- D1 / D3 often require **correct abstention**;
- D2 often requires a **qualified answer**;
- D4 often requires **premise correction**.

### 7.1 General Rule for D-class

For every D-class case, review in this order:

1. Did the system identify the correct **boundary type**?
2. Does Retrieval support that boundary judgment?
3. Does Generation follow the correct **response policy**?
4. Does the answer avoid overclaim, unsupported extrapolation, or incorrect premise acceptance?

In D-class cases, Retrieval often targets **boundary evidence** rather than a direct fact answer.

Common boundary evidence includes evidence showing that:

- the paper **does not report** the requested information;
- the paper supports only a **weaker conclusion**;
- the question requires **external evidence** beyond the corpus;
- the question’s **premise is false**.

---

## 8. D-class Subtypes

### D1 — No Evidence

**What it tests**  
Whether the system can recognize that the paper discusses a nearby topic but does **not** report the requested fact.

**Retrieval = pass** only when the retrieved content is enough to show both:

- the paper does discuss the nearby topic;
- the requested fact was not actually reported.

**Generation = pass** only when the answer does all of the following:

- explicitly states that the paper **does not report** the information;
- does not invent runtime / cost / latency / dollar figures or other missing values;
- may mention what the paper does discuss, but does not convert nearby details into the missing answer.

**Typical failure patterns**

- inventing runtime / dollar cost / API price;
- turning nearby efficiency / workflow details into a concrete answer;
- saying “not reported” without the right boundary evidence.

### D2 — Insufficient Evidence

**What it tests**  
Whether the system can distinguish **related evidence** from **sufficient evidence for a stronger claim**.

**Retrieval = pass** only when the retrieved content is enough to show both:

- the paper contains relevant discussion;
- that discussion is still insufficient for the stronger claim in the question.

**Generation = pass** only when the answer does all of the following:

- explicitly states that the evidence is **not sufficient**;
- identifies the weaker, conditional, or setting-dependent conclusion that the paper actually supports;
- does not upgrade a conditional finding into a universal claim.

**Typical failure patterns**

- upgrading partial evidence into a clean causal or universal conclusion;
- ignoring limiting conditions or exceptions;
- giving a full abstention when the paper actually supports a weaker qualified answer.

### D3 — External-only

**What it tests**  
Whether the system can recognize that the question targets something **outside the corpus boundary**, such as a new model, a production setting, or an unseen case.

**Retrieval = pass** only when the retrieved content is enough to show both:

- the paper contains relevant internal evidence;
- that evidence cannot determine the answer for the external / unseen case.

**Generation = pass** only when the answer does all of the following:

- explicitly states that **the paper alone is not enough**;
- identifies the need for **external evidence / additional testing / deployment evidence**;
- does not extrapolate a concrete conclusion for the unseen case from the paper alone.

**Typical failure patterns**

- using old-model results to predict a new model;
- upgrading prototyping evidence into a production-replacement claim;
- saying only “not enough information” without identifying the real external-dependency boundary.

### D4 — False Premise

**What it tests**  
Whether the system can identify and correct a **false premise** before continuing the answer.

**Retrieval = pass** only when the retrieved content is enough to show both:

- the question premise is directly or materially contradicted by the paper;
- the paper supports the corrected minimal answer.

**Generation = pass** only when the answer does all of the following:

- corrects the false premise first;
- then states what the paper actually supports;
- does not continue answering under the false premise.

**Typical failure patterns**

- accepting the false premise and continuing the answer;
- hedging without actually correcting the premise;
- selectively citing evidence in a way that makes the false premise look true.

---

## 9. Cross-cutting D-class Errors

Treat these as high-priority errors across D1–D4:

1. **Fabrication / unsupported completion**  
   Filling in unreported content as a specific fact, number, prediction, or conclusion.

2. **Boundary collapse**  
   Treating “related but insufficient” as “already established”.

3. **Policy mismatch**  
   Failing to abstain, qualify, or correct the premise when the case requires it.

4. **Evidence laundering**  
   Turning nearby discussion (for example, efficiency, scale, trend, conditional results, or model size) into a stronger answer than the evidence supports.

---

## 10. Quick Annotation Checklist

Use this as the shortest operational version of the document.

- Judge **Retrieval** first.
- Judge **Generation** second.
- Assign one dominant **Failure Bucket**.
- Apply D-class rules only to boundary-oriented cases.
- Do not pass plausible but unsupported answers.
- Do not treat the correct paper as sufficient if the key passage was not retrieved.
- Do not upgrade partial evidence into a stronger conclusion.
- Do not accept a false premise without correction.
- When in doubt, use the more conservative label.

