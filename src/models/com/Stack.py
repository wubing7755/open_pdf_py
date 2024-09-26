# 自定义栈类
class Stack:
    def __init__(self):
        self.items = []

    # 入栈
    def push(self, item):
        self.items.append(item)

    # 出栈
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop error: stack is empty")

    # 判空
    def is_empty(self):
        return len(self.items) == 0

    # 查看栈顶元素的值
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek error: stack is empty")

    # 栈长度
    def size(self):
        return len(self.items)

    # 打印栈所有元素
    def print_stack(self):
        if not self.is_empty():
            for item in self.items:
                print(item)
        else:
            print("print: stack is empty")
