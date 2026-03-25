# Lightweight RAG System for Academic Papers

本项目用于构建一个轻量级的**检索增强生成（RAG）系统**，能够基于本地PDF论文语料回答用户问题。  
当前模块包含两部分：一是**PDF语料的预处理**（从原始PDF中提取文本、清洗并生成结构化文件），二是**RAG 基准测试推理**（利用向量检索和大模型批量生成格式化的评测数据）。

---
## 交互APP

https://github.com/user-attachments/assets/84746155-0e44-4057-b0fa-2c0b06cd2265

## 环境配置

### 1. Python 版本要求
建议使用 **Python 3.10 或 3.11**（PyMuPDF 等库对 Python 3.14 尚不支持）。可通过以下命令检查当前版本：
```bash
python --version
```

### 2. 创建虚拟环境
激活虚拟环境

```bash
rag_env\Scripts\activate
```

### 3. 安装依赖
预处理与文本解析依赖：
```bash
pip install pymupdf pandas tqdm
pip install pdf2image pytesseract
```
RAG 检索与推理依赖：
```bash
pip install langchain langchain-community langchain-text-splitters pypdf
pip install sentence-transformers faiss-cpu torch transformers openpyxl
```
app 依赖：
```bash
pip install streamlit
```
### 4. 本地大模型准备 

在 Task 2 生成回答时，依赖本地运行的大语言模型。代码中使用的是 `Ollama` 接口（调用 `qwen2:7b`）：
1. 请前往 [Ollama 官网](https://ollama.com/) 下载并安装 Ollama 客户端。
2. 打开终端，拉取并运行对应的模型（首次运行会自动下载）：
   ```bash
   ollama run qwen2:7b
   ```

## 数据准备

### 1. PDF 存放位置
将所有待处理的 PDF 文件放入 data/papers/raw/ 文件夹。如果文件夹不存在，请手动创建：
```bash
Lightweight-RAG-System-for-Academic-Papers/
└── data/
    └── papers/
        └── raw/          # 存放原始 PDF
```

为了自动提取作者、年份和标题信息，建议按以下格式命名：
```bash
FirstAuthor_Year_Title.pdf
```

### 2. 评测题库准备
在执行批量 RAG 推理前，请确保评测问题表已就绪：
```bash
evaluation/benchmarking_question.xlsx
```

## 运行脚本

### Task 1: 运行预处理脚本
基本用法（纯文本PDF）：
```bash
python process_pdfs.py --pdf_dir ./data/papers/raw --out_dir ./data/papers/processed --meta_out ./
```

启用 OCR（处理扫描版PDF）：
```bash
python process_pdfs.py --pdf_dir ./data/papers/raw --out_dir ./data/papers/processed --meta_out ./ --use_ocr
```

### Task 2: 运行 RAG 批量推理
该步骤会构建 FAISS 向量库，并根据 `benchmarking_question.xlsx` 批量生成大模型的回答及检索到的证据（Context）。

运行对应的 Jupyter Notebook， 即retrieval_main_chain.ipynb。

### Task 4: Demo与可视化交互app
① demo.py为任务1与任务2的合并文档。
```bash
python demo.py
```
② app.py为可视化交互app前端，backend.py由demo.py删减得到的交互app后端。只运行app.py即可，运行方式如下：
```bash
streamlit run app.py
```

## 输出说明

### 1. JSON 文件
保存在 `--out_dir`（默认 `data/papers/processed/`），文件名为 `{file_id}.json`，内容示例：
```json
{
  "file_id": "Smith_2023_RetrievalAugmentedLLM",
  "file_name": "Smith_2023_RetrievalAugmentedLLM.pdf",
  "title": "Retrieval-Augmented Large Language Models",
  "authors": "John Smith;Jane Doe",
  "year": "2023",
  "source": "",
  "abstract": "",
  "keywords": "",
  "text": "全文清洗后的文本..."
}
```

### 2. 元数据 CSV 
生成 `paper_metadata.csv` 在 `--meta_out` 指定目录（默认当前目录），包含字段：

* file_name：PDF 文件名
* title：论文标题
* authors：作者列表
* year：发表年份
* source：来源（如期刊/会议，可手动填写）
* abstract：摘要（可后续补充）
* keywords：关键词
* path_to_text：对应 JSON 文件的相对路径

### 3. RAG 评测结果 CSV 
生成 `rag_benchmark_output.csv` 在项目根目录，这是后续进行 LLM-as-a-judge 打分的核心文件。包含以下关键字段：

* Target_Doc_IDs：问题对应的标准答案来源文档ID
* Generated_Answer：大语言模型基于检索内容生成的回答
* Retrieved_Context：实际喂给大模型的检索文本块（用于判定 Retrieval failure）
* Retrieved_Sources：检索出的文本块来源列表
