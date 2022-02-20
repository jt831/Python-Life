from collections import deque

arounds = [
    lambda x, y:(x+1, y),
    lambda x, y:(x-1, y),
    lambda x, y:(x, y+1),
    lambda x, y:(x, y-1)
]


def maze_path(maze, x1, y1, x2, y2):
    stacks = [(x1, y1)]
    maze[x1][y1] = 2
    while len(stacks) > 0:
        now_place = stacks[-1]
        if now_place[0] == x2 and now_place[1] == y2:
            for stack in stacks:
                print(stack)
            return True
        findtimes = 0
        for around in arounds:
            next_place = around(now_place[0], now_place[1])
            if maze[next_place[0]][next_place[1]] == 0:
                stacks.append(next_place)
                maze[next_place[0]][next_place[1]] = 2
                break
            elif findtimes < 3:
                findtimes += 1
                continue
            else:
                stacks.pop()
    else:
        print("No such path")
        return False


def print_r(path):
    curNode = path[-1]
    real_path = []
    while curNode[2] == -1:
        real_path.append(curNode[0:2])
        curNode = path(curNode[2])
    real_path.append(curNode[0:2])  # 把起点放进去
    real_path.reverse()
    print(real_path)


def maze_path_deque(maze, x1, y1, x2, y2):
    queue = deque()  # 存储当前正在考虑的节点
    queue.append((x1, y1, -1))
    path = []
    while len(queue) > 0:
        curNode = queue.pop()
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            print_r(path)
            return True
        for around in arounds:
            nextNode = around(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                queue.append((nextNode[0], nextNode[1], len(path) - 1))
                maze[nextNode[0]][nextNode[1]] = 2
            else:
                continue
    else:
        print("No such path")
        return False


maze_test = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1]
]

maze_path_deque(maze_test, 2, 1, 2, 4)

