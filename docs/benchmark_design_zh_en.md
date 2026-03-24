# benchmark_design.md

## 1. 项目定位 (Project Positioning)

这套 benchmark 的目标，是评估一个 lightweight RAG system 在 academic-paper corpus 上，能否完成以下几个核心环节：

- 检索相关证据 (retrieve relevant evidence)
- 忠实使用证据 (use evidence faithfully)
- 在需要时做信息整合 (integrate information when needed)
- 正确处理回答边界 (handle answer boundaries correctly)

它是一套 轻量级、解释导向、资源受限条件下的诊断型评测设计 (lightweight, interpretable, resource-constrained diagnostic evaluation)。

这套设计始终保留两层核心解释力：

- **Retrieval**：系统有没有找回足以支撑正确回答的关键证据
- **Generation**：在证据已经足够时，系统有没有正确使用这些证据并生成受约束的回答

在主结果 (main reporting) 中，失败统一收束为一个简化 taxonomy：

- **Retrieval failure**：检回证据不足、缺关键部分或偏题，因此正确答案在当前检回内容上不可导出
- **Generation failure**：证据已经足够，但答案仍然错误
- **None**：在当前通过线 (passing threshold) 下，没有明显 failure


## 2. 已提交Assets的功能 (Committed Benchmark Assets)

当前要提交的 benchmark package 可以分成两个角色。

### 2.1 主定义工作簿 (Primary benchmark-definition workbook)

**文件**：`benchmarking_question.xlsx`

这是主 benchmark 资产，核心围绕两张表：

- **Main-36**：正式跑分与结果分析使用的主评测集
- **Paper Map**：语料文档与出题用途之间的映射表

其中 `Main-36` 是真正的 operational core，负责定义每道题，使其达到：

- 可运行 (runnable)
- 可评分 (gradable)
- 可归因 (attributable)
- 可复核 (reviewable)

### 2.2 证据支持工作簿 (Evidence support workbook)

**文件**：`evidence_prep_draft.xlsx`

这是 evidence 支持文件，主要存放：

- gold evidence 的临时位置 (temporary gold-evidence locations)
- gold evidence 文本 (gold-evidence text)
- supporting evidence 的临时位置
- supporting evidence 文本

它是 supporting file，而不是 headline benchmark-definition file。

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
目的：测试真实问法下的 practical usability。  
重点：
- 基本检索 (basic retrieval)
- 基本生成 (basic generation)
- 单跳证据使用 (single-hop evidence use)

#### B 类：标准任务题 (Standard task questions)
目的：测试 structured task execution 与跨系统稳定比较。  
重点：
- 多片段检索 (multi-span retrieval)
- 比较与整合 (comparison and synthesis)
- 结构化回答 (structured answer generation)

#### C 类：压力 / 鲁棒性题 (Stress / robustness questions)
目的：测试系统对较不整洁输入的承受能力。  
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
- `RAGAS Eval Profile`

### 4.1 各字段作用 (Role of Each Field)

- **QID**：题目唯一编号
- **Question**：最终喂给系统的 benchmark question
- **Primary Type**：A / B / C / D1 / D2 / D3 / D4
- **Source Doc IDs**：对应 `Paper Map` 中的 source-document 编号
- **Target Answer Type**：期待的回答方式，例如 explanation、comparison、abstention、premise correction
- **Answerability**：该题在当前语料下是否可答、如何可答
- **Evidence Scope Note**：简短说明证据边界 (evidence boundary)
- **Reference Answer**：在当前证据边界内的理想参考答案
- **Minimum Acceptable Answer**：generation 的最低通过线
- **Critical Error**：足以直接判失败的致命错误
- **Retrieval Pass Rule**：检索何时算通过
- **Generation Pass Rule**：生成何时算通过
- **Expected Response Policy**：期望的响应策略，如 direct answer、abstain、qualified answer、correct false premise
- **RAGAS Eval Profile**：后续 judge / export 用的轻量评测配置标签

### 4.2 当前 answerability 与 response-policy 分布

当前 `Main-36` 中：

- **Answerable**：28
- **Insufficient**：4
- **External-only**：2
- **False-premise**：2

当前 `Expected Response Policy` 分布为：

- **direct_answer**：28
- **abstain_missing_info**：4
- **qualified_answer**：2
- **correct_false_premise**：2

这个分布符合设计意图：  
大多数题仍是普通可答题 (normal answerable tasks)，但同时保留一个明确的边界处理子集，用于测试 refusal、insufficiency、external dependency 与 premise correction。

## 5. Paper Map 的 schema 设计 (Paper Map Schema)

当前提交版 `Paper Map` 被定义为一张 **语料角色与出题用途映射表** (corpus-role and question-design mapping table)，列如下：

- `Doc ID`
- `File Name`
- `Year`
- `Paper Role`
- `Best Use for Question Design`

这张表的目的是回答：  
**每篇 source paper 在语料里扮演什么角色，以及它最适合支撑什么类型的问题设计。**

## 6. Answerability 框架 (Answerability Framework)

本 benchmark 统一使用四个 answerability 标签：

- **Answerable**
- **Insufficient**
- **External-only**
- **False-premise**

它们定义“什么样的回答才算正确”的框架。作为题目主分类ABCD的补充。

其作用包括：

- 决定系统是否应直接作答
- 帮助识别 failure 是否属于 boundary handling
- 区分 D 类内部不同类型的不可正常回答情形

在当前设计中，answerability 被视为四条主分析轴之一，与：

- ABCD
- simplified failure type
- gold evidence support

并列。

## 7. Evidence 设计与当前 evidence 状态 (Evidence Design and Status)

在这套 benchmark 中，evidence 不是最终分数本身，而是判分链条中的证据基础 (evidential basis)。  
它定义的是：

- 当前语料最多支持到哪里
- 什么样的回答仍在支持边界内
- retrieval / generation 判断应锚定在什么基础上

理想的判分链条是：

**question definition → evidence boundary → pass rule / rubric → answer-level grading**

在这个链条中：

- **Gold Evidence**：最小可裁判依据 (minimum judgeable support)
- **Supporting Evidence**：上下文补充、边界补充、去歧义、支撑 abstention / correction

### 7.1 当前项目中 evidence 的性质

结合当前工作流，项目中的 evidence 更准确地应描述为：

**weakly grounded but source-anchored evidence**

即：

- 语料是真实的 (real corpus)
- evidence 锚定真实 source
- evidence 的抽取、压缩、改写、整理有 LLM assistance
- 边界经过检查（boundary checking was LLM-assisted）
- 但尚未达到 fully human-verified benchmark-grade evidence 的强度（其中问题ID 1，2，13，20，35的 evidence-related fields 与 answer-related fields 经过人工检查并通过）

因此，这批 evidence 适合支撑：

- 相对比较 (relative comparison)
- 趋势观察 (trend observation)
- 题级判分 (question-level grading)
- 初步失效模式分析 (initial failure-mode analysis)

在写结论时，应避免把它说成 fully human-grounded benchmark evidence。

## 8. Answer 字段编写原则 (Rules for Answer Fields)

`Reference Answer`、`Minimum Acceptable Answer`、`Critical Error` 应被视为同一个 judging system 中的三个层级，而不是彼此独立的说明栏。

### 8.1 Reference Answer
应写成 evidence boundary 内的真正参考答案，而不是 “should explain ...” 这类说明句。

### 8.2 Minimum Acceptable Answer
应压缩成最低通过线 (minimum passing line)，只保留判断是否过线所必需的核心点。

### 8.3 Critical Error
应只保留 1–2 条 decisive failure pattern，不要写成一般性不足清单。

这三列已经经过校准，并与以下内容对齐：

- source-document evidence
- gold / supporting evidence boundary
- generation pass rule

当前未发现明显超出既有 evidence 支持边界的新结论。

No currently identified answer-field statement appears to introduce a conclusion that clearly exceeds the present evidence boundary.

## 9. 评测协议冻结原则 (Protocol-Freeze Principle)

正式 benchmark 之前，至少应冻结以下几层 protocol。

### 9.1 Corpus version
- corpus version / document list
- cleaning rules

### 9.2 Retrieval configuration
- chunk size
- overlap
- embedding model
- retriever / vector-store settings
- top-k
- reranking choice

### 9.3 Generation configuration
- generator model
- system prompt version
- decoding settings
- 是否允许外部知识 (whether external knowledge is allowed)

### 9.4 Scoring protocol
- rubric version
- answerability labels
- retrieval pass rule version
- generation pass rule version
- simplified failure-taxonomy version

关键原则：

如果 retrieval 或 generation 配置发生了实质变化，应视为一个新 protocol，或一个单独的 control run。 

## 10. 结果展示框架 (Reporting Structure)

主结果应保持紧凑、可解释 (compact and interpretable)。  
主报告可以按以下顺序展开：（暂定）

1. **Overall**
2. **By ABCD**
3. **Error summary（Retrieval / Generation / None）**
4. **By Answerability**（可选补充）

## 11. 这套 benchmark 最适合测什么 (What It Is Best Suited to Measure)

这套 benchmark 最适合测：

- academic-paper corpus 上基础 RAG 的回答质量
- retrieval sufficiency
- 检到证据后是否用对 (post-retrieval evidence use)
- 不同题型的薄弱点 (question-type-specific weaknesses)
- 缺证 / 证据不足时是否乱编 (hallucination / overclaiming)
- 错误前提纠正能力 (false-premise correction)

它不主要用于证明 algorithmic SOTA，也不是通用 public benchmark。

## 12. 局限性 (Limitations)

### 12.1 更接近 semi-rigorous，而非 fully benchmark-grade
因为 evidence drafting、answer drafting 与部分结构整理有 LLM assistance，这套工作流更准确的说法是 **semi-rigorous / exploratory evaluation**，而不是 fully human-grounded benchmark。 

### 12.2 配比属于 engineering heuristics，而不是真实分布估计
A/B/C/D 的配比是为了 coverage 与 interpretability 服务的 engineering heuristics，而不是基于真实用户流量的统计估计。 

### 12.3 目前尚无正式多人校准机制
当前版本尚未纳入 formal multi-rater calibration、inter-annotator agreement 或 adjudication protocol，因此更适合作为课程项目里的 diagnostic study，而不是强 benchmark claim。

## 13. 最简工作流 (Practical Workflow)（暂定）

推荐工作流如下：

1. 冻结 protocol
2. 定稿 Main-36 结构
3. 补 answerability 与 evidence
4. 定稿 retrieval / generation pass rule
5. 抽取 A/B/C/D 做小规模 pilot
6. 再跑正式实验，并按 Retrieval / Generation / None 汇总 failures 
