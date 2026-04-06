# Companion Rationale for `evaluation_rubric.md`

This document is the companion rationale for `evaluation_rubric.md`.

It explains the design logic behind the benchmark’s evaluation and annotation rules. It is not the primary reviewer-facing rubric.

Specifically, it explains:

- why the benchmark is evaluated through an evidence path rather than answer plausibility;
- why Retrieval and Generation are separated as different failure sources;
- why D-class cases use a different evaluation logic from standard A/B/C cases.

The goal is to preserve the reasoning behind the rubric design so future contributors can understand, maintain, and extend the evaluation framework consistently.

---

## 1. Why this benchmark is evidence-grounded

This benchmark evaluates RAG outputs by the **evidence path**, not by whether the final answer merely sounds correct.

The key question is not just:

> Is the answer plausible?

It is:

> Did the system retrieve the right evidence, and did it use that evidence correctly?

This matters because a RAG system can fail in two main ways:

- **Retrieval failure**: the system did not retrieve the evidence the case requires;
- **Generation failure**: the evidence was sufficient, but the answer was still wrong, overextended, hallucinated, or violated the expected response policy.

Because of this, the benchmark does not treat a plausible answer as sufficient. It rewards evidence-grounded behavior rather than lucky guessing.

---

## 2. Why the benchmark uses a benchmark-grounded standard

The rubric follows a **benchmark-grounded** standard rather than a user-impression standard.

A response should pass only when all of the following are true:

- the retrieved content matches the intended evidence target;
- the answer satisfies the case-specific pass rule;
- the answer is supported by retrieved evidence rather than plausible guessing.

This means:

- a plausible answer without the required evidence is still a **fail**;
- retrieving the correct paper without the key passage is still a **Retrieval failure**;
- for comparison or integration questions, retrieving only one side is still a **Retrieval failure**.

The goal is to measure whether the system followed the intended evidence path, not whether it produced a believable answer.

---

## 3. Why Retrieval and Generation are scored separately

The rubric separates **Retrieval** and **Generation** because they reflect different bottlenecks in a RAG pipeline.

### Retrieval

Retrieval asks whether the system found the correct evidence source and whether that evidence was sufficient for the intended answer.

A case should fail Retrieval when, for example:

- the source is wrong;
- the source is relevant but the key passage is missing;
- the retrieved evidence is too generic;
- a multi-source question retrieves only part of what is needed;
- the retrieved evidence is related but still insufficient.

### Generation

Generation asks whether the answer was faithful to the retrieved evidence and whether it followed the expected response policy.

A case should fail Generation when, for example:

- the answer is only weakly grounded;
- the answer overclaims beyond what the evidence supports;
- the answer hallucinates missing details;
- the case requires a specific mechanism or logic chain but the answer remains generic;
- the case is answerable, but the system gives an improper abstention.

Scoring these dimensions separately makes the annotation more diagnostic. It helps distinguish missing evidence from misuse of available evidence.

---

## 4. Why Failure Bucket records a dominant cause

The rubric includes `Failure Bucket` to record the **primary cause** of the final failure.

The intended logic is:

- if the core problem is missing or insufficient evidence, assign **Retrieval failure**;
- if the evidence is sufficient but the answer is still wrong or policy-incompatible, assign **Generation failure**;
- if the case fully passes, assign `None`.

The rubric defaults to a single **dominant cause** because the benchmark is meant to support interpretable error analysis. Mixed labels should be rare.

This design encourages reviewers to ask not just whether the answer failed, but where the main failure occurred.

---

## 5. Why the policy is binary pass/fail

The benchmark uses binary pass/fail for both Retrieval and Generation.

This is deliberate. The goal is not to reward answers for being “almost correct” or “partially reasonable,” but to maintain annotation consistency and sharp failure attribution.

Under this policy:

- if the final answer does not satisfy the generation rule, `Generation = fail`;
- reviewers should not assign partial credit for vague or nearly correct outputs;
- except for special cases, reviewers should still judge Generation even if Retrieval failed.

The binary policy keeps the rubric easier to apply and makes downstream analysis cleaner.

---

## 6. Why the review workflow is ordered

The recommended workflow is:

1. judge Retrieval;
2. judge Generation;
3. assign Failure Bucket.

This mirrors the causal structure of a RAG system:

- first ask whether the required evidence is present;
- then ask whether the answer used that evidence correctly;
- finally identify the dominant failure source.

This ordering helps reduce annotation drift by keeping reviewers on the same decision path.

---

## 7. Why borderline cases are judged conservatively

The rubric explicitly calls out several borderline patterns and recommends a conservative standard.

### Correct paper, wrong passage

The correct paper is not enough if the defining evidence was never actually retrieved. This is still a Retrieval failure.

### Plausible but weakly grounded answer

A believable answer should not pass if the evidence support is weak or missing. Otherwise, the benchmark would reward plausible guessing.

### Generic answer to a mechanism question

If a case was designed to test a specific mechanism or logic chain, then a broad high-level answer is not enough.

These conservative rules help preserve what the benchmark is actually trying to measure.

---

## 8. Why D-class needs a different evaluation logic

D-class is not a standard content-recall category. It is designed to test **boundary handling**.

The key abilities under evaluation are:

- **boundary recognition**;
- **response-policy compliance**;
- **anti-hallucination discipline**;
- **evidence-limited reasoning**.

Because of this, the key question for D-class is not:

> Did the answer say something useful?

Instead, it is:

> Did the system recognize the boundary correctly and respond in the right way?

This leads to a different success pattern from standard A/B/C cases:

- D1 and D3 often succeed through **correct abstention**;
- D2 often succeeds through a **qualified answer**;
- D4 often succeeds through **premise correction**.

D-class is not mainly about factual recall. It is about whether the system behaves correctly when the evidence boundary matters.

---

## 9. Why D-class still uses Retrieval and Generation

Although D-class cases are boundary-oriented, the same Retrieval / Generation split still matters.

For D-class, Retrieval is often not about finding a direct fact answer. Instead, it is about finding **boundary evidence**.

Typical boundary evidence shows that:

- the paper does **not** report the requested information;
- the paper supports only a weaker conclusion;
- the question requires external evidence beyond the corpus;
- the premise of the question is false.

Generation then asks whether the system used that boundary evidence correctly:

- Did it abstain when abstention was required?
- Did it qualify the answer rather than overstate it?
- Did it explicitly mark external dependency?
- Did it correct a false premise before continuing?

This is why D-class still fits the overall rubric structure, even though its evaluation target differs from ordinary recall cases.

---

## 10. Why D-class is split into D1–D4

The D-class subtypes separate different kinds of boundary behavior.

### D1 — No Evidence

The paper discusses a nearby topic but does not report the requested fact.

The key failure mode is unsupported completion: inventing the missing value or laundering nearby discussion into a concrete answer.

### D2 — Insufficient Evidence

The paper contains relevant discussion, but not enough to support the stronger claim in the question.

The key failure mode is upgrading partial evidence into a stronger or more universal conclusion than the paper supports.

### D3 — External-only

The question targets something outside the corpus boundary, such as a new model, a current production setting, or an unseen case.

The key failure mode is extrapolating beyond the paper without identifying the need for external evidence.

### D4 — False Premise

The question contains a false premise.

The key failure mode is accepting that premise and answering under it instead of correcting it first.

These distinctions matter because different boundary failures require different response policies.

---

## 11. Why cross-cutting D-class errors are highlighted

The rubric explicitly highlights four high-priority D-class errors because they recur across multiple boundary types:

1. **Fabrication / unsupported completion**  
   Filling in unreported content as a concrete fact, number, prediction, or conclusion.

2. **Boundary collapse**  
   Treating “related but insufficient” as if it were already established.

3. **Policy mismatch**  
   Failing to abstain, qualify, or correct the premise when the case requires it.

4. **Evidence laundering**  
   Turning nearby discussion—such as efficiency, scale, trends, conditional results, or model size—into a stronger answer than the evidence supports.

These categories improve reviewer consistency and make D-class failures easier to interpret.

---

## 12. Minimal operational interpretation

At the most compressed level, the rubric follows the logic below.

### Standard A/B/C cases

- **Pass** = correct evidence path + faithful answer
- **Fail** = wrong source / insufficient evidence / ungrounded answer / overclaim

### D1

- **Pass** = clearly states that the paper does not report the information
- **Fail** = invents or infers the missing value

### D2

- **Pass** = clearly states that the evidence is insufficient for the stronger claim and gives the weaker supported claim
- **Fail** = uses partial evidence to support the stronger claim

### D3

- **Pass** = clearly states that the paper alone is not enough and that external evidence is needed
- **Fail** = extrapolates beyond the paper to an unseen case

### D4

- **Pass** = corrects the false premise before answering
- **Fail** = accepts the premise or fails to correct it clearly

---

## 13. Why Reason Note matters

A good `Reason Note` should minimally explain:

1. the **evidence status**;
2. whether the expected **response policy** was followed.

A simple template is:

> The retrieved evidence is sufficient / insufficient to support the required judgment. The answer does / does not follow the expected response policy, because ...

For D-class, the `Reason Note` should ideally name the boundary type explicitly, such as:

- missing information
- insufficient evidence for a strong claim
- external-only case
- false premise

This improves reviewer transparency and makes later audits easier.

