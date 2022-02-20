from collections import deque



class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


class Queue:
    def __init__(self, size):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.front = 0
        self.end = 0

    def is_full(self):
        return (self.front - 1) % self.size == self.end

    def is_empty(self):
        return self.front == self.end

    def push(self, element):
        if self.is_full():
            raise IndexError("Queue is Full")
        else:
            self.end = (self.end + 1) % self.size
            self.queue[self.end] = element

    def pop(self):
        if self.is_empty():
            raise IndexError("Queue is Empty")
        else:
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


def create_linklist(li):
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head


def create_linklistR(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head


'''li = [1, 2, 3, 4, 5, 6, 7, 9]
lk = create_linklistR(li)
while lk:
    print(lk.item, end='.')
    lk = lk.next'''


class Fibonacci(object):
    def __init__(self, nums):
        self.nums = nums
        self.a = 0
        self.b = 1
        self.times = 0

    def __iter__(self):
        return self

    def __next__(self):
        ret = self.a
        if self.times < self.nums:
            self.a, self.b = self.b, self.a + self.b
            self.times += 1
            return ret
        else:
            raise StopIteration












def bucket_match(li):
    stack = Stack()
    match = {'(': ')', '[': ']', '{': '}'}
    for i in li:
        if i in {'(', '[', '{'}:
            stack.push(i)
        else:
            if stack.is_empty():  # 只有一个右括号
                return False
            elif stack.get_top() == match[i]:  # 括号形式不匹配
                stack.pop()
            else:
                return False
    if stack.is_empty():  # 只有一个左括号
        return True
    else:
        return False
