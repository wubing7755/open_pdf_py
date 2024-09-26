# �Զ���ջ��
class Stack:
    def __init__(self):
        self.items = []

    # ��ջ
    def push(self, item):
        self.items.append(item)

    # ��ջ
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop error: stack is empty")

    # �п�
    def is_empty(self):
        return len(self.items) == 0

    # �鿴ջ��Ԫ�ص�ֵ
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek error: stack is empty")

    # ջ����
    def size(self):
        return len(self.items)

    # ��ӡջ����Ԫ��
    def print_stack(self):
        if not self.is_empty():
            for item in self.items:
                print(item)
        else:
            print("print: stack is empty")
