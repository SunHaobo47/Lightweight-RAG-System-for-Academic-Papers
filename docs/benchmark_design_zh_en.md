# benchmark_design_zh_en.md

## 1. 项目定位 (Project Positioning)

这套 benchmark 用于评估一个 lightweight RAG system 在 academic-paper corpus 上的问答表现，关注以下四个方面：

- 检索相关证据 (retrieve relevant evidence)
- 忠实使用证据 (use evidence faithfully)
- 在需要时做信息整合 (integrate information when needed)
- 正确处理回答边界 (handle answer boundaries correctly)

它采用轻量级、解释导向的设计，使 retrieval、generation 与 boundary handling 可以被分开观察。评测重点是 evidence sufficiency、evidence faithfulness 与 answer boundary control，而不是答案是否“听起来合理”。

为支持结果分析，这套设计保留两层基本区分：

- **Retrieval**：系统是否找回了足以支撑正确回答的核心证据
- **Generation**：在证据已经足够时，系统是否正确使用这些证据并生成受约束的回答

在结果记录中，失败统一收束为一个简化 taxonomy：

- **Retrieval failure**：检回证据不足、缺核心部分或偏题，因此正确答案在当前检回内容上不可导出
- **Generation failure**：证据已经足够，但答案仍然错误
- **None**：在当前通过线 (passing threshold) 下，没有明显 failure

---

## 2. 已提交 Assets 的功能 (Committed Benchmark Assets)

当前提交的内容主要由两个文件构成。

### 2.1 主定义工作簿 (Primary benchmark-definition workbook)

**文件**：`benchmarking_question.xlsx`

这是主 benchmark 资产，核心围绕两张表：

- **Main-36**：正式跑分与结果分析使用的主评测集
- **Paper Map**：语料文档与出题用途之间的映射表

其中 `Main-36` 是真正的核心定义表，负责定义每道题，使其达到：

- 可运行 (runnable)
- 可评分 (gradable)
- 可归因 (attributable)
- 可复核 (reviewable)

### 2.2 证据支持工作簿 (Evidence support workbook)

**文件**：`evidence_prep_draft.xlsx`

这是 evidence 支持文件，主要存放：

- core evidence 的临时位置 (temporary core-evidence locations)
- core evidence 文本 (core-evidence text)
- supporting evidence 的临时位置
- supporting evidence 文本

它是证据支持文件，而不是主 benchmark 定义文件。

---

## 3. 主评测集结构 (Main Benchmark Structure)

当前 `Main-36` 共 **36 题**，配比如下：

- **A**：12
- **B**：10
- **C**：6
- **D**：8
  - D1：2
  - D2：2
  - D3：2
  - D4：2

主体仍是可正常作答的主场景题，同时保留成组的 D 类边界题以支撑结果解释。

### 3.1 A / B / C / D 题型框架 (Question Taxonomy)

#### A 类：真实用户题 (Real-user questions)

目的：测试真实问法下的实际可用性。\
重点：

- 基本检索 (basic retrieval)
- 基本生成 (basic generation)
- 单跳证据使用 (single-hop evidence use)

#### B 类：标准任务题 (Standard task questions)

目的：测试结构化任务执行能力与跨系统稳定比较。\
重点：

- 多片段检索 (multi-span retrieval)
- 比较与整合 (comparison and synthesis)
- 结构化回答 (structured answer generation)

#### C 类：压力 / 鲁棒性题 (Stress / robustness questions)

目的：测试系统对较不整洁输入的承受能力。\
重点：

- 语义鲁棒性 (semantic robustness)
- retrieval elasticity
- 模糊查询下的 generation 稳健性

#### D 类：拒答 / 边界题 (Refusal / boundary questions)

目的：测试系统会不会乱编 (hallucinate) 或错误处理不可正常回答的情况。

D 类保留四个子类：

- **D1: No Evidence**：文档中根本没有用户所问的关键信息
- **D2: Insufficient Evidence**：文档涉及相关主题，但不足以下强结论
- **D3: External-only**：问题需要当前语料外的外部知识
- **D4: False Premise / Counterfactual**：问题前提与原文不符，或建立在错误假设上

D1–D4 单独划分，因为它影响 refusal、boundary handling 与 hallucination analysis。

---

## 4. Main-36 的 schema 设计 (Main-36 Schema)

当前提交版 `Main-36` 被定义为一张 **主评测集定义表** (main evaluation-set definition table)，当前列如下：

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

### 4.1 各字段作用 (Role of Each Field)

- **QID**：题目唯一编号
- **Question**：最终喂给系统的 benchmark question
- **Primary Type**：A / B / C / D1 / D2 / D3 / D4
- **Source Doc IDs**：对应 `Paper Map` 中的 source-document 编号
- **Target Answer Type**：期待的回答方式。当前支持的类型包括：
  - `Explanatory`：说明概念、原因、机制、影响或现象
  - `Comparative`：比较两个或多项对象、方法、观点或结果
  - `Procedural`：描述步骤、流程或操作顺序
  - `Mapping / Retrieval`：用于定位、映射、归类或表项查找
  - `Diagnostic`：用于错误分析、失效模式分析或问题诊断
  - `Non-answer / Correction`：用于拒答、保留判断或纠正错误前提
- **Answerability**：该题在当前语料下是否可答、如何可答
- **Evidence Scope Note**：简短说明证据边界 (evidence boundary)
- **Reference Answer**：在当前证据边界内的理想参考答案
- **Minimum Acceptable Answer**：generation 的最低通过线
- **Critical Error**：足以直接判失败的致命错误
- **Retrieval Pass Rule**：检索何时算通过
- **Generation Pass Rule**：生成何时算通过
- **Expected Response Policy**：期望的响应策略。当前支持的类型包括：
  - `direct_answer`：直接回答问题
  - `abstain_missing_info`：因关键信息缺失而拒答
  - `qualified_answer`：在证据不足或边界受限时给出保留式回答
  - `correct_false_premise`：指出并纠正错误前提

### 4.2 当前 answerability 与 response-policy 分布

当前 `Main-36` 中：

- **Answerable**：28
- **Insufficient**：4
- **External-only**：2
- **False-premise**：2

当前 `Expected Response Policy` 分布为：

- **direct\_answer**：28
- **abstain\_missing\_info**：4
- **qualified\_answer**：2
- **correct\_false\_premise**：2

这个分布符合设计意图：大多数题仍是普通可答题，同时保留一个明确的边界处理子集，用于测试 refusal、insufficiency、external dependency 与 premise correction。

### 4.3 Answerability 框架 (Answerability Framework)

本 benchmark 统一使用四个 answerability 标签：

- **Answerable**
- **Insufficient**
- **External-only**
- **False-premise**

它们定义了在当前语料边界下，什么样的回答才算正确，并作为题目主分类 ABCD 的补充。

其作用包括：

- 决定系统是否应直接作答
- 帮助识别 failure 是否属于 boundary handling
- 区分 D 类内部不同类型的不可正常回答情形

在当前设计中，answerability 被作为一个预设分析维度，与 ABCD、simplified failure type 和 core evidence support 一起，为后续结果分析提供一个初步结构。

---

## 5. Paper Map 的 schema 设计 (Paper Map Schema)

当前提交版 `Paper Map` 被定义为一张 **语料角色与出题用途映射表** (corpus-role and question-design mapping table)，列如下：

- `Doc ID`
- `File Name`
- `Year`
- `Paper Role`
- `Best Use for Question Design`

目的：\
标注每篇 source paper 在语料里扮演什么角色，以及它最适合支撑什么类型的问题设计。

---

## 6. Evidence 设计 (Evidence Design)

在这套 benchmark 中，evidence 不是最终分数本身，而是判分链条中的证据基础 (evidential basis)。\
它定义的是：

- 当前语料最多支持到哪里
- 什么样的回答仍在支持边界内
- retrieval / generation 判断应锚定在什么基础上

理想的判分链条是：

**question definition → evidence boundary → pass rule / rubric → answer-level grading**

在这个链条中：

- **Core Evidence**：支撑正确回答所必需的最小核心证据集合\
  (minimum core evidence required for a correct answer)
- **Supporting Evidence**：有帮助但非必需的补充证据\
  (helpful but non-essential evidence)

### 6.1 Core Evidence 的定义与作用

Core Evidence 不等于“最完整的证据集合”，也不等于“所有相关内容”。\
它的定义是：

> **如果缺少这部分证据，系统不应被判定为 retrieval sufficient；如果这部分证据已经被检回，则正确答案在原则上应可从当前证据中导出。**

因此，Core Evidence 的功能是：

- 定义 retrieval sufficiency 的最低通过线
- 为 retrieval vs generation failure attribution 提供依据
- 约束 Reference Answer / Minimum Acceptable Answer 的支持边界
- 支撑 D 类题中的 abstention / qualified answer / premise correction 判断

### 6.2 Supporting Evidence 的定义与作用

Supporting Evidence 指与问题相关、能补充上下文、去歧义、增强回答完整性或支撑边界判断的证据，但它本身通常不决定“该题是否已经可答”。

Supporting Evidence 可用于：

- 补充比较、限制条件或背景信息
- 支撑更完整、更稳健的生成
- 帮助判断哪些说法属于 overclaiming
- 支撑更细粒度的人工复核

---

## 7. Current Status and Limitations

当前版本中，evidence 被视为 **weakly grounded**。

即：

- `Main-36` 已具备题目定义、answerability、response policy、reference answer、minimum acceptable answer、critical error 和 pass rule 等核心判分要素
- 当前 evidence 体系尚未完成逐题精修；现阶段的 grounded evidence 主要由高级 LLM 辅助整理，并以人工校核作为补充
- 已完成人工复查的题目、evidence 与 answer 包括：ID 1、2、13、20、29–36

已可用于：

- 小规模系统比较
- 初步错误模式分析
- 初步的 retrieval / generation 归因分析
- exploratory result analysis
