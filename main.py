# -*- coding: GBK -*-

import subprocess

from src.funcs import read_pdf

from src.funcs import redo, undo

from src.models import Stack


def main():
    # ��ȡpdf�ļ�����д��txt�ļ���
    #read_pdf()

    stack = Stack()

    nums = input("������һ�����֣��� ',' �ָ���").split(',')

    for num in nums:
        stack.push(num)

    stack.print_stack()

    # ��ԭ
    redo(stack)
    stack.print_stack()

    # ����
    undo(stack)
    stack.print_stack()

if __name__ == "__main__":
    # ��������ʾ����ִ�� 'cls' ����
    subprocess.run("cmd.exe /c cls", shell=True)
    main()
