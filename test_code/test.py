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
    先将li[i]存储在temp中，若li[i]<li[j]，再把li[j]往后挪一位
    直到找到li[i]>li[j],就将li[i]插入第j+1个位置
    或者直到第一个值还是比li[i]大，就将li[i]插入第一个位置"""
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


def merge(li, low, mid, high):  # 实现归并,使得两个有序的序列归并成一个同序的序列
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
        p2 += 1
    li[low:high + 1] = temp


def merge_sort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)


def shell_sort(li):
    gap = len(li) // 2
    while gap >= 1:
        insert_sort_gap(li, gap)
        gap = gap // 2


def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):
        tmp = li[i]
        j = i - gap
        while j >= 0 and li[j] > tmp:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = tmp


def count_sort(li, max_count=100):  # 已经知道数组中数的范围时，使用计数排序
    count = [0 for _ in range(max_count + 1)]  # 创建一个数的范围长度的列表
    for val in li:
        count[val] += 1  # 此时列表值表示下标对应的数的个数
    li.clear()  # 清空原数组
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)


def bucket_sort(li, n=10, max_num=100):
    buckets = [[] for _ in range(n)]  # 创建了n个下标从0到n - 1的桶（数组）
    for var in li:
        i = min(var // (max_num // n), n - 1)  # 确定每个数要放在哪个桶里。使用min是为了让var等于max_num时li【i】不越界
        buckets[i].append(var)  # 将原li中的数放入对应数组
        for j in range(len(buckets[i]) - 1, 0, -1):  # 对每个数排序
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break
    sorted_li = []  # 实现合成一个数组输出
    for bucket in buckets:
        sorted_li.extend(bucket)
    return sorted_li


def radix_sort(li):
    max_num = max(li)
    times = 0
    while 10 ** times <= max_num:  # 确定最大值的位数（循环的次数）
        buckets = [[] for _ in range(10)]
        for var in li:
            digit = (var // 10 ** times) % 10  # 依次取个位，十位。。。
            buckets[digit].append(var)
        li.clear()
        for bucket in buckets:
            li.extend(bucket)
        times += 1


list1 = [random.randint(0, 114514) for num in range(1000)]
print("origin list " + str(list1))
sleep(1)
radix_sort(list1)
print(list1)
