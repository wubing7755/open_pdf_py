# -*- coding: GBK -*-

from ast import Import
import pymupdf  # ʹ�� PyMuPDF ����ģ������
import subprocess
from pathlib import Path

def read_pdf():
    pdf_file_name = input("������pdf�ļ�����") + ".pdf"

    # �ļ�·����
    base_path = Path(r"C:\Users\xuanit\Desktop\docTest")
    pdf_path = base_path / pdf_file_name  # ʹ�� Path ����ƴ��·��

    print(f"pdf�ļ�·���� {pdf_path}")

    # ��pdf�ĵ�
    try:
        doc = pymupdf.Document(pdf_path, filetype="pdf")
    except Exception as e:
        print(f"�� PDF �ļ�ʱ����: {e}")
        return

    # �½��ı��ļ�
    txt_file_name = input("������txt�ļ�����") + ".txt"
    txt_file_path = base_path / txt_file_name
    print(f"�ı��ļ�·���� {txt_file_path}")
    with open(txt_file_path, "w") as new_txt:
        # ����pdf�ĵ���������д��txt�ļ���
        for page in doc:
            text = page.get_text()
            new_txt.write(text + "\n")

        # ��ӡpdfҳ��
        new_txt.write(f"page_count:{doc.page_count}")


        new_txt.close()

    print(f"PDF �����ѳɹ�д�� {txt_file_path}")
    # ʹ�� subprocess ���ļ���Դ������
    subprocess.run(["explorer", txt_file_path])