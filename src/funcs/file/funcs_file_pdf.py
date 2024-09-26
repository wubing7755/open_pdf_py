# -*- coding: GBK -*-

from ast import Import
import pymupdf  # 使用 PyMuPDF 的新模块名称
import subprocess
from pathlib import Path

def read_pdf():
    pdf_file_name = input("请输入pdf文件名：") + ".pdf"

    # 文件路径名
    base_path = Path(r"C:\Users\xuanit\Desktop\docTest")
    pdf_path = base_path / pdf_file_name  # 使用 Path 对象拼接路径

    print(f"pdf文件路径： {pdf_path}")

    # 打开pdf文档
    try:
        doc = pymupdf.Document(pdf_path, filetype="pdf")
    except Exception as e:
        print(f"打开 PDF 文件时出错: {e}")
        return

    # 新建文本文件
    txt_file_name = input("请输入txt文件名：") + ".txt"
    txt_file_path = base_path / txt_file_name
    print(f"文本文件路径： {txt_file_path}")
    with open(txt_file_path, "w") as new_txt:
        # 遍历pdf文档，将内容写到txt文件中
        for page in doc:
            text = page.get_text()
            new_txt.write(text + "\n")

        # 打印pdf页数
        new_txt.write(f"page_count:{doc.page_count}")


        new_txt.close()

    print(f"PDF 内容已成功写入 {txt_file_path}")
    # 使用 subprocess 打开文件资源管理器
    subprocess.run(["explorer", txt_file_path])