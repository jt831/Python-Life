import time
graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}


def DFS(graph, s):
    stack = [s]  # 创建一个stack
    seen = {s}  # 创建一个存放已经加入过stack的set
    while stack:  # 当stack不为空
        """
        pop 是唯一与BFS不同的地方
        """
        vertex = stack.pop()  # 最后一个元素出栈
        for node in graph[vertex]:  # 遍历与其相连的元素
            if node not in seen:  # 如果发现还未被加入stack的元素
                stack.append(node)  # 将其加入stack
                seen.add(node)  # 将其标记为已加入
        print(vertex)


print(time.time())
DFS(graph, "F")
print(time.time())
