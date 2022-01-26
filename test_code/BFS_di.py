import heapq
import math

graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6}
}


def init_distance(graph, s):

    distance = {s: 0}  # 记录当前节点到起点的距离
    for vertex in graph:
        if vertex is not s:  # 对于那些不是起始节点的
            distance[vertex] = math.inf  # 将它们初始化为正无穷
    return distance


def BFS_di(graph, s):
    """
    传入一个加权图以及起始节点，返回各节点到起始节点的最短路线与距离

    :param graph: 一个嵌套字典。外层key为父节点名。内层key为与父节点直接连接的子节点名，value为子节点与父节点的距离
    :param s: 起始节点
    :returns: parent: 在各节点到起始节点最短路径下，各节点的父节点。
              distance: 各节点离起始节点的最短距离
    """
    pqueue = []  # 创建一个pqueue存放待处理的点
    heapq.heappush(pqueue, (0, s))  # 将第一个点以及它离起始点的距离放进去
    seen = set()  # 创建一个存放已经从pqueue出来的节点名称的set
    parent = {s: None}  # 创建一个dict，表示key是从value来的
    distance = init_distance(graph, s)  # 将起始点到起始点的距离初始化为0，其余点初始化为正无穷

    while len(pqueue) > 0:  # 当pqueue不为空
        pair = heapq.heappop(pqueue)  # 取出pqueue第一个点（dist， vertex）（此时dist为最小）
        dist = pair[0]  # 被取出的点到起始点的距离
        vertex = pair[1]  # 被取出的点名称
        seen.add(vertex)  # 只有vertex被取出之后才能视为不再被遍历

        for node in graph[vertex].keys():
            if node not in seen:  # 对于那些未被从pqueue取出过的vertex的子节点来说
                if dist + graph[vertex][node] < distance[node]:  # 如果它们经由父节点到起始点的距离比原来的距离短
                    heapq.heappush(pqueue, (dist + graph[vertex][node], node))  # 就将它们加入queue
                    parent[node] = vertex  # 更新它们的父节点
                    distance[node] = dist + graph[vertex][node]  # 更新它们到起始点的距离
    return parent, distance


parent, distance = BFS_di(graph, "A")
print(parent)
print(distance)
