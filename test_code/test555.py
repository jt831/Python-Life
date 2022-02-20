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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(self, root: TreeNode) :
    if not root: return []
    queue = [root]
    res = []
    layer = 0
    while queue:
        res.append([node.val for node in queue] if layer % 2 is 0
                   else list(reversed([node.val for node in queue])))

        children = []
        for node in queue:
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
        queue = children
        layer += 1
    return res
