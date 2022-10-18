import time
import os, psutil


def binary_search(arr, val):
    first = 0
    last = len(arr)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if arr[mid] == val:
            index = mid
        else:
            if val < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("4_input.txt")
m = open("4_output.txt", "w")

num1 = int(f.readline())
string = f.readline()
array = list(map(int, string.split()))
num2 = int(f.readline())
string = f.readline()
find_indexes = list(map(int, string.split()))

indexes = []
for i in find_indexes:
    indexes.append(binary_search(array, i))

m.write(" ".join(map(str, indexes)))

f.close()
m.close()

print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")
