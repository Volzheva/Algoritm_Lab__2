import time
import os, psutil
import random


def merge(list1, list2):
    list3 = []
    i = j = 0
    while i < len(list1) or j < len(list2):
        if j == len(list2) or (i < len(list1) and list1[i] < list2[j]):
            list3.append(list1[i])
            i += 1
        else:
            list3.append(list2[j])
            j += 1
    return list3


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    left = merge_sort(arr[: len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2:])

    return merge(left, right)


def test(a, b):
    k = []
    for i in range(0, a):
        k.append(random.randint(-b, b))
    return k



t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("1_input.txt", "w")
m = open("1_output.txt", "w")

f.write("10\n")
numbers = test(10, 10)
f.write(" ".join(map(str, numbers)))
print(merge_sort(numbers))
sorted_numbers = merge_sort(numbers)
m.write(" ".join(map(str, sorted_numbers)))

f.close()
m.close()

print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")
