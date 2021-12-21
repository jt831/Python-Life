import random


class Stack:
    def __init__(self):
        self.stack = []  # 初始化一个名叫的stack的list变量，它是Stack类中包含的一个属性

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


def brace_match(s):
    match = {'{': '}', '[': ']', '(': ')'}
    stack = Stack()
    for ch in s:
        if ch in {'{', '(', '['}:
            stack.push(ch)
        elif ch in {']', ')', '}'}:
            if stack.is_empty():  # 匹配完成后']', ')', '}'还有需要匹配的
                return False
            elif stack.get_top() == match[ch]:
                stack.pop()
            elif stack.get_top() != match[ch]:  # 出现不匹配的
                return False
    if stack.is_empty():  # 匹配完成后'{', '(', '['还有没被匹配到的
        return True
    else:
        return False
