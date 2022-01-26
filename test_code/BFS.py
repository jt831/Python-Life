import time
graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}


def BFS(graph, s):
    queue = [s]  # 创建一个queue
    seen = {s}  # 创建一个存放已经加入过queue的set
    while len(queue) > 0:  # 当queue不为空
        vertex = queue.pop(0)  # 取出queue第一个元素
        nodes = graph[vertex]  # 取得与其相连的元素
        for node in nodes:  # 遍历与其相连的元素
            if node not in seen:  # 如果发现还未被加入queue的元素
                queue.append(node)  # 将其加入queue
                seen.add(node)  # 将其标记为已加入
        print(vertex)


print(time.time())
BFS(graph, "F")
print(time.time())
