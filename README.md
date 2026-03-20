# Lightweight RAG System for Academic Papers

本项目用于构建一个轻量级的**检索增强生成（RAG）系统**，能够基于本地PDF论文语料回答用户问题。  
当前模块负责**PDF语料的预处理**：从原始PDF中提取文本、清洗、保留元数据，并生成结构化的JSON文件和元数据CSV，供后续的向量数据库构建和检索使用。

---

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
```bash
pip install pymupdf pandas tqdm
pip install pdf2image pytesseract
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

### 1. PDF 存放位置
为了自动提取作者、年份和标题信息，建议按以下格式命名：
```bash
FirstAuthor_Year_Title.pdf
```

## 运行预处理脚本
### 基本用法（纯文本PDF）
```bash
python process_pdfs.py --pdf_dir ./data/papers/raw --out_dir ./data/papers/processed --meta_out ./
```

### 启用 OCR（处理扫描版PDF）
```bash
python process_pdfs.py --pdf_dir ./data/papers/raw --out_dir ./data/papers/processed --meta_out ./ --use_ocr
```

## 输出说明

### 1. JSON 文件（每个 PDF 对应一个）
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
生成 paper_metadata.csv 在 --meta_out 指定目录（默认当前目录），包含字段：

file_name：PDF 文件名

title：论文标题

authors：作者列表

year：发表年份

source：来源（如期刊/会议，可手动填写）

abstract：摘要（可后续补充）

keywords：关键词

path_to_text：对应 JSON 文件的相对路径
