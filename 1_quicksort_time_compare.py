import random
import time
import numpy as np


# クイックソート
def qsort(nlist, left, right):
    pl = left
    pr = right
    x = nlist[(left + right) // 2]

    while pl <= pr:
        while nlist[pl] < x:
            pl += 1
        while nlist[pr] <= x:
            pr -= 1
        if pl <= pr:
            nlist[pl], nlist[pr] = nlist[pr], nlist[pl]
            pl += 1
            pr -= 1
    if left < pr:
        qsort(nlist, left, pr)
    if pr < right:
        qsort(nlist, pl, right)


# リスト
list0 = []
for i in range(10000):
    list0.append(random.randint(0, 10000))
# print(list0)

# クイックソート
start = time.time()
list2 = list0
np.sort(list2, kind="quicksort")
process_time = time.time() - start
print("{:.16f}".format(float(process_time)))
