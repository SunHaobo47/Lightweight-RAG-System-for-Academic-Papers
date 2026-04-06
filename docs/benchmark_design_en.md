# benchmark_design_en.md

## 1. Project Positioning

This benchmark evaluates the question-answering behavior of a lightweight RAG system on an academic-paper corpus. It focuses on four aspects:

- retrieving relevant evidence
- using evidence faithfully
- integrating information when needed
- handling answer boundaries correctly

The design is lightweight and interpretation-oriented, so retrieval, generation, and boundary handling can be observed separately. The evaluation emphasizes evidence sufficiency, evidence faithfulness, and answer boundary control, rather than whether an answer merely sounds plausible.

For result analysis, the design keeps two basic distinctions:

- **Retrieval**: whether the system retrieved the core evidence needed for a correct answer
- **Generation**: whether the system used sufficient evidence correctly and produced a constrained answer

In result logging, failures are grouped into a simplified taxonomy:

- **Retrieval failure**: retrieved evidence is insufficient, misses core parts, or is off-topic, so the correct answer cannot be derived from it
- **Generation failure**: evidence is sufficient, but the answer is still incorrect
- **None**: no clear failure is observed under the current passing threshold

---

## 2. Committed Benchmark Assets

The current submission mainly consists of two files.

### 2.1 Primary benchmark-definition workbook

**File**: `benchmarking_question.xlsx`

This is the main benchmark asset. It contains two core sheets:

- **Main-36**: the main evaluation set for scoring and result analysis
- **Paper Map**: a mapping table between corpus documents and their role in question design

`Main-36` is the core definition sheet. It defines each question so that it is:

- runnable
- gradable
- attributable
- reviewable

### 2.2 Evidence support workbook

**File**: `evidence_prep_draft.xlsx`

This file stores evidence support material, including:

- temporary core-evidence locations
- core-evidence text
- temporary supporting-evidence locations
- supporting-evidence text

It is an evidence support file, not the main benchmark definition file.

---

## 3. Main Benchmark Structure

`Main-36` currently contains **36 questions**, distributed as follows:

- **A**: 12
- **B**: 10
- **C**: 6
- **D**: 8
  - D1: 2
  - D2: 2
  - D3: 2
  - D4: 2

The set is centered on normal answerable questions, while retaining a grouped subset of D-type boundary cases for result interpretation.

### 3.1 A / B / C / D Question Taxonomy

#### Type A: Real-user questions

Purpose: to test practical usability under realistic user phrasing.

Focus:

- basic retrieval
- basic generation
- single-hop evidence use

#### Type B: Standard task questions

Purpose: to test structured task execution and stable cross-system comparison.

Focus:

- multi-span retrieval
- comparison and synthesis
- structured answer generation

#### Type C: Stress / robustness questions

Purpose: to test tolerance to less clean or less direct inputs.

Focus:

- semantic robustness
- retrieval elasticity
- generation robustness under vague queries

#### Type D: Refusal / boundary questions

Purpose: to test whether the system hallucinates or mishandles questions that should not be answered normally.

Type D contains four subtypes:

- **D1: No Evidence**: the corpus does not contain the key information asked by the user
- **D2: Insufficient Evidence**: the corpus discusses a related topic, but not enough to support a strong conclusion
- **D3: External-only**: the question requires knowledge outside the current corpus
- **D4: False Premise / Counterfactual**: the question is based on an incorrect premise or contradicts the source text

D1-D4 are separated because they affect refusal behavior, boundary handling, and hallucination analysis.

---

## 4. Main-36 Schema

The current `Main-36` sheet is a **main evaluation-set definition table** with the following columns:

- `QID`
- `Question`
- `Primary Type`
- `Source Doc IDs`
- `Target Answer Type`
- `Answerability`
- `Evidence Scope Note`
- `Reference Answer`
- `Minimum Acceptable Answer`
- `Critical Error`
- `Retrieval Pass Rule`
- `Generation Pass Rule`
- `Expected Response Policy`

### 4.1 Role of Each Field

- **QID**: unique question identifier
- **Question**: the final benchmark question given to the system
- **Primary Type**: A / B / C / D1 / D2 / D3 / D4
- **Source Doc IDs**: source-document identifiers corresponding to the `Paper Map`
- **Target Answer Type**: expected answer format. Supported types are:
  - `Explanatory`: explains a concept, cause, mechanism, effect, or phenomenon
  - `Comparative`: compares two or more objects, methods, viewpoints, or results
  - `Procedural`: describes steps, procedures, or operational sequence
  - `Mapping / Retrieval`: used for locating, mapping, classifying, or looking up items
  - `Diagnostic`: used for error analysis, failure-mode analysis, or diagnosis
  - `Non-answer / Correction`: used for refusal, qualified non-answer, or correction of a false premise
- **Answerability**: whether and how the question is answerable under the current corpus boundary
- **Evidence Scope Note**: brief note describing the evidence boundary
- **Reference Answer**: ideal answer within the current evidence boundary
- **Minimum Acceptable Answer**: minimum passing line for generation
- **Critical Error**: fatal error sufficient to trigger failure directly
- **Retrieval Pass Rule**: rule for judging retrieval success
- **Generation Pass Rule**: rule for judging generation success
- **Expected Response Policy**: expected response strategy. Supported types are:
  - `direct_answer`: answer the question directly
  - `abstain_missing_info`: abstain because key information is missing
  - `qualified_answer`: give a qualified answer under insufficient evidence or boundary constraints
  - `correct_false_premise`: point out and correct a false premise

### 4.2 Current Answerability and Response-policy Distribution

In the current `Main-36`:

- **Answerable**: 28
- **Insufficient**: 4
- **External-only**: 2
- **False-premise**: 2

The current `Expected Response Policy` distribution is:

- **direct_answer**: 28
- **abstain_missing_info**: 4
- **qualified_answer**: 2
- **correct_false_premise**: 2

This matches the design intention: most questions remain normally answerable, while a clearly defined boundary-handling subset is retained for testing refusal, insufficiency, external dependency, and premise correction.

### 4.3 Answerability Framework

The benchmark uses four answerability labels:

- **Answerable**
- **Insufficient**
- **External-only**
- **False-premise**

These labels define what counts as a correct response under the current corpus boundary and complement the main ABCD question taxonomy.

Their roles include:

- determining whether the system should answer directly
- helping identify whether a failure belongs to boundary handling
- distinguishing different kinds of non-standard answer conditions within Type D

In the current design, answerability is treated as a predefined analysis dimension. Together with ABCD, simplified failure type, and core evidence support, it provides an initial structure for later result analysis.

---

## 5. Paper Map Schema

The current `Paper Map` sheet is a **corpus-role and question-design mapping table** with the following columns:

- `Doc ID`
- `File Name`
- `Year`
- `Paper Role`
- `Best Use for Question Design`

Purpose:

to indicate the role each source paper plays in the corpus and the kind of question design it is best suited to support.

---

## 6. Evidence Design

In this benchmark, evidence is not the final score itself. It serves as the evidential basis of the grading chain.

It defines:

- how far the current corpus can support a claim
- what kinds of answers remain within the supported boundary
- what retrieval and generation judgments should be anchored to

The intended grading chain is:

**question definition -> evidence boundary -> pass rule / rubric -> answer-level grading**

Within this chain:

- **Core Evidence**: the minimum set of evidence required to support a correct answer
- **Supporting Evidence**: helpful but non-essential supplementary evidence

### 6.1 Definition and Role of Core Evidence

Core Evidence is not the most complete evidence set, and it is not all relevant content.

Its definition is:

> **If this evidence is missing, the system should not be judged retrieval-sufficient; if this evidence has been retrieved, the correct answer should in principle be derivable from the available evidence.**

Accordingly, Core Evidence serves to:

- define the minimum passing line for retrieval sufficiency
- support retrieval-vs-generation failure attribution
- constrain the support boundary of the Reference Answer and Minimum Acceptable Answer
- support abstention, qualified answer, and premise-correction judgments in Type D questions

### 6.2 Definition and Role of Supporting Evidence

Supporting Evidence refers to evidence that is relevant to the question and helps supplement context, reduce ambiguity, improve completeness, or support boundary judgment, but does not usually determine whether the question is already answerable.

Supporting Evidence can be used to:

- supplement comparisons, constraints, or background information
- support more complete and more robust generation
- help judge whether a claim is overreaching
- support finer-grained human review

---

## 7. Current Status and Limitations

In the current version, the evidence layer is treated as **weakly grounded**.

That means:

- `Main-36` already contains the core grading elements, including question definition, answerability, response policy, reference answer, minimum acceptable answer, critical error, and pass rules
- the current evidence layer has not yet been fully refined on a question-by-question basis; at this stage, grounded evidence is mainly organized with the assistance of advanced LLMs, with human checking used as a supplement
- the questions, evidence, and answers that have undergone manual review include: ID 1, 2, 13, 20, and 29-36

At its current stage, the benchmark can be used for:

- small-scale system comparison
- preliminary error-pattern analysis
- preliminary retrieval / generation attribution analysis
- exploratory result analysis

---

