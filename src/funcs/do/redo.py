from src.models import Stack

def redo(stack:Stack):
    stack.pop()

def undo(stack:Stack):
    stack.push(3)