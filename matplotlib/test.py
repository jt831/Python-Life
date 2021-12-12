import random
from time import sleep


def liner_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
        return


def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:
        divide = (left + right) // 2
        if li[divide] == val:
            return divide
        elif li[divide] > val:
            right = divide - 1
        elif li[divide] < val:
            left = divide + 1
    else:
        return None


def bubble_sort(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - 1 - i):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            return
        print(li)


def select_sort(li):
    """每次选出当前无序list中最小的一个数，并把它和无序list的第一个元素交换"""
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]
        print(li)


def insert_sort(li):
    """i代表你抽出的牌，j代表你的手牌。
    若i<j，先将i对应的值存储在temp中，再把j对应的值往后挪一位
    直到找到i>j,就将i插入第j+1个位置
    或者直到第一个值还是比i大，就将i插入第一个位置"""
    for i in range(1, len(li)):
        j = i - 1
        temp = li[i]
        while temp < li[j] and j >= 0:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = temp
        print(li)


def quick_sort(li, left, right):
    if left < right:  # 确保至少有两个元素
        divide = qs_partition(li, left, right)
        quick_sort(li, left, divide - 1)
        quick_sort(li, divide + 1, right)


def qs_partition(li, left, right):
    """此函数接收一个可迭代对象和左右索引。
    实现对该可迭代对象进行排序，确定一个大于左边的数并小于右边的数的'分割数'，返回分割数的索引"""
    print(li)
    divide_num = li[left]
    while left < right:
        while left < right and li[right] >= divide_num:  # 从右边找比divide小的数并填到左边去
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= divide_num:  # 从左边找比divide大的数并填到右边去
            left += 1
        li[right] = li[left]

    li[left] = divide_num  # 将分割数归位
    return left  # 返回此时分割数的索引


def heap_sort(li):
    n = len(li)
    for i in range((n - 2) // 2, -1, -1):  # 找到每一个父节点
        sift(li, i, n - 1)
    # 建堆完成
    for i in range(n - 1, -1, -1):  # 指向当前最后的元素
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)  # i-1指向新的最后一个元素


def sift(li, low, high):
    """
    向下调整函数，用于将除了根节点之外的位置都已经是堆的树调整为一个堆
    :param li: a iterable object
    :param low:the location of the root node of the heap
    :param high:the location of the last node of the heap
    :return:
    """
    i = low  # i 指向当前父节点
    j = 2 * i + 1  # j暂时指向父节点的左子节点
    tmp = li[low]  # storage the num of the root node
    while j <= high:  # j指向的位置有效
        if j + 1 <= high and li[j + 1] > li[j]:  # 存在右子节点且右节点的值比左节点大
            j = j + 1  # j指向较大子节点
        if li[j] > tmp:
            li[i] = li[j]
            i = j  # i和j都往下移动一层
            j = i * 2 + 1
        else:
            break
    li[i] = tmp


def merge(li, low, mid, high):  # 实现归并
    p1 = low
    p2 = mid + 1
    temp = []
    while p1 <= mid and p2 <= high:
        if li[p1] < li[p2]:
            temp.append(li[p1])
            p1 += 1
        else:
            temp.append(li[p2])
            p2 += 1
    while p1 <= mid:
        temp.append(li[p1])
        p1 += 1
    while p2 <= high:
        temp.append(li[p2])
        p2 += 2
    li[low:high + 1] = temp


def merge_sort(li, low, high):
    if low < high:
        mid = (low + high)//2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)


list1 = [random.randint(1, 55) for num in range(10)]
print("origin list " + str(list1))
sleep(1)
merge_sort(list1, 0, len(list1) - 1)
print(list1)
