# -*- coding: GBK -*-

import subprocess

from src.funcs import read_pdf

from src.funcs import redo, undo

from src.models import Stack


def main():
    # 读取pdf文件，并写入txt文件中
    #read_pdf()

    stack = Stack()

    nums = input("请输入一串数字，以 ',' 分隔：").split(',')

    for num in nums:
        stack.push(num)

    stack.print_stack()

    # 复原
    redo(stack)
    stack.print_stack()

    # 撤销
    undo(stack)
    stack.print_stack()

if __name__ == "__main__":
    # 打开命令提示符并执行 'cls' 命令
    subprocess.run("cmd.exe /c cls", shell=True)
    main()
