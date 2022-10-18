import time
import os, psutil
import random


def max_subarray_sum(my_array, array_size):
    max_till_now = my_array[0]
    max_ending = 0
    for n in range(0, array_size):
        max_ending = max_ending + my_array[n]
        if max_ending < 0:
            max_ending = 0
        elif max_till_now < max_ending:
            max_till_now = max_ending

    return max_till_now


def test(a, b):
    k = []
    for i in range(0, a):
        k.append(random.randint(-b, b))
    return k


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("7_input.txt", "w")
m = open("7_output.txt", "w")

f.write("10\n")
numbers = test(10, 10)
f.write(" ".join(map(str, numbers)))
m.write(str(max_subarray_sum(numbers, len(numbers))))

f.close()
m.close()

print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")



