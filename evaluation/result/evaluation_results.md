# Evaluation Results
- This version is human-annotated and double-checked and rephrased with AI assist.

## QID: 1

In the French-to-English translation setting, what common prompting failure mode do the authors observe?

[Judgement]
- Retrieval: fail
- Generation: fail
- Failure Type: Retrieval failure

[Reason]
The retrieved chunks do not include the target source passage and instead bring in irrelevant material from other papers. Because the required evidence is missing, the model abstains rather than answering from the correct paper. Under the benchmark rubric, retrieval therefore fails, and generation also fails because the final answer does not satisfy the minimum acceptable answer.
---

[Gold Reference]
- Core Evidence (text or summary): “failures ... were often catastrophic in nature. That is, the task of translation was not even attempted. ... instead of a translation, the model would continue with another sentence in French or output blanks or underscores ...”
- Min Acceptable Answer: Says the model often fails by continuing in French rather than giving an English translation, or says the task is not actually attempted.
- Critical Error: Names a generic quality problem like poor translation fluency instead of the paper’s failure mode; says the model translated badly rather than failing to attempt translation.
- Pass Rule:
  - Retrieval: Retrieve the main passage that directly states or defines the common prompting failure mode observed in the French-to-English translation setting; nearby support is optional.
  - Generation: uses retrieved evidence faithfully and answers the asked point

---

[Model Output]
- Generated Answer: The context provided does not contain information about a specific study or paper discussing the French-to-English translation setting or any common prompting failure modes observed. Therefore, based on the given documents, there is no answer to the question regarding common prompting failure modes in the French-to-English translation setting.
- Retrieved Chunks: [Chunk 1 | Source: AndrewKeanGao_2023_PromptEngineeringforLLM.pdf]
languagemodelsthrough“prompts'',or naturallanguageinstructions.Carefullydesignedpromptscanleadtosignificantlybetteroutputs.

------------------------

[Chunk 2 | Source: Shubham_2024_EngineeringMethodsForLLM.pdf]
3.20 M ACHINE TRANSLATION
In this task, a model is tested on it’s ability in terms of tran slation between two languages. The different
datasets which we came across while reading up on different p rompting techniques for this task include
Salient Translation Error Detection Srivastava et al. (202 2), FLORES Costa-juss` a et al. (2022), WMT21
Farhad et al. (2021), Multi-Domain Aharoni & Goldberg (2020 ) and PDC Sun et al. (2020). Table 20 lists

------------------------

[Chunk 3 | Source: Disha_2023_Repository-LevelPromptGenerationforLLM.pdf]
we learn to produce prompts conditioned on each example.
Another important distinction is that we do not require ac-
cess to the weights of the LM. A concurrent work as ours,
(Wang et al., 2022) studies the role of prompt-tuning when
compared to fine-tuning for code translation, defect local-
ization, and code summarization. However, their technique
requires access to the weights of the LLM and they perform
experiments over models that are much smaller in scale than

## QID: 2

According to the paper, why is APE considered an automatic prompt engineering method?

[Judgement]
- Retrieval: pass
- Generation: pass
- Failure Type: 

[Reason]
The retrieved evidence directly supports the paper’s definition of APE as an automatic prompt engineering method: it generates instruction candidates and then evaluates or selects them. The answer follows that evidence faithfully, reaches the minimum acceptable answer, and does not introduce a material error.
---

[Gold Reference]
- Core Evidence (text or summary): “we propose Automatic Prompt Engineer (APE) for automatic instruction generation and selection.” “we treat the instruction as the ‘program,’ optimized by searching over a pool of instruction candidates proposed by an LLM in order to maximize a chosen score function.”
- Min Acceptable Answer: Says APE automatically proposes and scores/selects instruction prompts rather than depending on manual prompt writing alone.
- Critical Error: Describes APE as just a manual prompting trick; omits the generate-and-select/search mechanism.
- Pass Rule:
  - Retrieval: Retrieve the main passage that directly states or defines why APE is considered an automatic prompt engineering method; nearby support is optional.
  - Generation: uses retrieved evidence faithfully and answers the asked point

---

[Model Output]
- Generated Answer: APE (Automatic Prompt Engineer) is considered an automatic prompt engineering method because it proposes a systematic approach for generating and selecting instructions or prompts. Inspired by classical program synthesis and the human approach to prompt engineering, APE aims to automate the process of instruction generation and selection for language models (LLMs). This automation allows for optimizing existing templates to improve performance on various reasoning tasks, thereby addressing the significant dependency of task performance on the quality of prompts used to guide the model. By doing so, APE represents a step towards making prompt engineering more accessible and efficient, potentially leading to better outcomes in tasks that require specific or nuanced instructions from LLMs.
- Retrieved Chunks: [Chunk 1 | Source: YongchaoZhou_2023_LLMPrompt.pdf]
to find a prompt starting with “Let’s” that maximizes the likelihood of these correct reasoning steps.
See Table 5 for the template used for prompt generation and evaluation. APE produces the prompt
“Let’s work this out in a step by step way to be sure we have the right answer.” This generated prompt
further improves performance from 78.7 to 82.0 on MultiArith and from 40.7 to 43.0 on GSM8K. We
believe this general workflow represents a common use-case for APE where prompt engineers use

------------------------

[Chunk 2 | Source: YongchaoZhou_2023_LLMPrompt.pdf]
displayed impressive capabilities as general-purpose computers. However, task performance
depends significantly on the quality of the prompt used to steer the model, and most effective
prompts have been handcrafted by humans. Inspired by classical program synthesis and
the human approach to prompt engineering, we propose Automatic Prompt Engineer 1
(APE) for automatic instruction generation and selection. In our method, we treat the

------------------------

[Chunk 3 | Source: YongchaoZhou_2023_LLMPrompt.pdf]
APE to optimize parts of their exiting templates to improve performance. See Figure 10 for details on
the performance of this prompt on other reasoning tasks.
4.4 T RUTHFUL QA
We apply our method on TruthfulQA (Lin et al., 2022) to see how APE-generated instructions can
steer an LLM to generate answers with different styles, and study the trade-off between truthfulness
and informativeness. Borrowing the metrics from the original paper, we use APE to the learn

## QID: 3

According to the paper, how is worst prompt performance defined?

[Judgement]
- Retrieval: fail
- Generation: fail
- Failure Type: Retrieval failure

[Reason]
The retrieval reaches the correct paper but does not surface the passage that explicitly defines worst prompt performance. The answer then approaches the target by inference rather than by directly grounding itself in the required defining evidence. Under the benchmark criteria, retrieval fails because the key definition was not retrieved, and generation also fails because the answer is not sufficiently grounded in the retrieved support.
---

[Gold Reference]
- Core Evidence (text or summary): The paper defines worst prompt performance as the model’s lower-bound performance across semantically equivalent and syntactically fluent prompt paraphrases for the same query. This gives the metric’s core object: not average performance, but the lowest performance observed under equivalent phrasings.
- Min Acceptable Answer: Says it is the lowest performance observed across semantically equivalent / fluent paraphrases of the same query, not average performance.
- Critical Error: Defines it as average or best prompt performance; treats it as ordinary task accuracy without the lower-bound-under-paraphrase idea.
- Pass Rule:
  - Retrieval: Retrieve the main passage that directly states or defines what the paper means by worst prompt performance; nearby support is optional.
  - Generation: uses retrieved evidence faithfully and answers the asked point

---

[Model Output]
- Generated Answer: The context provided does not explicitly define what "worst prompt performance" means within the paper. However, based on the sections mentioned (Sections 3, 4, and 5), it can be inferred that worst prompt performance refers to the lowest or least effective performance of large language models when dealing with certain prompts. The paper discusses benchmarking these performances, identifying the worst prompts among semantically equivalent ones, and improving their performance through various analyses and methods.
- Retrieved Chunks: [Chunk 1 | Source: BowenCao_2024_WorstPromptPerformanceofLLM.pdf]
parameters, how they were chosen, type of optimizer, etc.) necessary to understand the
results?
Answer: [Yes]
Justification: In Sections 3 (Benchmarking the Worst Prompt Performance), 4 (Identifying
the Worst Prompts) and 5 (Improving Worst Prompt Performance).
Guidelines:
• The answer NA means that the paper does not include experiments.
• The experimental setting should be presented in the core of the paper to a level of detail
that is necessary to appreciate the results and make sense of them.

------------------------

[Chunk 2 | Source: BowenCao_2024_WorstPromptPerformanceofLLM.pdf]
4 Identifying the Worst Prompts
Given the noticeable performance disparities across semantically equivalent prompts, our next
question is: can we identify the worst prompt among these paraphrases? This would not only aid our
understanding of the model’s lower bound but also be instrumental in improving model performance
by guiding the refinement of prompts. We investigate this matter from both model-agnostic (§4.1)
and model-dependent (§4.2) perspectives.
4.1 Model-agnostic Analysis

------------------------

[Chunk 3 | Source: BowenCao_2024_WorstPromptPerformanceofLLM.pdf]
improved, the highest score is only 58.92, suggesting
that the models are largely unable to perceive the im-
pact of the given prompts on their own performance.
Discussion Our explorations over prompt perplexity, Min-k% Prob, hidden states, and model
preference show that it is very challenging to identify the worst prompt in advance even with
the access to the model. Note that this difficulty is often overlooked in previous studies as they

## QID: 4

According to the paper, what problem does Repo-Level Prompt Generator (RLPG) solve, and what is its core value?

[Judgement]
- Retrieval: pass
- Generation: pass
- Failure Type: 

[Reason]
The retrieved evidence is sufficient to cover both parts of the question: RLPG addresses repository-level or cross-file context selection under a limited prompt budget, and its core value is that it automatically builds example-specific prompts from repository context. The answer is not perfectly phrased, but it remains faithful to the retrieved evidence and clears the minimum acceptable threshold for both the problem and the value statement.
---

[Gold Reference]
- Core Evidence (text or summary): The paper frames the prompt-design problem as selecting relevant code context under limited prompt length, where useful context may come from imports, parent classes, sibling files, and other repository locations rather than only the current file. It introduces RLPG as a method that automatically generates example-specific prompts from repository structure and cross-file context without requiring access to LLM weights.
- Min Acceptable Answer: Says RLPG helps choose relevant repository-level / cross-file context under limited prompt length and automatically builds prompts for code completion.
- Critical Error: Reduces RLPG to “using a bigger context window” or generic code prompting; omits repository-aware context selection as the core value.
- Pass Rule:
  - Retrieval: Retrieve the main passage(s) that state both the problem RLPG is designed to solve and its core value; nearby support is optional.
  - Generation: uses retrieved evidence faithfully and answers both parts of the question.

---

[Model Output]
- Generated Answer: According to the paper, the Repository-Level Prompt Generator (RLPG) addresses the issue of improving the effectiveness of large language models in code generation by proposing a method that substitutes part of the default context used by Codex with context from other parts of the repository. The core idea is governed by decisions on what specific context to substitute and where within the repository this context should be taken from. 

The paper highlights the value of RLPG through its ability to generate example-specific prompts, which demonstrates an improvement in performance over using fixed prompt proposals. Specifically, both learned variants of RLPG (RLPG-H and RLPG-R) outperform the RLPG-BM25 method, emphasizing the importance of learning a Prompt Proposal Classifier (PPC). This indicates that by leveraging machine learning to adaptively generate prompts based on repository context, RLPG enhances the performance of large language models in code generation tasks.
- Retrieved Chunks: [Chunk 1 | Source: Disha_2023_Repository-LevelPromptGenerationforLLM.pdf]
In this section, we provide details of our framework. We
start by describing our prompt proposals and then discuss
our prompt proposal classifier which is followed by a de-
scription of the prompt composer.
2.1. Repo-Level Prompt Proposals
The core idea of RLPG consists of substituting part of the de-
fault context used by Codex with context coming from some-
where else in the repository. The decision of what to take
and from where in the repository to take from is governed

------------------------

[Chunk 2 | Source: Disha_2023_Repository-LevelPromptGenerationforLLM.pdf]
Fixed Prompt Proposal (repo-wise)
RLPG-R (repo-wise)
Fixed Prompt Proposal (hole-wise)
RLPG-R (hole-wise)
0
10
20
30
40
50
60 Cur
Sib
SimN
ImpSimN
ImpSib
Imp
PaCl
ImpPaCl
ChCl
ImpChCl
Figure 2. (Top) Variation of RLPG and Fixed Prompt Proposal
with #attempts ( k), when averaged over individual repositories
(repo-wise) and all holes (hole-wise); (Bottom) Mean success rates
of different prompt sources when they are applicable.
good baseline but still performs worse than either the fixed

------------------------

[Chunk 3 | Source: Disha_2023_Repository-LevelPromptGenerationforLLM.pdf]
posal, showing the value of generating example-specific
prompts using RLPG. However, both the learned variants of
RLPG, i.e., RLPG-H and RLPG-R outperform the RLPG-
BM25, highlighting the importance of learning PPC. See
Appendix D.1 and Appendix D.7 for the performance of
all methods across individual repositories. Note that even
though we consider identifier usage as a separate baseline,
one could consider it as one of the prompt proposals leading
to further improved performance of RLPG.

## QID: 5

Why can changing the wording of a prompt change how well it works?

[Judgement]
- Retrieval: fail
- Generation: fail
- Failure Type: Retrieval failure

[Reason]
The retrieval does not satisfy the designed evidence requirement: it misses the intended source paper and fails to surface the key mechanism about prompt wording constraining desired versus undesired continuations. Although the answer gives a broadly plausible explanation, it is generic rather than grounded in the required evidence. Under the benchmark rubric, this should not receive generation pass, and the primary failure remains retrieval.
---

[Gold Reference]
- Core Evidence (text or summary): “The model ... will respond in many ways ... including all the ways unintended by the human operator.” “we want a prompt that is not merely consistent with the desired continuation, but inconsistent with undesired continuations.” “Changing the first line ... will further increase reliability ...”
- Min Acceptable Answer: Says prompt wording changes how well the prompt constrains desired versus undesired continuations, or how well it locates the intended task.
- Critical Error: Explains it only as randomness or “model mood”; says semantically similar wording should work the same regardless of constraint quality.
- Pass Rule:
  - Retrieval: Retrieve at least two evidence units needed to explain or connect the ideas involved in how language dynamics affect prompting performance.
  - Generation: faithfully uses evidence and completes the required integration/comparison

---

[Model Output]
- Generated Answer: Changing the wording of a prompt can affect its performance because prompts are designed to guide large language models (LLMs) on what information or context they should consider when generating responses. The specific words and structure used in a prompt can highlight certain features or aspects of the input data, making them more salient for the model. This can lead to the model focusing on spurious features—unrelated or misleading details that might not be relevant but are emphasized by the wording of the prompt. By changing the wording, one can potentially guide the model away from these spurious features and towards more accurate or desired responses.

Moreover, different wordings can influence how the model interprets the context provided in the prompt. For instance, a prompt with more specific language might help the model better understand the nuances of the task at hand, leading to improved performance. Conversely, overly broad or ambiguous prompts might confuse the model, causing it to generate responses that are less relevant or accurate.

Additionally, the structure and format of the prompt can also impact its effectiveness. For example, breaking down a complex question into multiple prompts or using a more structured format might help the model process information more effectively, leading to better performance. Therefore, changing the wording of a prompt involves considering how it will be interpreted by the LLM, which in turn affects the relevance and accuracy of the generated responses.
- Retrieved Chunks: [Chunk 1 | Source: BowenCao_2024_WorstPromptPerformanceofLLM.pdf]
to spurious features in prompt design or: How i learned to start worrying about prompt formatting.
ArXiv preprint, abs/2310.11324, 2023.
10
69031
https://doi.org/10.52202/079017-2205

------------------------

[Chunk 2 | Source: Silviu_2023_BoostedPromptEnsemblesforLLM.pdf]
Automatic Prompt Engineering It has been observed
that language model performance can be sensitive to the
chosen prompt (Zhao et al., 2021), which has led to in-depth
studies of prompting methodology (Liu et al., 2023; Wang
et al., 2022a) and the development of several approaches to
automatic prompt generation (Shin et al., 2020; Gao et al.,
2020). While some of these approaches are gradient-based
(Li & Liang, 2021; Qin & Eisner, 2021), requiring access

------------------------

[Chunk 3 | Source: PranabSahoo_2024_promptEngineering.pdf]
review approach, we meticulously delve into the intricacies
of diverse cutting-edge prompting methods. Our examination
encompasses their applications, the language models utilized,
and the datasets subjected to experimentation, providing a
detailed and nuanced analysis of the evolving landscape of
prompt engineering. Additionally, we discuss the pros and
cons of these techniques, offering insights into their compara-
tive efficacy. We present a comprehensive taxonomy diagram

## QID: 6

Why does the paper argue that Bayesian Optimization is suitable for black-box LLM settings?

[Judgement]
- Retrieval: pass
- Generation: pass
- Failure Type: 

[Reason]
The retrieved evidence is relevant and sufficient: it supports the key point that prompt evaluation in black-box LLM settings is expensive and that Bayesian Optimization is suitable because it is sample-efficient in such settings. The answer uses that evidence correctly, covers the black-box and expensive-evaluation logic, and completes the required explanation.
---

[Gold Reference]
- Core Evidence (text or summary): Anchor: “sample efficiency”. The paper explains that prompt evaluation requires repeated queries to the LLM, so the objective function is both black-box and expensive to evaluate; Bayesian Optimization is suitable for this setting because it is known for sample efficiency, modular structure, and adaptability in black-box optimization.
- Min Acceptable Answer: Says BO fits because prompt evaluation is black-box and expensive, and BO is sample-efficient.
- Critical Error: Claims BO is used because gradients are available; gives only a generic “BO is strong” answer without the black-box/expensive-evaluation reason.
- Pass Rule:
  - Retrieval: Retrieve at least two evidence units needed to explain or connect the ideas involved in why Bayesian Optimization suits black-box LLM settings.
  - Generation: faithfully uses evidence and completes the required integration/comparison

---

[Model Output]
- Generated Answer: The paper argues that Bayesian Optimization is suitable for black-box Large Language Model (LLM) settings because it offers several advantages in terms of sample efficiency, modular structure, and versatility. Specifically, Bayesian Optimization methods are designed to be efficient in scenarios where function evaluations are expensive or costly, which aligns well with the computational demands of working with large language models like GPT-4 as a black-box service. The paper highlights that exhaustive search strategies for optimizing prompts within these models are impractical due to the vast combinatorial search space, making Bayesian Optimization methods particularly appealing due to their ability to navigate such complex spaces efficiently using fewer evaluations.

Moreover, the modular structure of Bayesian Optimization allows it to be easily adapted and integrated with different components or frameworks, which is beneficial when working with diverse LLMs. The paper also mentions that Bayesian Optimization can handle uncertainty quantification effectively, providing a layer of reliability in the optimization process. This feature is crucial for ensuring that the optimized prompts are not only effective but also robust against potential uncertainties within the black-box LLM environment.

Additionally, the paper references previous works like InstructZero and INSTINCT which utilize neural networks or similar techniques to optimize prompts in black-box settings, further supporting the argument that Bayesian Optimization methods can be effectively applied alongside other machine learning approaches for prompt optimization tasks. The combination of these factors—sample efficiency, modular design, uncertainty handling, and compatibility with existing methodologies—contributes to the paper's assertion that Bayesian Optimization is well-suited for optimizing prompts in black-box Large Language Models.
- Retrieved Chunks: [Chunk 1 | Source: AntonioSabbatella_2024_PromptOptimization.pdf]
which adds a layer of uncertainty quantification to improve the reliability of prompt tuning
and to consider a strict notion of a likelihood-free black-box setting.
Bayesian approaches : Bayesian Optimization is a widely considered a sampling-
efficient solution for black-box optimization. It has been gaining importance for prompt
optimization in large language models. Ref. [ 24] propose a two-stage approach called
InstructZero: using an open source LLM, the first stage converts a prompt into an in-

------------------------

[Chunk 2 | Source: AntonioSabbatella_2024_PromptOptimization.pdf]
struction and (in the second stage) submits it to the black-box LLM—which computes
the performance score of this instruction and then sends it to the Bayesian Optimization
module to produce new soft prompts. A specific application in the context of adversarial
learning/optimization is reported in [25]. A similar approach, namely INSTINCT, has been
recently proposed in [26]. The main characteristic is that a neural network is used instead

------------------------

[Chunk 3 | Source: AntonioSabbatella_2024_PromptOptimization.pdf]
of a Gaussian Process in the BO algorithm. Finally, a preliminary version of the BO-based
prompt optimization algorithm presented in this manuscript has been briefly described
in [27]. LLMs have also been proposed for the multi-armed bandit (MAB) problems, which
are closely related to Bayesian Optimization. Ref. [28] propose an LLM-based strategy that
enables adaptive balancing of exploration and exploitation. Ref. [29] presents an approach

## QID: 7

Why is prompt optimization basically a combinatorial search problem here?

[Judgement]
- Retrieval: pass
- Generation: pass
- Failure Type: 

[Reason]
The retrieved evidence is sufficient to support the paper’s core logic: prompts are discrete n-gram or token sequences, and the size of the search space grows combinatorially with vocabulary size and prompt length. The answer follows that evidence faithfully, explains why exhaustive search is impractical, and correctly frames the task as a combinatorial search problem.
---

[Gold Reference]
- Core Evidence (text or summary): Anchor: “combinatorial optimization problem”. The paper defines a prompt as an n-gram sequence selected from the vocabulary; therefore, the number of possible prompts grows exponentially with vocabulary size and prompt length, making exhaustive search infeasible, so the task is fundamentally a combinatorial search problem.
- Min Acceptable Answer: Says prompts are discrete token or n-gram combinations and the search space grows exponentially / as |V|^L.
- Critical Error: Calls it continuous optimization from the outset; discusses difficulty without mentioning the discrete prompt space.
- Pass Rule:
  - Retrieval: Retrieve at least two evidence units needed to explain or connect the ideas involved in why prompt optimization is formulated as a combinatorial optimization problem.
  - Generation: faithfully uses evidence and completes the required integration/comparison

---

[Model Output]
- Generated Answer: Prompt optimization is considered a combinatorial search problem due to the vast and discrete nature of the prompt space. Given the dimension of the vocabulary \(V\) and the prompt length \(L\), the number of possible prompts forms an intractable combinatorial optimization problem, with the search space consisting of all possible combinations that can be generated by concatenating n-grams from \(V\). This discrete nature leads to a large combinatorial search space, making exhaustive search impractical. Therefore, efficient search strategies are needed, such as Bayesian Optimization (BO), which is used in this context for its sample efficiency and modular structure.
- Retrieved Chunks: [Chunk 1 | Source: AntonioSabbatella_2024_PromptOptimization.pdf]
Mathematics 2024, 12, 929 12 of 14
Table 4. Comparative results over different prompt lengths for the task MRPC.
Task Prompt Length Best Score on Test
MRPC 25 79.7619
MRPC 50 78.4431
MRPC 75 78.4195
5. Conclusions
The main conclusion of this paper is that Bayesian Optimization could become an
effective tool for prompt optimization. This vast discrete combinatorial prompt space
poses specific challenges for direct optimization. The large discrete prompt search space is

------------------------

[Chunk 2 | Source: AntonioSabbatella_2024_PromptOptimization.pdf]
Given the dimension of the vocabulary V and the prompt length L, prompt optimiza-
tion is an intractable combinatorial optimization problem, with a search space consisting of

------------------------

[Chunk 3 | Source: AntonioSabbatella_2024_PromptOptimization.pdf]
met. 
 
Figure 1. Prompt optimization loop using BO. 
3.3. Continuous Relaxation of the Combinatorial Space 
The goal of BO, considering the HPT problem, is to ﬁnd the optimal prompt 𝐩∗ ∈𝒱 ℓ. 
It is important to note that the prompt space, 𝒱ℓ, is a combinatorial space consisting of all 
the possible prompts with length ℓ which can be generated by concatenating n-grams 
from 𝒱. Working in this discrete space can be intractable because the number of possible
## QID: 8

What does it mean for reliability if two prompts mean the same thing but get very different results?

[Judgement]
- Retrieval: pass
- Generation: pass
- Failure Type: 

[Reason]
The retrieved evidence is sufficient to support the intended reliability claim: the paper frames robustness in terms of resilience to prompt variation and concludes that models still struggle to maintain high performance across diverse prompts. Although one retrieved chunk is irrelevant, the correct-paper evidence is enough to ground the answer. The generated response faithfully states that large differences across same-meaning prompts indicate a robustness and reliability gap.
---

[Gold Reference]
- Core Evidence (text or summary): Anchor: “significantly sensitive to the prompts” and “substantial performance degradation”. The paper argues that if semantically equivalent prompts yield very different results, the model is not reliably robust to prompt phrasing.
- Min Acceptable Answer: Says semantic equivalence does not guarantee similar performance and that this reveals a robustness / reliability gap.
- Critical Error: Says same-meaning prompts showing different results is unimportant or expected without reliability implications; denies the robustness issue.
- Pass Rule:
  - Retrieval: Retrieve at least two evidence units needed to explain or connect the ideas involved in what large variation across semantically equivalent prompts implies about LLM reliability.
  - Generation: faithfully uses evidence and completes the required integration/comparison

---

[Model Output]
- Generated Answer: It means that there is a lack of prompt consistency, which refers to the inherent resilience of Large Language Models (LLMs) to variations in prompts. If two prompts that are supposed to have the same meaning yield very different results, it indicates that the model is not robust or consistent in its performance across similar inputs. This inconsistency can undermine the reliability and predictability of the LLM's output, making it difficult to trust or depend on the model's responses for critical applications.
- Retrieved Chunks: [Chunk 1 | Source: BowenCao_2024_WorstPromptPerformanceofLLM.pdf]
2 Related Work
Existing research on prompt robustness can be classified into two categories. On the one hand,
research efforts have been focused on enhancing the inherent resilience of LLMs to prompt variations,
namely prompt consistency. On the other hand, progress has been made in automating prompt
engineering, the process to find the optimal prompt that yields the best performance.
Prompt Consistency. Previous studies (Gu et al., 2022; Wang et al., 2023a; Zhu et al., 2023;

------------------------

[Chunk 2 | Source: Disha_2023_Repository-LevelPromptGenerationforLLM.pdf]
Identifier Usage (NN) 64.91 10.52 67.94 12.03
Fixed Prompt Proposal 65.78 12.00 68.01 12.15
RLPG-BM25 66.41 13.07 68.15 12.39
RLPG-H 68.51 16.65 69.26 14.21
RLPG-R 67.80 15.44 69.28 14.26
D.2. Ablation on Performance based on Prompt Proposal
Figure 3 shows the mean success rate of prompt context types when success is counted only for the cases when these prompt
contexts are applicable. As can be seen from the figure, post lines is the most useful prompt context type on an average. The

------------------------

[Chunk 3 | Source: BowenCao_2024_WorstPromptPerformanceofLLM.pdf]
We further illustrate the difficulty in identifying the worst prompt from both model-
agnostic and model-dependent perspectives, emphasizing the absence of a shortcut
to characterize the worst prompt. We also attempt to enhance the worst prompt
performance using existing prompt engineering and prompt consistency methods,
but find that their impact is limited. These findings underscore the need to create
more resilient LLMs that can maintain high performance across diverse prompts.
## QID: 9

Why doesn't a bigger context window automatically fix the prompt design problem?

[Judgement]
- Retrieval: fail
- Generation: fail
- Failure Type: Retrieval failure

[Reason]
The retriever reaches the correct paper, but the returned chunks do not surface the key argument required by the question: a larger context window may reduce truncation pressure, yet it does not remove the need to decide which repository-level context is relevant enough to include. The generated answer explicitly falls back to inference rather than direct support from the retrieved evidence, so under the benchmark rubric both retrieval and generation fail, with retrieval as the primary failure.
---

[Gold Reference]
- Core Evidence (text or summary): The paper states that larger context windows do not remove the need for prompt design: many repositories are still longer than the available context length, and RLPG remains useful for deciding which contexts are relevant to include in the prompt.
- Min Acceptable Answer: Says more tokens help but do not automatically decide what relevant context to include, especially when repositories are still too large or context is distributed.
- Critical Error: Claims larger context windows remove the prompt-design problem; treats the issue as pure token-count expansion with no relevance-selection problem.
- Pass Rule:
  - Retrieval: Retrieve at least two evidence units needed to explain or connect the ideas involved in why a longer context window does not by itself solve the prompt design problem.
  - Generation: faithfully uses evidence and completes the required integration/comparison

---

[Model Output]
- Generated Answer: The answer cannot be directly derived from the provided context as it does not explicitly discuss the prompt design problem or how a larger context window relates to fixing it. However, based on the information given, we can infer that:

A smaller context length might lead to loss of relevant information when truncating the prompt proposal context to fit inside the prompt due to its limited size. This implies that even if there is more context available (i.e., a bigger context window), simply increasing the context size may not automatically solve the prompt design problem because it still needs to be effectively utilized within the constraints of the prompt.

The context suggests that the effectiveness of different types of prompt contexts can vary, with some contributing more than others. This implies that there might be issues related to how well certain prompts are designed or integrated into the larger context, which could affect their performance regardless of the context size.

In summary, while a bigger context window theoretically provides more information for potential use in improving prompt effectiveness, the actual design and integration of these prompts within the constraints of the available context length might still pose challenges that need to be addressed separately.
- Retrieved Chunks: [Chunk 1 | Source: Disha_2023_Repository-LevelPromptGenerationforLLM.pdf]
our prompt proposals. However, when compared to a larger context length, the relative gains are smaller. This is expected as
a smaller context length means that the relevant context coming from a prompt proposal needs to be truncated to make it fit
inside the prompt, thereby leading to loss of information.
20

------------------------

[Chunk 2 | Source: Disha_2023_Repository-LevelPromptGenerationforLLM.pdf]
contribution from other prompt context types though smaller than post lines is still significant highlighting the importance of
each prompt context type.
18

------------------------

[Chunk 3 | Source: Disha_2023_Repository-LevelPromptGenerationforLLM.pdf]
normally used by Codex (default Codex context) to generate
the prompt. Since the total length that can be used for a
prompt is fixed, we adopted a dynamic context allocation
strategy where if the prompt proposal context is shorter than
its allocated length, we assign the remaining portion from
the prompt proposal context to the default Codex context.
The prompt proposal context is always added before the
default Codex context. For all prompt proposals, we assign
## QID: 10

Why can prompt engineering become a workflow problem, not just a model problem, in real prototyping?

[Judgement]
- Retrieval: fail
- Generation: fail
- Failure Type: Retrieval failure

[Reason]
The retrieved evidence comes from general survey-style discussion of prompt engineering rather than the paper’s specific claim that prototyping creates an iterative workflow burden involving prompt design, testing, debugging, and example sourcing. Because that workflow framing is not actually retrieved, the answer stays generic and does not satisfy the intended evidence requirement. Under the benchmark rubric, retrieval fails first, and generation also fails because the final answer is not grounded in the required source logic.
---

[Gold Reference]
- Core Evidence (text or summary): The paper shows that prompt engineering becomes a workflow problem because practitioners must not only write prompts, but also reverse-engineer prompt designs, source examples, debug outputs, and evaluate whether prompts are actually improving over time.
- Min Acceptable Answer: Says it becomes a workflow problem because users must iteratively design, test, debug, evaluate, or source examples for prompts, not just depend on the model.
- Critical Error: Explains it only as a limitation of the model itself; omits the iterative human workflow burden.
- Pass Rule:
  - Retrieval: Retrieve at least two evidence units needed to explain or connect the ideas involved in why prompt engineering is framed as a workflow or interaction-design problem rather than only a model problem.
  - Generation: faithfully uses evidence and completes the required integration/comparison

---

[Model Output]
- Generated Answer: Prompt engineering can become a workflow problem rather than solely a model problem in real prototyping because it involves creating effective natural language instructions (prompts) that guide large language models (LLMs) to extract knowledge efficiently and accurately. The process of crafting these prompts requires deep understanding of both the LLM's capabilities and the specific task requirements, which can be complex and time-consuming. This is particularly challenging in real-world applications where tasks are diverse and require tailored approaches.

The workflow problem arises due to several factors:

1. **Task-Specificity**: Different tasks may require different types of prompts that effectively elicit relevant information from LLMs. Crafting these prompts requires domain expertise, understanding the nuances of language, and experimenting with various formulations to find the most effective ones.

2. **Model Adaptation**: While LLMs are powerful in processing large volumes of text, their responses can be influenced by the quality and specificity of the prompts provided. This necessitates continuous tuning and optimization of prompts based on feedback from model performance, which can become a significant part of the workflow.

3. **Scalability Issues**: As the number of tasks or datasets increases, managing and optimizing prompts for each becomes more challenging. This requires systematic approaches to categorize, evaluate, and refine prompts across different applications and models.

4. **Integration with Other Tools and Processes**: Prompt engineering needs to be integrated seamlessly into existing workflows, which can involve collaboration between multiple teams (e.g., data scientists, engineers, domain experts). Ensuring that the prompt creation process is efficient and does not disrupt ongoing operations adds another layer of complexity.

5. **Continuous Learning and Adaptation**: As new models are developed or as tasks evolve over time, prompts may need to be updated or replaced. This requires a dynamic approach to prompt engineering that can adapt to changes in model capabilities and task requirements.

In summary, while the core challenge of prompt engineering is to create effective prompts for LLMs, the workflow problem emerges from the practical challenges of implementing this process efficiently across diverse tasks and models, integrating it into existing workflows, and continuously adapting to new needs.
- Retrieved Chunks: [Chunk 1 | Source: PranabSahoo_2024_promptEngineering.pdf]
is often required for task-specific performance. This is the
transformative promise of prompt engineering, pushing the
boundaries of AI and opening doors to a future brimming with
possibilities. In an ever-evolving landscape, ongoing research
consistently reveals innovative approaches and applications
within prompt engineering. The significance of prompt engi-
neering is underscored by its capacity to steer model responses,
enhancing the adaptability and applicability of LLMs across

------------------------

[Chunk 2 | Source: Shubham_2024_EngineeringMethodsForLLM.pdf]
engineering.
Prompt engineering is the process of creating natural language instructions, or prompts, to extract knowledge
from LLMs in an organized manner. Prompt engineering, in con trast to earlier conventional models, relies
only on the embedded knowledge of LLMs and does not require ex tensive parameter re-training or ﬁne-
1

------------------------

[Chunk 3 | Source: PranabSahoo_2024_promptEngineering.pdf]
of LLMs. This survey paper aims to serve as a foundational
resource that systematically categorizes 41 distinct prompt
engineering techniques based on their targeted functionali-
ties, inspiring further research and empowering innovators in
the evolving landscape of prompt engineering. The analysis
spans applications, models, and datasets, shedding light on the
strengths and limitations of each approach. Furthermore, we
have added a diagram and a table to highlight the important
## QID: 11

Why do prompt design choices have to account for context length and token cost?

[Judgement]
- Retrieval: pass
- Generation: pass
- Failure Type: 

[Reason]
The retrieved evidence is sufficient to support both parts of the trade-off: context length limits how much information can be included or preserved, and longer prompts increase token cost. One chunk states this trade-off directly, while the additional retrieval reinforces the truncation side of the argument. The generated answer remains faithful to that evidence and clears the minimum acceptable threshold.
---

[Gold Reference]
- Core Evidence (text or summary): The paper says prompt design must account for context length and token cost: context length limits how much input the model can consider and generate, and few-shot prompting can make prompts several times longer, increasing cost.
- Min Acceptable Answer: Says prompt choices must consider limited context window plus increased token cost from longer prompts / examples.
- Critical Error: Claims longer prompts are effectively free or always better; ignores context-window and cost trade-offs.
- Pass Rule:
  - Retrieval: Retrieve at least two evidence units needed to explain or connect the ideas involved in why prompt engineering must consider context length and token cost.
  - Generation: faithfully uses evidence and completes the required integration/comparison

---

[Model Output]
- Generated Answer: Prompt design choices must account for context length and token cost because these factors directly impact the performance, efficiency, and effectiveness of large language models (LLMs) when processing prompts. Context length refers to how much input an LLM can consider and generate at once; as this limit increases with newer models like GPT-4 and Anthropic’s Claude, providing more tokens in a prompt can lead to deteriorating performance or increased computational cost. Token cost is related to the resources required to process each token of information, which becomes more significant when dealing with longer prompts. Prompt truncation due to context length limitations may result in loss of relevant information from the prompt proposal, affecting its utility and outcomes. Therefore, managing these aspects ensures optimal use of LLMs for tasks requiring specific input lengths or within budget constraints.
- Retrieved Chunks: [Chunk 1 | Source: Disha_2023_Repository-LevelPromptGenerationforLLM.pdf]
our prompt proposals. However, when compared to a larger context length, the relative gains are smaller. This is expected as
a smaller context length means that the relevant context coming from a prompt proposal needs to be truncated to make it fit
inside the prompt, thereby leading to loss of information.
20

------------------------

[Chunk 2 | Source: AndrewKeanGao_2023_PromptEngineeringforLLM.pdf]
One of the main limitations of prompting is the context length of LLMs, which is essentially howmuchinput an LLMcan consider and generate. Context lengths are rapidly increasing, with GPT-4 having a32,000 token (~24,000 word) context length and Anthropic’s Claude having a 100,000 token (75,000word) context length. Someusershavereporteddeterioratingperformanceasmoretokensareprovidedinthe prompt. Another consideration for prompt engineering is cost. For example, few-shot prompting canmultiply the length of

------------------------

[Chunk 3 | Source: Disha_2023_Repository-LevelPromptGenerationforLLM.pdf]
context length allowed by Codex. Therefore, in PPC when
we obtain the representation of the prompt proposal context,
we need to truncate the context. This might lead to omitting
important parts of the prompt proposal context in certain
cases. Using pretrained models that allow larger context
length or models that augment the context (Wu et al., 2022)
offer avenues for future work. See Appendix D.5 for results
when we use a smaller context length with Codex.
## QID: 12

According to the survey, how can prompt engineering extend task adaptation without changing model parameters?

[Judgement]
- Retrieval: pass
- Generation: pass
- Failure Type: 

[Reason]
This is a clean success case. The retrieved evidence directly supports the paper’s claim that prompt engineering adapts pre-trained models to downstream tasks through task-specific instructions or examples without modifying core model parameters. The answer states that point clearly, faithfully, and with no material distortion.
---

[Gold Reference]
- Core Evidence (text or summary): The survey says prompt engineering adapts models to tasks by using task-specific instructions to guide model behavior “without modifying the core model parameters.” It presents prompts as a way to elicit desired behavior from existing pre-trained models rather than updating the models themselves.
- Min Acceptable Answer: Says prompts adapt the model to a task through instructions / examples without updating model parameters or fine-tuning.
- Critical Error: Claims parameter updates or fine-tuning are required; treats prompting as ordinary retraining.
- Pass Rule:
  - Retrieval: Retrieve at least two evidence units needed to explain or connect the ideas involved in why prompt engineering can extend task adaptation without changing model parameters.
  - Generation: faithfully uses evidence and completes the required integration/comparison

---

[Model Output]
- Generated Answer: Prompt engineering extends task adaptation without changing model parameters by leveraging task-specific instructions, known as prompts. These prompts allow for seamless integration of pre-trained models into downstream tasks by eliciting desired model behaviors solely based on the given prompt, thus enhancing model efficacy without modifying the core model parameters.
- Retrieved Chunks: [Chunk 1 | Source: PranabSahoo_2024_promptEngineering.pdf]
is often required for task-specific performance. This is the
transformative promise of prompt engineering, pushing the
boundaries of AI and opening doors to a future brimming with
possibilities. In an ever-evolving landscape, ongoing research
consistently reveals innovative approaches and applications
within prompt engineering. The significance of prompt engi-
neering is underscored by its capacity to steer model responses,
enhancing the adaptability and applicability of LLMs across

------------------------

[Chunk 2 | Source: PranabSahoo_2024_promptEngineering.pdf]
elements shaping the prompt, and a user input interface.
evident in its transformative impact on the adaptability of
LLMs and VLMs. By offering a mechanism to fine-tune
model outputs through carefully crafted instructions, prompt
engineering enables these models to excel across diverse tasks
and domains. This adaptability is different from traditional
paradigms, where model retraining or extensive fine-tuning
is often required for task-specific performance. This is the

------------------------

[Chunk 3 | Source: PranabSahoo_2024_promptEngineering.pdf]
Abstract
Prompt engineering has emerged as an indispens-
able technique for extending the capabilities of large
language models (LLMs) and vision-language mod-
els (VLMs). This approach leverages task-specific
instructions, known as prompts, to enhance model
efficacy without modifying the core model param-
eters. Rather than updating the model parameters,
prompts allow seamless integration of pre-trained
models into downstream tasks by eliciting desired
model behaviors solely based on the given prompt.
## QID: 13

How does the paper distinguish manual prompt design from automatic prompt search?

[Judgement]
- Retrieval: fail
- Generation: fail
- Failure Type: Retrieval failure

[Reason]
The retrieved chunks do not surface the target paper’s own contrast between handcrafted prompts and automatic generation or selection. Instead, they mix in adjacent but wrong-source claims about user burden and labeled-data-heavy automatic prompting, which makes the final answer sound plausible without grounding it in the required evidence. Under the benchmark rubric, retrieval fails because the comparison is not supported from the intended source, and generation also fails because the answer does not faithfully complete the paper-specific distinction.
---

[Gold Reference]
- Core Evidence (text or summary): “most effective prompts have been handcrafted by humans.” “To reduce the human effort involved in creating and validating effective instructions, we propose a novel algorithm using LLMs to generate and select instructions automatically.”
- Min Acceptable Answer: Mentions human handcrafting / trial-and-error versus automatic generation / search / selection.
- Critical Error: Says both are manual; reverses which side performs the search and selection.
- Pass Rule:
  - Retrieval: Retrieve evidence for both sides of the asked distinction about the distinction between manual prompt design and automatic prompt search, not just one term.
  - Generation: faithfully uses evidence and completes the required integration/comparison

---

[Model Output]
- Generated Answer: The paper distinguishes manual prompt design from automatic prompt search by highlighting that manual prompt design requires users to master the art of creating optimal prompts, which is unrealistic for most users due to time constraints. Automatic prompt search, on the other hand, involves using algorithms and methods to generate prompts without requiring extensive user input or expertise. This approach often necessitates testing on substantial labeled data to ensure the effectiveness of the generated prompts.
- Retrieved Chunks: [Chunk 1 | Source: Silviu_2023_BoostedPromptEnsemblesforLLM.pdf]
Automatic Prompt Engineering It has been observed
that language model performance can be sensitive to the
chosen prompt (Zhao et al., 2021), which has led to in-depth
studies of prompting methodology (Liu et al., 2023; Wang
et al., 2022a) and the development of several approaches to
automatic prompt generation (Shin et al., 2020; Gao et al.,
2020). While some of these approaches are gradient-based
(Li & Liang, 2021; Qin & Eisner, 2021), requiring access

------------------------

[Chunk 2 | Source: BowenCao_2024_WorstPromptPerformanceofLLM.pdf]
Figure 1: An example illustrating the gap between existing benchmarks that evaluate prompt consis-
tency and real user queries.
Despite the efficacy of prompt engineering, it is not without its drawbacks. First, it is unrealistic to
expect users to master the art of designing optimal prompts or to invest a significant amount of time
in doing so. Second, automatic prompt engineering often necessitates testing on substantial labeled

------------------------

[Chunk 3 | Source: Disha_2023_Repository-LevelPromptGenerationforLLM.pdf]
Identifier Usage (NN) 64.91 10.52 67.94 12.03
Fixed Prompt Proposal 65.78 12.00 68.01 12.15
RLPG-BM25 66.41 13.07 68.15 12.39
RLPG-H 68.51 16.65 69.26 14.21
RLPG-R 67.80 15.44 69.28 14.26
D.2. Ablation on Performance based on Prompt Proposal
Figure 3 shows the mean success rate of prompt context types when success is counted only for the cases when these prompt
contexts are applicable. As can be seen from the figure, post lines is the most useful prompt context type on an average. The

## QID: 14

How does the paper distinguish hard prompt tuning from soft prompt tuning?

[Judgement]
- Retrieval: pass
- Generation: pass
- Failure Type: 

[Reason]
The retrieved evidence directly covers both sides of the distinction the question asks for: hard prompt tuning operates in a discrete prompt space, whereas soft prompt tuning searches over continuous embeddings with gradient-based optimization. The answer follows that evidence faithfully, states the contrast cleanly, and reaches the minimum acceptable answer without introducing a material error.
---

[Gold Reference]
- Core Evidence (text or summary): The paper directly distinguishes the two: HPT searches for an optimal prompt directly in a discrete prompt space, while SPT uses “continuous-valued language embeddings” and searches for optimal embeddings in a continuous latent space with gradient-based methods.
- Min Acceptable Answer: States discrete hard prompts versus continuous soft embeddings, and mentions that hard prompts do not require gradients.
- Critical Error: Swaps hard and soft definitions; claims hard prompts are continuous embeddings or require gradients.
- Pass Rule:
  - Retrieval: Retrieve evidence for both sides of the asked distinction about the distinction between hard prompt tuning and soft prompt tuning, not just one term.
  - Generation: faithfully uses evidence and completes the required integration/comparison

---

[Model Output]
- Generated Answer: The paper distinguishes hard prompt tuning from soft prompt tuning by stating that hard prompt tuning directly searches for an optimal prompt in the combinatorial search space V^L, while soft prompt tuning uses continuous-valued language embeddings and searches for the optimal embedding via gradient-based optimization in the resulting continuous latent space.
- Retrieved Chunks: [Chunk 1 | Source: AntonioSabbatella_2024_PromptOptimization.pdf]
are elements of the vocabulary V.
Prompt engineering methods can be split into two categories—Hard Prompt Tun-
ing (HPT), which directly searches for an optimal prompt in the combinatorial search
space V L, and Soft Prompt Tuning (SPT), which uses continuous-valued language em-
beddings and searches for the optimal embedding via gradient-based optimization in the
resulting continuous latent space. It is important to remark that hard prompts have two
important advantages:

------------------------

[Chunk 2 | Source: AntonioSabbatella_2024_PromptOptimization.pdf]
and describes hard prompt tuning via Bayesian Optimization and the continuous
relaxation of the combinatorial space.
• Section 4 “Computational Results” presents datasets, baselines, andcomputational results.
• Section 5 contains conclusions, limitations, and perspectives of the proposed approach.
2. Related Works
Different modeling and algorithmic strategies have been proposed for prompt opti-
mization. Ref. [ 4] were among the first to demonstrate the power of prompting for task

------------------------

[Chunk 3 | Source: BowenCao_2024_WorstPromptPerformanceofLLM.pdf]
parameters, how they were chosen, type of optimizer, etc.) necessary to understand the
results?
Answer: [Yes]
Justification: In Sections 3 (Benchmarking the Worst Prompt Performance), 4 (Identifying
the Worst Prompts) and 5 (Improving Worst Prompt Performance).
Guidelines:
• The answer NA means that the paper does not include experiments.
• The experimental setting should be presented in the core of the paper to a level of detail
that is necessary to appreciate the results and make sense of them.

## QID: 15

According to the paper, how do real-world user queries differ from task-specific benchmark prompts?

[Judgement]
- Retrieval: pass
- Generation: pass
- Failure Type: 

[Reason]
The retrieved evidence is sufficient to support both sides of the contrast: the paper explicitly states that real-world user queries often do not separate task-level instruction from case-level input, whereas benchmark prompts are built around cleaner task-specific formats. The generated answer uses that evidence faithfully and correctly concludes that real-world queries are broader, messier, and less explicitly structured than benchmark prompts.
---

[Gold Reference]
- Core Evidence (text or summary): Anchor: “real-world user queries often do not explicitly segregate task-level instruction and case-level input”. The paper says real user queries are not neatly separated into benchmark-style instruction and input fields and may span many different tasks.
- Min Acceptable Answer: Mentions that real-world queries are messier / less explicitly structured than benchmark prompts, or that they cover broader task variation instead of a neat task-specific format.
- Critical Error: Claims the two are basically the same apart from wording polish; reverses which side is tidy / task-specific.
- Pass Rule:
  - Retrieval: Retrieve evidence for both sides of the asked distinction about the distinction between real-world user queries and task-specific benchmark prompts, not just one term.
  - Generation: faithfully uses evidence and completes the required integration/comparison

---

[Model Output]
- Generated Answer: According to the paper, real-world user queries often do not explicitly segregate task-level instruction and case-level input (See the right part of Figure 1). These queries may cover a wide array of tasks and it is not possible to optimize the prompts through evaluating on a task-specific testing set. This indicates that real-world user queries are more diverse and less structured compared to task-specific benchmark prompts, which are often designed with clear task-level instructions and case-level input separation for evaluation purposes.
- Retrieved Chunks: [Chunk 1 | Source: BowenCao_2024_WorstPromptPerformanceofLLM.pdf]
Figure 1: An example illustrating the gap between existing benchmarks that evaluate prompt consis-
tency and real user queries.
Despite the efficacy of prompt engineering, it is not without its drawbacks. First, it is unrealistic to
expect users to master the art of designing optimal prompts or to invest a significant amount of time
in doing so. Second, automatic prompt engineering often necessitates testing on substantial labeled

------------------------

[Chunk 2 | Source: BowenCao_2024_WorstPromptPerformanceofLLM.pdf]
that the best task-level instruction might vary across individual cases. Second, they overlook the
impact of variations in case-level input on model performance. Last but not least, real-world user
queries often do not explicitly segregate task-level instruction and case-level input (See the right part
of Figure 1). These queries may cover a wide array of tasks and it is not possible to optimize the
prompts through evaluating on a task-specific testing set.

------------------------

[Chunk 3 | Source: BowenCao_2024_WorstPromptPerformanceofLLM.pdf]
variations. We introduced a new benchmark that shifts the focus from task-level instructions to case-
level queries. Extensive experiments on ChatGPT and six open-source LLMs, revealed the substantial
performance variability across different prompts, the challenge of predicting worst prompts, and the
limited efficacy of existing methods for improving the worst prompts performance. Our findings
underscored the importance of continued research into prompt robustness in more realistic settings.

## QID: 16

How does the paper distinguish single-prompt, bagged-prompt, and boosted prompt ensembles?

[Judgement]
- Retrieval: fail
- Generation: fail
- Failure Type: Retrieval failure

[Reason]
The retrieved chunks support only a partial comparison: they show that boosted ensembles outperform single-prompt and bagged baselines, but they do not retrieve the defining evidence needed to distinguish all three methods cleanly—especially single-prompt self-consistency, random bagging, and iterative hard-example-based boosting. The answer therefore stays at the level of relative performance and high-level ensemble framing rather than the required method-level distinction. Under the benchmark rubric, retrieval fails because the needed three-way evidence is incomplete, and generation also fails because the final answer does not fully and faithfully distinguish the compared methods.
---

[Gold Reference]
- Core Evidence (text or summary): Single-prompt: “self-consistency ... uses a single prompt and creates an ensemble in output space.” Bagged-prompt: “bagged prompts ... chooses several few shot prompts at random.” Boosted prompt ensemble: the method “iteratively adds an informative prompt” and forms new prompts from “hard” examples on which the previous ensemble is uncertain.
- Min Acceptable Answer: Must distinguish all three: one prompt with output-space ensembling, random prompt-space bagging, and iterative hard-example-based boosting.
- Critical Error: Collapses bagged and boosted into the same random multi-prompt method; describes single-prompt as already using multiple prompt variants.
- Pass Rule:
  - Retrieval: Retrieve evidence covering all three compared methods—single-prompt, bagged-prompt, and boosted prompt ensembles—not just one or two of them.
  - Generation: uses retrieved evidence faithfully and correctly distinguishes all three methods.

---

[Model Output]
- Generated Answer: The paper distinguishes between single-prompt, bagged-prompt, and boosted prompt ensembles based on their performance when dealing with small training datasets (50-300 samples). Specifically, it finds that boosting offers a performance advantage over both randomly bagging few-shot examples and using single-prompt self-consistency. The difference can be notably large if the initial prompt is suboptimal. Boosted prompt ensembles are designed to work well together as an ensemble, aiming for combined predictions that outperform those of a single prompt output space ensemble or a multi-prompt bagged ensemble.
- Retrieved Chunks: [Chunk 1 | Source: Silviu_2023_BoostedPromptEnsemblesforLLM.pdf]
single prompt samples for self-consistency, and for bagging
and boosting, 10 samples from each of 10 prompts.
Do boosted prompt ensembles offer a performance ad-
vantage over single prompt and bagged ensembles?
Yes, in all cases, when a small training dataset (50-300
samples) is available, we ﬁnd that boosting is superior to
randomly bagging few shot examples as well as to single-
prompt self-consistency. The difference to the latter can be
quite large if the initial prompt is suboptimal, as observed

------------------------

[Chunk 2 | Source: Silviu_2023_BoostedPromptEnsemblesforLLM.pdf]
advantage over single prompt and bagged prompt en-
sembles?
• How does our method’s performance vary with the
amount of annotation available?
• How sensitive is boosting to the initial prompt?
• How does varying the number of ensemble members /
samples per ensemble member impact results?
• How does the level of “sufﬁcient agreement” for deter-
mining correctness impact test-time boosting?
• Can we further improve performance by applying
weights to the ensemble members?

------------------------

[Chunk 3 | Source: Silviu_2023_BoostedPromptEnsemblesforLLM.pdf]
training examples as in classical boosting when optimizing
a “verbalizer” that maps model outputs to classes.
3. Boosted Prompt Ensembles
Our goal is to construct a set of few shot prompts for a
pretrained language model that work well together as an
ensemble, in the sense that their combined predictions do
better than the predictions of a single prompt output space
ensemble (Wang et al., 2022c) or a multi-prompt bagged
ensemble (Wang et al., 2022b; Li et al., 2022b).

## QID: 17

How do the two surveys organize the prompt-engineering landscape differently: by application area versus by NLP task?

[Judgement]
- Retrieval: pass
- Generation: pass
- Failure Type: 

[Reason]
The retrieved evidence is sufficient for both sides of the comparison: one survey explicitly organizes prompting methods by application area, while the other structures its taxonomy across NLP tasks. The answer states that contrast correctly and completely enough for the benchmark, even though it refers to the papers as “the first” and “the second” rather than naming them directly.
---

[Gold Reference]
- Core Evidence (text or summary): Doc 9 says prompt-engineering techniques are “categorized by application area” and presents them according to application domains. Doc 10 states that it instead organizes prompting strategies by “different NLP tasks,” using a task-oriented structure rather than an application-oriented one.
- Min Acceptable Answer: Must state both sides: application-area organization for Doc 9 and NLP-task organization for Doc 10.
- Critical Error: Says the two surveys use the same taxonomy; omits one side or reverses which survey uses which principle.
- Pass Rule:
  - Retrieval: Retrieve evidence for both sides of the asked distinction about application-area organization versus NLP-task organization across the two surveys.
  - Generation: faithfully uses evidence and completes the required integration/comparison

---

[Model Output]
- Generated Answer: The first survey organizes the prompt-engineering landscape by categorizing applications, which can encapsulate numerous Natural Language Processing (NLP) tasks. This approach provides a broad overview where one application might cover multiple NLP tasks. The second survey, on the other hand, focuses on organizing the landscape based on different NLP tasks themselves. It likely presents an in-depth look at specific tasks and how they relate to prompt engineering methods.
- Retrieved Chunks: [Chunk 1 | Source: Shubham_2024_EngineeringMethodsForLLM.pdf]
on 29 different NLP tasks. There have not been a lot of prior sy stematic surveys on prompt engineering.
Sahoo et al. (2024) surveys 29 prompting technique papers ba sed on their applications. This is a very broad
categorization as a single application can encapsulate num erous NLP tasks. For example, one of the appli-
cations which they discuss is reasoning and logic which can have plethora of NLP tasks like commonsense

------------------------

[Chunk 2 | Source: Shubham_2024_EngineeringMethodsForLLM.pdf]
CoK [Wang et al. (2024), Li et al. (2023c),Cheng et al. (2022) ,
Y e et al. (2023)]
Figure 1: Taxonomy Diagram of Prompt Engineering Methods Ac ross Different NLP Tasks
research papers. Another point to highlight is that in many w orks, the authors have experimented with
different versions of the same dataset, making it difﬁcult f or an absolute comparison between different
prompting techniques applied to them. Based on our understa nding, we have considered all the above-

------------------------

[Chunk 3 | Source: PranabSahoo_2024_promptEngineering.pdf]
this survey aims to serve as a valuable resource for researchers
and practitioners, offering insights into the latest developments
and facilitating a deeper understanding of the evolving land-
scape of prompt engineering. The structure of the paper is
organized as follows: Section 2 presents the prompt engineer-
ing techniques from both basic to advanced by categorizing
application-area and Section 3 provides a conclusion along
with considerations for future research endeavors.
2 Prompt Engineering

## QID: 18

How do the Reynolds paper and the worst-prompt paper describe two different kinds of robustness failure: task not being properly located versus performance collapsing across semantically equivalent phrasings?

[Judgement]
- Retrieval: fail
- Generation: fail
- Failure Type: Retrieval failure

[Reason]
The retrieval fails to bring in the Reynolds evidence about catastrophic task-location failure, so the answer cannot ground the first half of the required cross-paper comparison. What the model produces is instead a generic discussion of prompt consistency plus a partially grounded account of worst-prompt instability, which is not enough to satisfy the designed comparison. Under the benchmark rubric, retrieval is the primary failure, and generation also fails because the final answer does not faithfully distinguish the two paper-specific robustness failures.
---

[Gold Reference]
- Core Evidence (text or summary): Doc 1: “failures ... were often catastrophic in nature. That is, the task of translation was not even attempted.” Doc 4: “Even minor alterations in format, without semantic changes, can trigger substantial performance degradation.” Together they describe two different robustness failures: failure to properly locate/attempt the task vs. large performance drops across semantically equivalent phrasings.
- Min Acceptable Answer: Distinguishes task-not-located / task-not-attempted failure from performance collapse across semantically equivalent phrasings.
- Critical Error: Says both papers study the same failure in the same way; omits one side of the comparison.
- Pass Rule:
  - Retrieval: Retrieve evidence for both sides of the asked distinction about task-location failure in Reynolds and worst-case paraphrase instability in the worst-prompt paper.
  - Generation: faithfully uses evidence and completes the required integration/comparison

---

[Model Output]
- Generated Answer: The context provided does not contain information about a specific paper named "Reynolds paper." However, based on the given documents, we can discuss how the papers described two different kinds of robustness failures.

1. **Prompt Consistency**: The first document discusses research efforts focused on enhancing the inherent resilience of Large Language Models (LLMs) to prompt variations, which is referred to as "prompt consistency." This means that when a model encounters similar prompts or instructions, it should produce consistent and reliable outputs regardless of slight changes in wording.

2. **Worst Prompt Performance**: The second document focuses on identifying the worst prompt performance among semantically equivalent prompts. It suggests that there are noticeable performance disparities across these prompts, which implies robustness failure occurs when the model's performance collapses or significantly degrades across different but semantically similar phrasings of a task.

In summary:
- **Prompt Consistency** addresses the issue where models should maintain consistent performance despite slight variations in prompt wording.
- **Worst Prompt Performance** deals with the scenario where models fail to perform well even when presented with semantically equivalent prompts, indicating a robustness failure related to how well they handle different phrasings of the same task.

These two concepts highlight different aspects of robustness failures: one is about maintaining performance consistency across similar prompts (prompt consistency), and the other is about identifying and understanding why certain phrasings lead to poor model performance (worst prompt performance).
- Retrieved Chunks: [Chunk 1 | Source: BowenCao_2024_WorstPromptPerformanceofLLM.pdf]
2 Related Work
Existing research on prompt robustness can be classified into two categories. On the one hand,
research efforts have been focused on enhancing the inherent resilience of LLMs to prompt variations,
namely prompt consistency. On the other hand, progress has been made in automating prompt
engineering, the process to find the optimal prompt that yields the best performance.
Prompt Consistency. Previous studies (Gu et al., 2022; Wang et al., 2023a; Zhu et al., 2023;

------------------------

[Chunk 2 | Source: BowenCao_2024_WorstPromptPerformanceofLLM.pdf]
Jiasheng Gu, Hongyu Zhao, Hanzi Xu, Liangyu Nie, Hongyuan Mei, and Wenpeng Yin. Robustness
of learning from task instructions. ArXiv preprint, abs/2212.03813, 2022.
Moran Mizrahi, Guy Kaplan, Dan Malkin, Rotem Dror, Dafna Shahaf, and Gabriel Stanovsky. State
of what art? a call for multi-prompt llm evaluation. ArXiv preprint, abs/2401.00595, 2024.
Jiuding Sun, Chantal Shaib, and Byron C Wallace. Evaluating the zero-shot robustness of instruction-
tuned language models. ArXiv preprint, abs/2306.11270, 2023.

------------------------

[Chunk 3 | Source: BowenCao_2024_WorstPromptPerformanceofLLM.pdf]
4 Identifying the Worst Prompts
Given the noticeable performance disparities across semantically equivalent prompts, our next
question is: can we identify the worst prompt among these paraphrases? This would not only aid our
understanding of the model’s lower bound but also be instrumental in improving model performance
by guiding the refinement of prompts. We investigate this matter from both model-agnostic (§4.1)
and model-dependent (§4.2) perspectives.
4.1 Model-agnostic Analysis

## QID: 19

What pipeline does the paper describe for APE?

[Judgement]
- Retrieval: pass
- Generation: pass
- Failure Type: None

[Reason]
The retrieved evidence is sufficient to reconstruct the APE pipeline: candidate instructions are generated, scored, filtered or selected, optionally updated or resampled, and the best instruction is returned. The answer follows that evidence in the correct overall order and clears the minimum acceptable threshold, even though some extra wording goes beyond the most compact gold formulation.
---

[Gold Reference]
- Core Evidence (text or summary): “Use LLM to sample instruction proposals U ← {ρ1, ..., ρm}.” “Evaluate score on the subset ...” “Filter the top k% of instructions with high scores ...” “Update instructions ... or use LLM to resample ...” “Return instruction with the highest score ...”
- Min Acceptable Answer: Gives the ordered flow generate -> score -> filter/select -> optional iterate/resample -> return best.
- Critical Error: Presents the flow out of order or leaves out scoring/selection; describes APE as a one-shot manually written prompt.
- Pass Rule:
  - Retrieval: Retrieve at least two evidence units needed to explain or connect the ideas involved in the APE pipeline described in the paper.
  - Generation: faithfully uses evidence and completes the required integration/comparison

---

[Model Output]
- Generated Answer: The paper describes a pipeline for APE (Algorithmic Prompt Engineering) that involves:

1. **Generating Instructions**: The process starts with generating instructions using either human instructions or model-generated instructions.

2. **Evaluation and Selection**: An evaluation mechanism is used to compute scores for each instruction, allowing the selection of the most appropriate one based on these scores.

3. **Execution**: Once an optimal instruction is selected, it is executed by APE (Algorithmic Prompt Engineering), which can handle a broad range of natural language programs.

4. **Performance Measurement**: The quality and effectiveness of the instructions are measured during execution, particularly through metrics like interquartile mean across various NLP tasks.

5. **Optimization**: In some cases, APE is used to optimize existing prompts (like CoT prompts) by discovering a new prompt that leads to better performance on specific tasks.

This pipeline aims to enhance the capabilities of AI models in executing natural language programs and improving their performance through optimized instructions or prompts.
- Retrieved Chunks: [Chunk 1 | Source: YongchaoZhou_2023_LLMPrompt.pdf]
algorithm can be thought of as a greedy version of APE, without a search and selection process; thus, we refer to it as “Greedy”. Figure 4 shows the zero-shot performance of InstructGPT using human instructions and model generated instructions. Our algorithm outperforms “Greedy” on every task and achieves equal or better than human performance on

## QID: 20

How does APE differ from Bayesian-optimization-based hard prompt tuning in what is being searched and how candidates are evaluated?

[Judgement]
- Retrieval: fail
- Generation: fail
- Failure Type: Retrieval failure

[Reason]
The retriever does not surface the APE side of the comparison and instead returns only the Bayesian-optimization-based hard prompt tuning material. Because the question requires evidence for both what APE searches and how APE candidates are evaluated, retrieval fails under the pass rule. The generator stays mostly faithful to the incomplete evidence by abstaining from the missing comparison, but the final answer still fails because it does not complete the required two-sided contrast.
---

[Gold Reference]
- Core Evidence (text or summary): Doc 2 states that APE searches over natural-language instruction candidates proposed by an LLM, treating the instruction as the “program.” Doc 3 states that hard prompt tuning searches directly for an optimal prompt sequence in a discrete token / n-gram space. This grounds the difference in what is being searched: instruction candidates versus discrete prompt sequences.
- Min Acceptable Answer: Compares both what is searched (instructions vs hard prompt sequences) and how candidates are evaluated (instruction scoring vs BO objective/query loop).
- Critical Error: Compares only one side of the contrast; treats APE and BO-based hard prompt tuning as the same mechanism.
- Pass Rule:
  - Retrieval: Retrieve evidence for both sides of the asked distinction about what APE searches/evaluates versus what Bayesian-optimization-based hard prompt tuning searches/evaluates.
  - Generation: faithfully uses evidence and completes the required integration/comparison

---

[Model Output]
- Generated Answer: The context provided does not contain enough information to directly compare APE (Assumed Prompt Enhancement) with Bayesian-optimization-based hard prompt tuning. The document discusses Bayesian Optimization as a method for prompt optimization, particularly focusing on Hard Prompt Tuning which searches for an optimal prompt without requiring access to the Large Language Model. However, there is no explicit mention of APE or its differences from Bayesian Optimization in terms of what is being searched and how candidates are evaluated.

To answer this question accurately, we would need more specific details about APE's methodology, including what it searches for (the nature of prompts considered), how it evaluates candidate prompts, and any unique strategies it employs compared to the Bayesian Optimization approach described. Without such information, we cannot provide a precise comparison.
- Retrieved Chunks: [Chunk 1 | Source: AntonioSabbatella_2024_PromptOptimization.pdf]
Mathematics 2024, 12, 929 12 of 14 Table 4. Comparative results over different prompt lengths for the task MRPC. Task Prompt Length Best Score on Test MRPC 25 79.7619 MRPC 50 78.4431 MRPC 75 78.4195 5. Conclusions The main conclusion of this paper is that Bayesian Optimization could become an effective tool for prompt optimization. 

## QID: 21

How do RLPG and PromptMaker represent two different prompt-design problems: selecting relevant context for the model versus helping humans iteratively design and evaluate prompts?

[Judgement]
- Retrieval: fail
- Generation: fail
- Failure Type: Retrieval failure

[Reason]
The retriever does not bring back the PromptMaker evidence needed for the human-centered side of the comparison and therefore fails the two-sided retrieval requirement. The generator then guesses the missing distinction from partial RLPG evidence and produces an overextended answer. Because the comparison is broken at the evidence stage, retrieval is the primary failure and generation also fails to meet the required contrast.
---

[Gold Reference]
- Core Evidence (text or summary): Doc 6 frames prompt design as an automatic context-selection problem under limited prompt length: the system must decide what repository context to include for code completion. Doc 7 frames prompt design as a human prototyping workflow in which users write prompts, test inputs, inspect outputs, and iteratively revise the prompt.
- Min Acceptable Answer: Says RLPG is about model-side context selection / prompt construction, while PromptMaker is about human iterative prompt design and evaluation.
- Critical Error: Reduces the distinction to “one is about code and one is about prototyping” without identifying the underlying problem each paper addresses; collapses both into generic prompt optimization.
- Pass Rule:
  - Retrieval: Retrieve evidence for both sides of the asked distinction about RLPG as context selection and PromptMaker as human-centered prompt design/evaluation.
  - Generation: faithfully uses evidence and completes the required integration/comparison

---

[Model Output]
- Generated Answer: RLPG (Repository-Level Prompt Generation) represents a problem focused on selecting relevant context for the large language models of code. It aims to compose prompt proposals that are useful and can scale well with the number of attempts, as evidenced by its higher success rate compared to other methods.

On the other hand, PromptMaker might represent an iterative process where humans design and evaluate prompts themselves. The context suggests that this approach observes consistent behavior for both fixed prompt proposal methods and RLPG. However, it highlights that for the same value of k (a parameter or variable in the context), RLPG shows a higher success rate, indicating its ability to learn a useful ranking of prompt proposal contexts.

In summary, RLPG is about optimizing context selection for models, while PromptMaker likely pertains to how humans might iteratively interact with prompt design and evaluation, emphasizing a human-centered approach.
- Retrieved Chunks: [Chunk 1 | Source: Disha_2023_Repository-LevelPromptGenerationforLLM.pdf]
Method Success Rate(%) (hole-wise) Rel. ↑(%) (hole-wise) Success Rate(%) (repo-wise) Rel. ↑(%) (repo-wise) Codex (Chen et al., 2021) 58.73 - 60.64 - Post Lines (immediate line after the hole) 65.78 12.00 68.01 12.15 Post Lines (skipping three lines after the hole) 65.11 10.86 66.42 9.53 D.4. Composition of prompt proposals T

## QID: 22

Across the two surveys, which methods are most relevant when the problem is long, chaotic, or noisy context rather than pure reasoning difficulty?

[Judgement]
- Retrieval: fail
- Generation: fail
- Failure Type: Retrieval failure

[Reason]
Although the retrieved material is loosely on-topic, it does not surface the cross-survey evidence needed to map noisy-context problems to retrieval, filtering, grounding, or verification-oriented methods. The answer therefore pivots to a narrower and unsupported method choice rather than the required across-survey mapping. Under the benchmark rubric, retrieval is the primary failure, and generation also fails because the final answer does not meet the minimum acceptable answer.
---

[Gold Reference]
- Core Evidence (text or summary): Doc 9 places methods such as RAG, ReAct, CoVe, CoN, and CoK in a “Reduce Hallucination” grouping centered on retrieval, verification, and knowledge grounding. Doc 10 discusses Implicit RAG in contextual question answering and discusses S2A, Instructed Prompting, CoVe, and CoK in settings involving irrelevant context, truthfulness, or verification.
- Min Acceptable Answer: Must name at least two context-handling methods from the evidence and say they are for grounding / filtering / verification under noisy context rather than pure reasoning alone.
- Critical Error: Answers only with generic reasoning methods such as plain CoT-style reasoning and ignores retrieval / filtering / verification methods; invents methods not supported by the evidence set.
- Pass Rule:
  - Retrieval: Retrieve at least two evidence units needed to map long/noisy-context problems to the most relevant methods across the two surveys.
  - Generation: faithfully uses evidence and completes the required integration/comparison

---

[Model Output]
- Generated Answer: Based on the provided context, the method that is most relevant when dealing with long, chaotic, or noisy contexts rather than pure reasoning difficulty seems to be Thread of Thought (ThoT) Prompting. This method, proposed by Zhou et al. (2023), focuses on handling such contexts and enhancing the reasoning abilities of Large Language Models (LLMs). ThoT is designed to systematically examine extensive contexts into manageable segments for incremental analysis, which makes it particularly suitable for scenarios where the context is complex or noisy.
- Retrieved Chunks: [Chunk 1 | Source: Shubham_2024_EngineeringMethodsForLLM.pdf]
Mathematical Problem Solving. We came across only two datas ets while reading up on different prompting
strategies for this task which are FeTaQA Nan et al

## QID: 23

Why can adding one example sometimes make performance worse instead of better in the translation setting?

[Judgement]
- Retrieval: pass
- Generation: fail
- Failure Type: Generation failure

[Reason]
The retrieved evidence is sufficient to recover the relevant causal direction: adding an example can hurt when the added example changes or misaligns the task signal instead of helping the model interpret it correctly. The generator, however, reframes the issue as overfitting and then adds its own unsupported analysis about generalization. That shifts the answer away from the paper’s intended explanation, so the primary error is in generation rather than retrieval.
---

[Gold Reference]
- Core Evidence (text or summary): “1-shot performed significantly worse than 0-shot.” “the decreased performance was due to semantic contamination from the 1-shot example.” “Instead of treating the example as a categorical guide, it is inferred that the semantic meaning of the examples are relevant to the task ... as part of a consecutive narrative.”
- Min Acceptable Answer: Mentions semantic contamination, or says the example is interpreted as content / narrative rather than a pure demonstration.
- Critical Error: Says extra examples are always safer or better; explains the drop only as noise or an implementation accident.
- Pass Rule:
  - Retrieval: Retrieve the evidence needed to explain why adding one example can worsen performance in the translation setting, including the paper’s account of how examples can mislead or contaminate the task signal.
  - Generation: faithfully uses evidence and explains the causal point asked by the question.

---

[Model Output]
- Generated Answer: Adding an example might sometimes make performance worse instead of better in the translation setting because it could lead to overfitting, particularly in a zero-shot learning scenario. The selected instructions might perform well under conditions where there is no data (zero-shot), but when transitioning to scenarios with limited data (few-shot), they may not generalize effectively and thus negatively impact model performance. This suggests that the instructions might be tailored too closely for the specific task without considering its adaptability in different contexts, leading to a mismatch between instruction and actual context requirements.
- Retrieved Chunks: [Chunk 1 | Source: Disha_2023_Repository-LevelPromptGenerationforLLM.pdf]
we learn to produce prompts conditioned on each example.
Another important distinction is that we do not require ac-
cess to the weights o

## QID: 24

Is APE basically just a fancier 'let’s think step by step,' or is it doing something different?

[Judgement]
- Retrieval: pass
- Generation: pass
- Failure Type: None

[Reason]
The retrieved evidence covers both sides of the distinction the question asks for: it identifies “Let’s think step by step” as the fixed baseline phrase and also shows that APE is used to discover a better prompt through prompt generation and evaluation. The answer directly rejects the false equivalence, explains that APE finds better prompts than the fixed baseline, and stays within the evidence even if it does not restate the search procedure in the most formal terms.
---

[Gold Reference]
- Core Evidence (text or summary): The paper says APE is used “to automatically search for the best answer-prefix” and reports a discovered prompt that improves over the fixed phrase “Let’s think step by step.” This shows that APE is doing automatic search over candidate prompts / answer prefixes rather than simply reusing one fixed CoT phrase.
- Min Acceptable Answer: Says APE is not just nicer wording of the baseline and that it automatically searches/evaluates prompts instead of using one fixed handcrafted phrase.
- Critical Error: Collapses APE into ordinary chain-of-thought wording; misses the automatic search/evaluation mechanism.
- Pass Rule:
  - Retrieval: Retrieve evidence for both sides of the asked distinction: the APE search pipeline and the fixed baseline prompt.
  - Generation: faithfully uses evidence and completes the required integration/comparison

---

[Model Output]
- Generated Answer: APE (Automated Prompt Engineer) is not merely a fancier version of "let's think step by step." Based on the context provided, APE discovers better chain-of-thought (CoT) prompts than simple instructions like "Let’s think step by step." It finds more general and effective prompts such as "Let’s work this out in a step by step way to be sure we have the right answer." These prompts are able to improve the performance of large language models (LLMs) on tasks like zero-shot chain-of-thought reasoning, improving their accuracy from 78.7% to 82.0% on MultiArith and from 40.7% to 43.0% on GSM8K. This demonstrates that APE is capable of finding prompts that can significantly enhance the performance of LLMs beyond what simple step-by-step instructions might offer, suggesting it performs a more sophisticated task than just providing basic guidance.
- Retrieved Chunks: [Chunk 1 | Source: YongchaoZhou_2023_LLMPrompt.pdf]
Published as a conference paper at ICLR 2023
C.3 Z ERO-SHOT CHAIN OF THOUGHT REASONING
We use APE to discover a better chain of thought (CoT) prompt than "Let’s think step by step." from

## QID: 25

If two user queries mean the same thing, why can an LLM still perform very differently on them according to the paper?

[Judgement]
- Retrieval: pass
- Generation: fail
- Failure Type: Generation failure

[Reason]
The retrieved evidence is sufficient to support the key claim that semantically equivalent queries can still produce large performance differences. However, the answer explains this too vaguely as a general lack of robustness rather than stating the paper’s more specific point: the model is sensitive to phrasing or paraphrase form even when meaning is preserved. Because the answer stops short of that target causal framing, generation does not fully meet the minimum acceptable answer.
---

[Gold Reference]
- Core Evidence (text or summary): Anchor: “Even minor alterations in format, without semantic changes” and “semantically equivalent and syntactically fluent prompts”. The paper says LLMs can still perform very differently because they are highly sensitive to phrasing even when meaning is preserved.
- Min Acceptable Answer: Says semantic equivalence does not guarantee similar performance because the model is sensitive to phrasing / paraphrase form.
- Critical Error: Claims same-meaning queries should perform the same; explains the difference by changing task meaning rather than paraphrase sensitivity.
- Pass Rule:
  - Retrieval: Retrieve at least two evidence units needed to explain or connect the ideas involved in why semantically equivalent user queries can still yield different performance.
  - Generation: faithfully uses evidence and completes the required integration/comparison

---

[Model Output]
- Generated Answer: According to the paper, even if two user queries have identical semantics and fluent expressions, large language models (LLMs) might still perform very differently on them. This variability in performance suggests that the current ability of LLMs to follow instructions is not robust enough. Instructions with similar meanings could lead models like Llama2-70B-chat from a level comparable to GPT4 (indicating equivalence to the reference model) to far below average levels. Scaling up models enhances their ability to follow instructions, but it does not necessarily correspondingly improve this robustness.
- Retrieved Chunks: [Chunk 1 | Source: BowenCao_2024_WorstPromptPerformanceofLLM.pdf]
prompt performance, defined as the lowest performance a model exhibits across different paraphrases
of a query with equal semantics and fluency, is a crucial metric for assessing the lower bound of

## QID: 26

If benchmark prompts are tidy but real user questions are messy, why does that matter for evaluating prompt performance?

[Judgement]
- Retrieval: pass
- Generation: pass
- Failure Type: None

[Reason]
The retrieved evidence is sufficient to support the paper’s benchmark critique: existing evaluations focus on tidy task-level benchmark prompts and average performance, which can miss case-level variation in diverse real user queries. The answer correctly connects that distinction to the evaluation implication, namely that benchmark-only testing can misrepresent or overstate how robust prompt performance will be in real-world use.
---

[Gold Reference]
- Core Evidence (text or summary): Anchor: “focused on the LLM’s resilience to task-level instructions exclusively” and “reporting the average performance across testing set cases”. The paper argues that tidy benchmark prompts miss case-level variation and therefore can misrepresent how models behave on messy real user queries.
- Min Acceptable Answer: Says clean benchmark-only evaluation can misrepresent or overstate robustness because it misses variation in real user phrasing.
- Critical Error: Treats the issue as generic UX noise rather than an evaluation-validity / robustness problem; says benchmark wording is fully representative of real-user behavior.
- Pass Rule:
  - Retrieval: Retrieve at least two evidence units needed to connect the benchmark-prompt vs real-user-query distinction with the evaluation implication.
  - Generation: faithfully uses evidence and completes the required integration/comparison

---

[Model Output]
- Generated Answer: The tidiness of benchmark prompts versus the messiness of real user questions matters because it highlights a discrepancy between the evaluation methods used and their applicability to real-world scenarios. Benchmark prompts are often designed with consistency in mind, which can lead to overly simplified or idealized representations of tasks. This contrasts with real user queries, which tend to be more complex, varied, and less structured.

The significance of this difference is that it affects the reliability and generalizability of prompt performance evaluations. When benchmarks fail to capture the nuances and complexities found in actual user interactions, they may not accurately reflect how well a model performs under real-world conditions. This can lead to overestimations or underestimations of a model's capabilities.

To address this issue, researchers might explore alternative strategies such as allowing models to refine prompts themselves or developing more comprehensive evaluation frameworks that consider the full spectrum of user queries and tasks. These approaches aim to bridge the gap between idealized benchmarks and practical applications, ensuring that evaluations are more reflective of real-world performance and challenges.
- Retrieved Chunks: [Chunk 1 | Source: BowenCao_2024_WorstPromptPerformanceofLLM.pdf]
Figure 1: An example illustrating the gap between existing benchmarks that evaluate prompt consistency and real user queries. Despite the efficacy of prompt engineering, it is not without its drawbacks. First, it is unrealistic to expect users to master the art of designing optimal prompts or to invest a significant amount of time in doing so. Second, automatic prompt engineering often necessitates testing on substantial labeled ...

[Chunk 2 | Source: BowenCao_2024_WorstPromptPerformanceofLLM.pdf]
... Prompt Engineering Most existing prompt engineering methodologies fall short in tackling the worst-performance issue, due to the lack of a test set for a single unlabeled prompt. Therefore, we explore two alternative strategies: (i) allowing the model to refine the prompts itself, and (ii) ...

[Chunk 3 | Source: BowenCao_2024_WorstPromptPerformanceofLLM.pdf]
... primarily focus on task-level instructions and assume a corresponding test set for prompt selection. Specifically, they obtain the generation results on the test set and directly measure the downstream task performance. However, this is not possible for diverse real-world user queries, which further underscores the importance of the case-level setup in ROBUST ALPACA EVAL.

## QID: 27

If I do not have labels, how does test-time boosting decide which model-generated answers are trustworthy enough to reuse?

[Judgement]
- Retrieval: fail
- Generation: fail
- Failure Type: Retrieval failure

[Reason]
The retrieval reaches the correct paper but does not surface the full decision rule needed for this question. It mentions substituting labels with model predictions and gestures toward “sufficient” predictions, but it does not clearly retrieve the key mechanism that trustworthiness is determined by majority agreement exceeding a threshold. Because that core evidence is missing, retrieval does not satisfy the pass rule. The answer then shifts to a generic confidence-based explanation, which does not meet the minimum acceptable answer and should not receive generation pass.
---

[Gold Reference]
- Core Evidence (text or summary): Without labels, test-time boosting treats predictions with “sufficient agreement” as correct. A question is reusable if there is “sufficient agreement” for the majority prediction in preds[q], i.e., if majority agreement exceeds a threshold Δ.
- Min Acceptable Answer: Says it uses agreement / majority agreement above a threshold instead of ground-truth labels.
- Critical Error: Says it uses true labels or human annotation at test time; leaves out the agreement-threshold mechanism that makes label-free reuse possible.
- Pass Rule:
  - Retrieval: Retrieve at least two evidence units needed to explain or connect the ideas involved in how test-time boosting selects trustworthy outputs without labels.
  - Generation: faithfully uses evidence and completes the required integration/comparison

---

[Model Output]
- Generated Answer: In the absence of training labels, test-time boosting substitutes ground truth answer labels with model predictions. This approach uses a similar motivation as (Huang et al., 2022), where predictions with "sufficient" confidence or trustworthiness are considered for reusing. The decision on which model-generated answers are trustworthy enough to reuse is based on the confidence level of these predictions, effectively leveraging the model's own outputs in the absence of human-labeled data.
- Retrieved Chunks: [Chunk 1 | Source: Silviu_2023_BoostedPromptEnsemblesforLLM.pdf]
Test-time Boosting In the absence of training labels, our algorithm can be adapted to the transductive ... In this case, we substitute ground truth answer labels with model predictions, using a similar motivation as (Huang et al., 2022), whereby predictions with “sufficient ...

[Chunk 2 | Source: Silviu_2023_BoostedPromptEnsemblesforLLM.pdf]
... The output of our train-time algorithm is a set of prompts, which are then applied to the test set. The output of our test-time algorithm is a set of prompts together with a set of test predictions. Train-time Boosting In this case, we assume access to a small labeled dataset ...

[Chunk 3 | Source: Silviu_2023_BoostedPromptEnsemblesforLLM.pdf]
How we determine correctness depends on the setting ... test-time boosting, for the case where no supervision is available and the model must rely solely on its own predictions.

## QID: 28

My prompt worked on a few examples. Why does the paper still say that may not mean the prototype will work well in real use?

[Judgement]
- Retrieval: fail
- Generation: fail
- Failure Type: Retrieval failure

[Reason]
The retrieval fails because it does not bring back the target paper or the required evidence about prototype evaluation in authentic environments. Instead, it returns more general material about prompt robustness and prompt engineering from other papers. Although the answer talks broadly about real-world performance and generalization, it does not ground itself in the paper’s actual point that success on a few examples may not generalize and that broader or more authentic evaluation is needed. Under the benchmark rubric, this should be treated primarily as a retrieval failure.
---

[Gold Reference]
- Core Evidence (text or summary): “successes on a few example inputs may not generalize to behavior in authentic environments,” so working on a few examples does not guarantee the prototype will behave well in real use.
- Min Acceptable Answer: Says a few examples are not enough because the prototype may not generalize to authentic environments, and mentions the need for broader / more realistic evaluation.
- Critical Error: Treats a few good examples as sufficient proof that the prototype works in real use; gives only generic “test more” advice without the paper’s generalization point.
- Pass Rule:
  - Retrieval: Retrieve at least two evidence units needed to explain or connect the ideas involved in why a prototype that works on a few examples may still fail in real use.
  - Generation: faithfully uses evidence and completes the required integration/comparison

---

[Model Output]
- Generated Answer: The paper suggests that even if your prompt works on a few examples, it doesn't necessarily mean it will perform well in real-world scenarios for several reasons:

1. Semantic changes and performance degradation: minor alterations in format, without changing the meaning, can lead to substantial performance degradation.
2. Prompt engineering's limitations: it can require expertise and time to design optimal prompts.
3. Lack of real user queries in benchmarks: controlled evaluations may not reflect real usage.
4. Automation challenges: automatic prompt engineering may require labeled data and still miss nuanced interactions.

In summary, while your prompt may work well in specific examples, real-world performance depends on various factors including context-specific nuances, evaluation limitations, and automation challenges.
- Retrieved Chunks: [Chunk 1 | Source: BowenCao_2024_WorstPromptPerformanceofLLM.pdf]
... Even minor alterations in format, without semantic changes, can trigger substantial performance degradation ...

[Chunk 2 | Source: BowenCao_2024_WorstPromptPerformanceofLLM.pdf]
Figure 1: An example illustrating the gap between existing benchmarks that evaluate prompt consistency and real user queries. Despite the efficacy of prompt engineering, it is not without its drawbacks ...

[Chunk 3 | Source: YongchaoZhou_2023_LLMPrompt.pdf]
... natural language prompt engineering ... provides a natural interface for humans to communicate with machines ...

## QID: 29

Does the paper say how long APE takes to run end to end?

[Judgement]
- Retrieval: fail
- Generation: fail
- Failure Type: Retrieval failure

[Reason]
This D1 item asks whether the paper reports end-to-end runtime, so retrieval must surface the closest scope evidence that discusses APE’s pipeline or computation-related details and thereby supports a grounded “not reported” judgment. Although the retrieved chunks come from the correct paper, they mainly discuss task performance, search behavior, and related metadata rather than the relevant scope passages about search cost or efficiency. Because the boundary judgment is not supported by the right evidence, retrieval should fail. The generated answer also fails under the D-class rubric: it reaches the correct “no runtime reported” conclusion, but does so by relying on loosely related content and even mentions irrelevant metadata, rather than grounding the abstention in proper boundary evidence.
---

[Gold Reference]
- Core Evidence (text or summary): Closest relevant scope evidence only. The paper says APE searches over instruction candidates and evaluates them with a score function, then discusses an adaptive filtering scheme to reduce computation cost. However, these passages do not give an end-to-end wall-clock runtime or total duration for running APE. So this is a D1 no-evidence item.
- Min Acceptable Answer: States that the paper does not say how long APE takes to run end to end.
- Critical Error: Invents a runtime / latency / GPU-hour figure, or turns sample-size / computation-efficiency details into an explicit runtime claim.
- Pass Rule:
  - Retrieval: Retrieve the APE pipeline and efficient-score-estimation passages and verify that they describe search and efficiency, but do not report end-to-end runtime.
  - Generation: Explicitly says no runtime is reported and does not infer one from nearby compute-efficiency details.

---

[Model Output]
- Generated Answer: The provided context does not contain information about the time it takes for APE to run end-to-end. The details mentioned are related to the version of pdfTeX used, LaTeX with hyperref creator, creation date, metadata labels such as author, keywords, and page content discussing the performance of InstructGPT, "Greedy" algorithm, survival plot, iterative search, comparison between APE and iterative APE, and an alternative CoT (Chain of Thought) prompt for APE. However, there is no mention of execution time or computational duration associated with running APE.
- Retrieved Chunks: [Chunk 1 | Source: YongchaoZhou_2023_LLMPrompt.pdf]
algorithm can be thought of as a greedy version of APE, without a search and selection process;
thus, we refer to it as “Greedy”. Figure 4 shows the zero-shot performance of InstructGPT using
human instructions and model generated instructions. Our algorithm outperforms “Greedy” on
every task and achieves equal or better than human performance on 24 of 24 tasks. Moreover, the
Interquartile Mean (IQM) (Agarwal et al., 2021) across all 24 tasks in Figure 1 suggests that APE with

------------------------

[Chunk 2 | Source: YongchaoZhou_2023_LLMPrompt.pdf]
tasks in the Appendix. The survival plot shows that the curves increase as the round goes up, which
suggests that iterative search does result in a higher-quality proposal set. However, we observe
diminishing returns to further selection rounds as the quality seems to stabilize after three rounds.
Do we need Iterative Search? We compare APE and iterative APE on six tasks6. As shown in
Figure 7, the iterative search marginally improves performance on tasks where APE underperforms

------------------------

[Chunk 3 | Source: YongchaoZhou_2023_LLMPrompt.pdf]
compared to the original CoT prompt. We include full results on 12 tasks with this new APE CoT
prompt in Figure 10.
Figure 10: The performance of APE discovered prompt "Let’s work this out in a step by step way
to be sure we have the right answer." on the 12 tasks from Kojima et al. (2022). We collect a CoT
dataset from the original paper and filter out incorrect answers. We then use APE to optimize the CoT
prompt. We improve performance on 6/12 tasks and nearly match human performance on 4/12 tasks.


## QID: 30

Does the case study say what it cost in dollars to run PromptMaker?

[Judgement]
- Retrieval: fail
- Generation: fail
- Failure Type: Retrieval failure

[Reason]
The retriever misses the PromptMaker case-study paper and instead returns unrelated material about general prompting cost, prompt optimization runtime, and prompt engineering surveys. Although the generated answer abstains, that abstention is not grounded in the target source or its case-study evidence. Under the current annotation, this is primarily a retrieval failure.
---

[Gold Reference]
- Core Evidence (text or summary): Closest relevant scope evidence only. The paper describes PromptMaker as a prompt-based prototyping tool, notes that it uses a 137B-parameter language model, and reports qualitative benefits like faster prototyping. But it does not provide any dollar cost, API pricing, or compute-cost figure for running PromptMaker. So this is a D1 no-evidence item.
- Min Acceptable Answer: States that the paper does not give the dollar cost of running PromptMaker.
- Critical Error: Invents a dollar/API cost, or extrapolates one from model size or qualitative time-savings anecdotes.
- Pass Rule:
  - Retrieval: Retrieve the abstract, tool-description, and time-savings passages and verify that they discuss prototyping workflow and the underlying model, but not financial cost.
  - Generation: Explicitly says no dollar/API cost is reported and does not infer pricing from model size or anecdotal speedup.

---

[Model Output]
- Generated Answer: No, the context does not provide information about the cost of running PromptMaker or any specific tool related to prompt engineering. The documents discuss costs associated with certain models like GPT-4 and mention that prompt optimization can be a priority for cost-effectiveness in commercial applications, but they do not specify the cost of running PromptMaker.
- Retrieved Chunks: [Chunk 1 | Source: AndrewKeanGao_2023_PromptEngineeringforLLM.pdf]
cost. For example, few-shot prompting canmultiply the length of prompts by several times, leading to higher costs. OpenAI’s GPT-4 model costs$0.03 USD per 1,000 input tokens which can quickly add up. In commercial applications likeLLM-powered educational technology, streamlining prompts to be as cost-effective as possiblemaybeapriority. It seems that prompting becomes less important as LLMs become more advanced (moreparameters, more training data). It is not clear if this trend will continue indefinitelyor

------------------------

[Chunk 2 | Source: AntonioSabbatella_2024_PromptOptimization.pdf]
Task PrompT-BO BDPL
MRPC 379.02 571.75
RTE 661.92 1081.62
QQP 669.52 1070.14
MNLI 896.61 1614.33
QNL 398.96 587.87
SST-2 264.23 384.84
Runtime is an important metric to consider, especially with respect to the societal
impact of LLMs and their prompt tuning. Indeed, PrompT-BO, like all other methods,
might enable negative applications due to incorrect results in critical decision-making
instances. It is therefore important that its implementation comply with ethical safety

------------------------

[Chunk 3 | Source: BowenCao_2024_WorstPromptPerformanceofLLM.pdf]
Figure 1: An example illustrating the gap between existing benchmarks that evaluate prompt consis-
tency and real user queries.
Despite the efficacy of prompt engineering, it is not without its drawbacks. First, it is unrealistic to
expect users to master the art of designing optimal prompts or to invest a significant amount of time
in doing so. Second, automatic prompt engineering often necessitates testing on substantial labeled


## QID: 31

Does the paper provide enough evidence to say that few-shot examples help mainly by locating or formatting the task, rather than by teaching the model the translation task itself?

[Judgement]
- Retrieval: fail
- Generation: fail
- Failure Type: Retrieval failure

[Reason]
The retrieved material does not reach the target source or the specific discussion needed to support this evidence-limited judgment. The generated answer does maintain that the evidence is insufficient, but it does so from loosely related or wrong-source material rather than from the paper’s actual argument about task location, semantic contamination, and the limits of the stronger conclusion. Under the current annotation, the main issue is retrieval failure.
---

[Gold Reference]
- Core Evidence (text or summary): The paper’s core framing is that few-shot prompting often serves task location rather than runtime task learning. It also argues that direct task specification can call functions the model has already learned, and that few-shot examples are processed as a whole rather than necessarily as parallel independent teaching signals. In the translation discussion, the paper reports that a 1-shot version of the simple colon prompt performed worse than 0-shot and attributes this to semantic contamination. Together, these passages support a cautious boundary: the paper gives real support for task-location / formatting-style effects and for semantic interference, but it does not isolate these factors enough to justify the stronger conclusion that the benefit comes mainly from locating or formatting the task rather than teaching it.
- Min Acceptable Answer: Says the evidence is insufficient for that strong “mainly formatting rather than semantic content” conclusion, even though related discussion exists.
- Critical Error: States the strong conclusion as established; says the paper cleanly proves formatting rather than semantics is the main cause.
- Pass Rule:
  - Retrieval: Retrieve the related discussion around whether the paper justifies the conclusion that format-only few-shot examples improve translation quality and show that it stops short of supporting the asked conclusion.
  - Generation: explicitly states evidence is insufficient and does not overclaim

---

[Model Output]
- Generated Answer: The provided context does not contain enough information to definitively conclude whether few-shot examples help mainly by locating or formatting the task versus teaching the model the translation task itself. The documents discuss aspects of few-shot prompting and its impact on model performance, but they do not explicitly compare these two hypotheses in detail. To make such a conclusion, one would need more specific evidence from the paper that directly addresses how few-shot examples are utilized and their primary function within the context of task understanding or translation learning.
- Retrieved Chunks: [Chunk 1 | Source: PranabSahoo_2024_promptEngineering.pdf]
Few-shot prompting provides models with a few input-output
examples to induce an understanding of a given task, unlike
zero-shot prompting, where no examples are supplied [Brown
et al. , 2020]. Providing even a few high-quality examples
has improved model performance on complex tasks compared
to no demonstration. However, few-shot prompting requires
additional tokens to include the examples, which may become
prohibitive for longer text inputs. Moreover, the selection

------------------------

[Chunk 2 | Source: YongchaoZhou_2023_LLMPrompt.pdf]
Tianyu Gao, Adam Fisch, and Danqi Chen. Making pre-trained language models better few-shot
learners. In Proceedings of the 59th Annual Meeting of the Association for Computational Linguis-
tics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long
Papers), pp. 3816–3830, Online, August 2021. Association for Computational Linguistics. doi:
10.18653/v1/2021.acl-long.295. URL https://aclanthology.org/2021.acl-long.
295.

------------------------

[Chunk 3 | Source: YongchaoZhou_2023_LLMPrompt.pdf]
In-context” in Figure 8. As shown in Figure 8, adding an instruction achieves a comparable or better
test performance than the standard in-context learning performance on 21 of 24 tasks. Counter-
intuitively, adding in-context examples for Rhymes, Large Animal, and Second Letters hurts model
performance. We conjecture that it may be because the selected instructions overfit the zero-shot
learning scenario and thus do not perform well on the few-shot case. Therefore, we experiment


## QID: 32

Does the paper provide sufficient evidence to conclude that boosted prompt ensembles are always better than the single-prompt baselines evaluated in the paper?

[Judgement]
- Retrieval: pass
- Generation: fail
- Failure Type: Generation failure

[Reason]
The retrieved evidence reaches the correct paper and includes the relevant comparison results, but those results only support conditional gains in reported settings rather than a universal “always better” claim. The generated answer overstates the evidence by treating setting-dependent superiority as if it were sufficient for a stronger general conclusion. This is therefore a generation-side overclaim on top of sufficient retrieval.
---

[Gold Reference]
- Core Evidence (text or summary): The paper reports that boosted prompt ensembles outperform single-prompt and bagged ensembles in the reported settings, especially when a small training dataset is available and when the initial prompt is suboptimal. This supports conditional gains for the reported regimes rather than a universal “always better” claim.
- Min Acceptable Answer: Says the paper shows setting-dependent gains but not enough to justify an “always better” conclusion.
- Critical Error: Upgrades conditional results into universal superiority; ignores reported limitations, exceptions, or setting dependence.
- Pass Rule:
  - Retrieval: Retrieve the relevant comparison results and verify that they do not support the universal "always better" conclusion.
  - Generation: explicitly states evidence is insufficient and does not overclaim

---

[Model Output]
- Generated Answer: Yes, based on the context provided, the paper suggests that when a small training dataset (50-300 samples) is available, boosted prompt ensembles are superior to randomly bagging few-shot examples as well as to single-prompt self-consistency. The difference can be quite large if the initial prompt is suboptimal. This indicates that the paper provides sufficient evidence to conclude that boosted prompt ensembles offer a performance advantage over single prompt and bagged ensembles under certain conditions.
- Retrieved Chunks: [Chunk 1 | Source: Silviu_2023_BoostedPromptEnsemblesforLLM.pdf]
single prompt samples for self-consistency, and for bagging
and boosting, 10 samples from each of 10 prompts.
Do boosted prompt ensembles offer a performance ad-
vantage over single prompt and bagged ensembles?
Yes, in all cases, when a small training dataset (50-300
samples) is available, we ﬁnd that boosting is superior to
randomly bagging few shot examples as well as to single-
prompt self-consistency. The difference to the latter can be
quite large if the initial prompt is suboptimal, as observed

------------------------

[Chunk 2 | Source: Silviu_2023_BoostedPromptEnsemblesforLLM.pdf]
This can then lead to a decrease in test-time performance, as
the boosted prompts may contain more incorrect examples.
Can we further improve performance by applying
weights to the ensemble members?
Classical boosting applies weights to the ensemble members
(Freund et al., 1999). Though lacking in mathematical mo-
tivation, we consider applying weights to boosted prompt
ensembles via the K-class Adaboost formula from Hastie
et al. (2009):
wi = log [(1− erri)/erri] + log(K− 1)

------------------------

[Chunk 3 | Source: Silviu_2023_BoostedPromptEnsemblesforLLM.pdf]
derstandable, because boosted prompting uses the model to
provide self supervised chains of thought for all subsequent
ensemble members and a worse initial prompt means worse
self supervision. The performance of the original prompt is
also a direct factor since we keep the original prompt as one
of the ten ensemble members.
How does varying the number of ensemble members /
samples per ensemble member impact results?
In Table 2, we report results on AQUA where we vary the


## QID: 33

If a newer model not tested in this paper came out today, could we use this paper alone to know which prompt would be its worst-performing paraphrase?

[Judgement]
- Retrieval: pass
- Generation: fail
- Failure Type: Generation failure

[Reason]
This is a D3 external-only item. The retrieved evidence is sufficient because it reaches the correct paper and supports the key boundary: worst prompts are model-specific, prompt rankings differ across models, and the paper does not provide a reusable rule for an unseen newer model. Retrieval therefore passes. However, generation should fail under the D-class rubric. The model answers “No,” which is the right surface conclusion, but its justification is wrong: it claims the context does not include information about the experiments in the paper, even though the retrieved evidence does include relevant experimental and model-specificity discussion. The answer does not clearly state the real boundary—that this question requires external testing or evidence for a newer untested model—so it fails as boundary handling even though the final yes/no stance is correct.
---

[Gold Reference]
- Core Evidence (text or summary): The paper explicitly argues that worst prompts are not universally applicable across models and that prompt rankings differ across models. This means the paper does not provide a reusable rule that would let us infer the worst-performing paraphrase for a newer model outside the evaluated set. Therefore, for an unseen newer model, the question is external-only rather than merely insufficiently supported within the current corpus.
- Min Acceptable Answer: States that the paper alone is not enough for an unseen newer model, and that answering this would require external evidence or direct testing on that model.
- Critical Error: Names or infers a specific worst-performing paraphrase for the newer model from this paper alone; treats model-specific findings as if they directly determine the worst prompt for an unseen model.
- Pass Rule:
  - Retrieval: Retrieve evidence that worst prompts are model-specific / not universally shared across models, plus evidence that prompt features do not reliably forecast performance for unseen cases.
  - Generation: Explicitly says this is external-only for a newer untested model, refuses to infer a specific worst paraphrase from the paper alone, and points to the need for external testing or additional evidence.

---

[Model Output]
- Generated Answer: No

Justification: The context provided does not include information about the experiments conducted in the paper. Therefore, it is not possible to determine if the paper includes enough data or analysis to predict how a newer model might perform on specific prompts based solely on its findings. The guidelines mentioned state that an answer of "Yes" would imply that the paper includes experiments and provides sufficient evidence for such predictions, which cannot be confirmed with the given information.
- Retrieved Chunks: [Chunk 1 | Source: BowenCao_2024_WorstPromptPerformanceofLLM.pdf]
4 Identifying the Worst Prompts
Given the noticeable performance disparities across semantically equivalent prompts, our next
question is: can we identify the worst prompt among these paraphrases? This would not only aid our
understanding of the model’s lower bound but also be instrumental in improving model performance
by guiding the refinement of prompts. We investigate this matter from both model-agnostic (§4.1)
and model-dependent (§4.2) perspectives.
4.1 Model-agnostic Analysis

------------------------

[Chunk 2 | Source: BowenCao_2024_WorstPromptPerformanceofLLM.pdf]
of the paper (regardless of whether the code and data are provided or not)?
Answer: [Yes]
Justification: In Section 3 (Benchmarking the Worst Prompt Performance), 4 (Identifying
the Worst Prompts) and 5 (Improving Worst Prompt Performance).
Guidelines:
• The answer NA means that the paper does not include experiments.
• If the paper includes experiments, a No answer to this question will not be perceived
well by the reviewers: Making the paper reproducible is important, regardless of

------------------------

[Chunk 3 | Source: BowenCao_2024_WorstPromptPerformanceofLLM.pdf]
Overlap of the worst prompts across different
models. If many of the worst prompts are model-
agnostic, there must exist certain prompts that,
among their semantically equivalent paraphrases,
consistently rank as the worst performing across
all models. To quantify the prevalence of such
prompts, we calculate the rate of the model-agnostic
worst-k prompt. Let Wm(x, k) denote the worst-k-
performing prompts for model m on case x, and let
the set of worst- k prompts for model m on dataset
D be Wm(D, k) = S


## QID: 34

Based on this paper alone, can we tell whether prompt-based prototyping would replace specialized ML pipelines in real production teams today?

[Judgement]
- Retrieval: fail
- Generation: fail
- Failure Type: Retrieval failure

[Reason]
The retriever does not hit the target prototyping paper and fails to surface the evidence about prototyping scope, alternative ML paths, and authentic-environment limits. The generated answer abstains in a broadly plausible way, but it does so from unrelated prompt-engineering material rather than the source paper’s actual production-boundary discussion. Under the current annotation, this is primarily a retrieval failure.
---

[Gold Reference]
- Core Evidence (text or summary): The paper frames prompt-based prototyping as a way to lower barriers, speed up prototyping, and help teams explore and de-risk ML ideas earlier. But it also explicitly says that the inability to produce an effective prompt does not mean a model cannot eventually be built with alternative methods such as training a specialized model or prompt-tuning. This means the paper does not provide a basis for deciding whether prompt-based prototyping would replace specialized ML pipelines in real production teams today.
- Min Acceptable Answer: States that the paper is about prototyping rather than production replacement, and that answering the real-production-today question would require external deployment evidence.
- Critical Error: Treats prototyping success as evidence of present-day production replacement; claims the paper supports replacing specialized ML pipelines in real production teams.
- Pass Rule:
  - Retrieval: Retrieve evidence that prompt programming lowers barriers for prototyping, that prompt failure does not rule out alternative ML methods, and that successes on a few inputs may not generalize to authentic environments.
  - Generation: Explicitly says the paper alone is not enough to decide present-day production replacement, keeps the claim at the prototyping level, and marks the production judgment as requiring external evidence.

---

[Model Output]
- Generated Answer: Based on the provided context from these documents, there is no information that directly addresses whether prompt-based prototyping would replace specialized Machine Learning (ML) pipelines in real production teams today. The documents discuss various aspects of prompt engineering and its significance in guiding model outputs without altering parameters, as well as the potential for minor format changes to trigger substantial performance degradation in large language models. However, they do not provide a clear stance or conclusion on whether prompt-based methods could replace traditional ML pipelines in practical applications.
- Retrieved Chunks: [Chunk 1 | Source: PranabSahoo_2024_promptEngineering.pdf]
is often required for task-specific performance. This is the
transformative promise of prompt engineering, pushing the
boundaries of AI and opening doors to a future brimming with
possibilities. In an ever-evolving landscape, ongoing research
consistently reveals innovative approaches and applications
within prompt engineering. The significance of prompt engi-
neering is underscored by its capacity to steer model responses,
enhancing the adaptability and applicability of LLMs across

------------------------

[Chunk 2 | Source: BowenCao_2024_WorstPromptPerformanceofLLM.pdf]
Sun et al., 2023; Li et al., 2024). Even minor alterations in format, without semantic changes, can
trigger substantial performance degradation (Sclar et al., 2023). Consequently, prompt engineering
has surfaced as a critical component, playing a critical role in unlocking the full potential of these
models (Shin et al., 2020; Zhou et al., 2022a; Pryzant et al., 2023; Prasad et al., 2023; Gonen et al.,
2022; Schulhoff et al., 2024).

------------------------

[Chunk 3 | Source: PranabSahoo_2024_promptEngineering.pdf]
strategically designing task-specific instructions, referred to
as prompts, to guide model output without altering param-
eters. The significance of prompt engineering is especially
∗Work does not relate to position at Amazon.
Prompt Engineering
Instruction 
User's Input
LLM
Pre-trained on
billions of
parameters
Output: Response
 generated by LLMContext
Figure 1: Visual breakdown of prompt engineering components:
LLMs trained on extensive data, instruction and context as pivotal


## QID: 35

Since few-shot examples teach the task at runtime, does the paper conclude that adding more examples is always safer than zero-shot prompting?

[Judgement]
- Retrieval: fail
- Generation: fail
- Failure Type: Retrieval failure

[Reason]
The retriever does not reach the target paper’s premise-correction evidence about few-shot not necessarily teaching the task at runtime and about examples sometimes hurting performance. The generated answer ultimately rejects the “always safer” claim, but it does so using generic few-shot/zero-shot discussion rather than the intended source evidence. Under the current annotation, the main problem is retrieval failure rather than generation behavior.
---

[Gold Reference]
- Core Evidence (text or summary): “GPT-3 is often not actually learning the task during run time from few-shot examples.” “Rather than learning how to perform the task from the examples, the examples may simply serve to instruct GPT-3 on what task it is to solve ...”
- Min Acceptable Answer: Corrects the premise and says zero-shot can match or beat few-shot, or that more examples are not automatically safer.
- Critical Error: Accepts the premise that more examples are always safer or better; answers as if the paper endorses runtime teaching without correction.
- Pass Rule:
  - Retrieval: Retrieve the relevant discussion of zero-shot vs few-shot and correct the false premise that more examples are always safer.
  - Generation: corrects the false premise before answering, or states it cannot be established

---

[Model Output]
- Generated Answer: The context provided does not explicitly state whether the paper concludes that adding more examples in few-shot prompting is always safer than zero-shot prompting. The documents discuss the differences between few-shot and zero-shot prompting but do not provide a definitive conclusion on which method is safer or more effective under all circumstances. The papers mention that providing even a few high-quality examples has improved model performance on complex tasks compared to no demonstration, but they also note that for longer text inputs, including examples in few-shot prompting may become prohibitive. Additionally, the context suggests that there might be scenarios where adding in-context examples can hurt model performance, particularly if the instructions overfit the zero-shot learning scenario and do not perform well on the few-shot case. Therefore, based on the information provided, it cannot be concluded that adding more examples is always safer than zero-shot prompting; rather, the effectiveness depends on various factors including task complexity, input length, and how well the examples align with the specific requirements of the task at hand.
- Retrieved Chunks: [Chunk 1 | Source: PranabSahoo_2024_promptEngineering.pdf]
Few-shot prompting provides models with a few input-output
examples to induce an understanding of a given task, unlike
zero-shot prompting, where no examples are supplied [Brown
et al. , 2020]. Providing even a few high-quality examples
has improved model performance on complex tasks compared
to no demonstration. However, few-shot prompting requires
additional tokens to include the examples, which may become
prohibitive for longer text inputs. Moreover, the selection

------------------------

[Chunk 2 | Source: Shubham_2024_EngineeringMethodsForLLM.pdf]
either zero-shot or few-shot variation and there may not be a possibility for any other variation to exist. In
zero-shot Radford et al. (2019) setting, there is no trainin g data involved and an LLM is asked to perform
a task through prompt instructions while completely relyin g on it’s embedded knowledge learnt during it’s
pre-training phase. On the other hand, in few-shot variatio n Brown et al. (2020), few training datapoints are

------------------------

[Chunk 3 | Source: YongchaoZhou_2023_LLMPrompt.pdf]
test performance than the standard in-context learning performance on 21 of 24 tasks. Counter-
intuitively, adding in-context examples for Rhymes, Large Animal, and Second Letters hurts model
performance. We conjecture that it may be because the selected instructions overfit the zero-shot
learning scenario and thus do not perform well on the few-shot case. Therefore, we experiment
using few-shot execution accuracy as the selection metric. Figure 14 shows that the few-shot metric


## QID: 36

Since RLPG uses repository-level context, does the paper show that repository context alone is always sufficient, even without outside API documentation?

[Judgement]
- Retrieval: pass
- Generation: pass
- Failure Type: None

[Reason]
The retrieved evidence reaches the correct RLPG paper and is sufficient to correct the false premise. It supports that repository-level context is useful, but not always sufficient on its own, and explicitly allows for additional relevant sources such as API documentation, tutorials, or related repositories. The answer properly corrects the premise instead of accepting repository-only sufficiency.
---

[Gold Reference]
- Core Evidence (text or summary): No. The paper does not show that repository context alone is always sufficient. It explicitly notes that, beyond the current repository, other relevant sources such as “API documentation, tutorials, or related repositories” can aid code autocompletion, and says RLPG can incorporate these through new prompt proposals.
- Min Acceptable Answer: Must correct the “repository context alone is always sufficient” premise and mention that relevant external sources may also matter.
- Critical Error: Accepts the repository-only sufficiency premise; omits the paper’s explicit allowance for external context sources.
- Pass Rule:
  - Retrieval: Retrieve the related discussion on repository-level context and the boundary that relevant information may exist outside the repository, then correct the false premise.
  - Generation: corrects the false premise before answering, or states it cannot be established

---

[Model Output]
- Generated Answer: No, the paper does not suggest that repository context alone is always sufficient for RLPG. It mentions that while repositories can be very large and contain a lot of relevant information (with 70.22% of repositories having more than 32k tokens), there are other sources of relevant context beyond just the current repository. These include API documentation, tutorials, and related repositories, which can also aid in code autocompletion. RLPG offers a mechanism to incorporate these additional sources of context through new prompt proposals.
- Retrieved Chunks: [Chunk 1 | Source: Disha_2023_Repository-LevelPromptGenerationforLLM.pdf]
repository as well as the relevant context in the files in the
repository. In RLPG, the choice of where from and what
to take from the repository is specified by a set of prompt
proposals. For example, one of the prompt proposals can be
1https://copilot.github.com/
1

------------------------

[Chunk 2 | Source: Disha_2023_Repository-LevelPromptGenerationforLLM.pdf]
In this section, we provide details of our framework. We
start by describing our prompt proposals and then discuss
our prompt proposal classifier which is followed by a de-
scription of the prompt composer.
2.1. Repo-Level Prompt Proposals
The core idea of RLPG consists of substituting part of the de-
fault context used by Codex with context coming from some-
where else in the repository. The decision of what to take
and from where in the repository to take from is governed

------------------------

[Chunk 3 | Source: Disha_2023_Repository-LevelPromptGenerationforLLM.pdf]
software repositories are often much longer. In our dataset
(after deduplication), we observed that 70.22% of reposito-
ries contain more than 32k tokens. It is worth noting that
apart from the current repository, there are other sources
of relevant context, such as API documentation, tutorials,
or related repositories, that can aid in code autocompletion.
RLPG offers a mechanism to incorporate these additional
sources of context through new prompt proposals. There-
