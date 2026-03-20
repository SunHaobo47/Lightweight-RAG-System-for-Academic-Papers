#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PDF论文处理脚本（支持OCR）
用法：
    python process_pdfs_ocr.py --pdf_dir ./data/papers/raw --out_dir ./data/papers/processed --meta_out ./ --use_ocr
"""

import os
import re
import json
import argparse
from typing import Dict, List, Optional

import fitz  # PyMuPDF
import pandas as pd
from tqdm import tqdm

# OCR 相关（如果未安装，则跳过）
try:
    from pdf2image import convert_from_path
    import pytesseract

    OCR_AVAILABLE = True
except ImportError:
    OCR_AVAILABLE = False
    print("警告：未安装 pdf2image 或 pytesseract，OCR功能不可用。如需使用，请安装：pip install pdf2image pytesseract")


def extract_metadata_from_filename(filename: str) -> Dict[str, str]:
    """从文件名解析基本信息（假设格式：FirstAuthor_Year_Title.pdf）"""
    base = os.path.splitext(filename)[0]
    parts = base.split('_')
    if len(parts) >= 2:
        author = parts[0]
        year = parts[1] if parts[1].isdigit() else ""
        title = ' '.join(parts[2:]) if len(parts) > 2 else ""
    else:
        author, year, title = "", "", base
    return {
        "file_name": filename,
        "authors": author,
        "year": year,
        "title": title
    }


def extract_text_with_pymupdf(pdf_path: str) -> str:
    """使用PyMuPDF提取文本"""
    doc = fitz.open(pdf_path)
    full_text = []
    for page in doc:
        text = page.get_text()
        full_text.append(text)
    doc.close()
    return "\n".join(full_text)


def extract_text_with_ocr(pdf_path: str) -> str:
    """使用OCR提取文本（将PDF页面转为图像后识别）"""
    if not OCR_AVAILABLE:
        raise RuntimeError("OCR库未安装，无法执行OCR。")
    images = convert_from_path(pdf_path)
    ocr_text = []
    for img in images:
        text = pytesseract.image_to_string(img, lang='eng')  # 可根据需要修改语言
        ocr_text.append(text)
    return "\n".join(ocr_text)


def clean_text(text: str) -> str:
    """
    清洗文本：
    1. 移除类似 text[[85,799,480,862]] 的坐标标记
    2. 处理连字符断行
    3. 合并多余空格/换行
    """
    # 移除坐标标记（如 text[[...]] 或 text[[...], [...]]）
    text = re.sub(r'text\[\[.*?\]\]', '', text, flags=re.DOTALL)
    # 处理连字符断行
    text = re.sub(r'(\w+)-\n(\w+)', r'\1\2', text)
    # 将单个换行（非段落分隔）替换为空格
    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)
    # 合并多个空格/空行
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n\s*\n', '\n\n', text)
    return text.strip()


def process_pdf(pdf_path: str, use_ocr: bool = False) -> Dict[str, any]:
    """
    处理单个PDF：提取文本（可选OCR）、清洗、获取元数据
    """
    # 先用PyMuPDF提取文本
    text = extract_text_with_pymupdf(pdf_path)

    # 如果启用OCR且提取的文本过短（少于200字符），则尝试OCR
    if use_ocr and len(text.strip()) < 200:
        print(f"  常规提取文本过短（{len(text)}字符），尝试OCR...")
        try:
            text = extract_text_with_ocr(pdf_path)
        except Exception as e:
            print(f"  OCR失败：{e}")
            # 保留原有文本

    # 获取PDF元数据
    doc = fitz.open(pdf_path)
    meta = doc.metadata
    doc.close()

    return {
        "text": text,
        "pdf_metadata": meta
    }


def save_json_output(data: Dict, out_path: str):
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main(pdf_dir: str, out_dir: str, meta_out: str, use_ocr: bool):
    os.makedirs(out_dir, exist_ok=True)

    pdf_files = [f for f in os.listdir(pdf_dir) if f.lower().endswith('.pdf')]
    if not pdf_files:
        print(f"在 {pdf_dir} 中未找到PDF文件")
        return

    metadata_records = []

    for pdf_file in tqdm(pdf_files, desc="处理PDF"):
        pdf_path = os.path.join(pdf_dir, pdf_file)
        try:
            # 从文件名提取基本信息
            file_meta = extract_metadata_from_filename(pdf_file)

            # 提取文本和PDF元数据
            extracted = process_pdf(pdf_path, use_ocr=use_ocr)
            pdf_meta = extracted["pdf_metadata"]
            raw_text = extracted["text"]

            # 清洗文本
            cleaned = clean_text(raw_text)

            # 合并元数据
            title = pdf_meta.get("title", "").strip() or file_meta["title"]
            authors = pdf_meta.get("author", "").strip() or file_meta["authors"]
            year = file_meta["year"]  # 从文件名解析的年份
            source = pdf_meta.get("source", "")

            record = {
                "file_id": os.path.splitext(pdf_file)[0],
                "file_name": pdf_file,
                "title": title,
                "authors": authors,
                "year": year,
                "source": source,
                "abstract": "",
                "keywords": "",
                "text": cleaned
            }

            # 保存JSON
            json_filename = f"{record['file_id']}.json"
            json_path = os.path.join(out_dir, json_filename)
            save_json_output(record, json_path)

            # 准备元数据行
            meta_row = record.copy()
            meta_row.pop("text")
            meta_row["path_to_text"] = os.path.relpath(json_path, start=os.path.dirname(meta_out) or '.')
            metadata_records.append(meta_row)

        except Exception as e:
            print(f"\n处理文件 {pdf_file} 时出错：{e}")
            continue

    # 保存元数据CSV
    if metadata_records:
        df = pd.DataFrame(metadata_records)
        cols = ["file_name", "title", "authors", "year", "source", "abstract", "keywords", "path_to_text"]
        # 确保所有列都存在
        for col in cols:
            if col not in df.columns:
                df[col] = ""
        df = df[cols]
        csv_path = os.path.join(meta_out, "paper_metadata.csv")
        df.to_csv(csv_path, index=False, encoding='utf-8-sig')
        print(f"\n元数据已保存至：{csv_path}")
        print(f"共处理 {len(metadata_records)} 个PDF文件")
    else:
        print("未生成任何元数据记录")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="处理PDF论文（支持OCR）并生成元数据")
    parser.add_argument("--pdf_dir", type=str, default="./data/papers/raw",
                        help="存放原始PDF的文件夹路径")
    parser.add_argument("--out_dir", type=str, default="./data/papers/processed",
                        help="输出处理后JSON文件的文件夹路径")
    parser.add_argument("--meta_out", type=str, default="./",
                        help="输出元数据CSV的文件夹路径")
    parser.add_argument("--use_ocr", action="store_true",
                        help="对扫描版PDF启用OCR（需要安装pdf2image和pytesseract）")
    args = parser.parse_args()

    if args.use_ocr and not OCR_AVAILABLE:
        print("错误：已指定 --use_ocr，但OCR依赖未安装。请运行：pip install pdf2image pytesseract")
        exit(1)

    main(args.pdf_dir, args.out_dir, args.meta_out, args.use_ocr)