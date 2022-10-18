def find_crossing(a, low, mid, high):
    max_left = 0
    max_right = 0
    left_sum = -1e308
    sum = 0
    for i in range(mid, low, -1):
        sum = sum + a[i][1]
        if sum > left_sum:
            left_sum = sum
            max_left = i
            max_right = 0

    right_sum = -1e308
    sum = 0
    for j in range(mid + 1, high):
        sum = sum + a[j][1]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return max_left, max_right, left_sum + right_sum


def find_max_subarray(a, low, high):
    if high == low:
        return low, high, a[low][1]
    else:
        mid = (low + high) / 2
        left_low, left_high, left_sum = find_max_subarray(a, low, mid)
        right_low, right_high, right_sum = find_max_subarray(a, mid + 1, high)
        cross_low, cross_high, cross_sum = find_crossing(a, low, mid, high)
        if (left_sum >= right_sum) & (left_sum >= cross_sum):
            return left_low, left_high, left_sum
        elif (right_sum >= left_sum) & (right_sum >= cross_sum):
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


f = open("6_input.txt")
m = open("6_output.txt", "w")

#чтение файла
num = int(f.readline())
date = [[0, 0] for i in range(num)]
for i in range(0, num):
    date[i][0] = f.readline().rstrip('\n')
for j in range(0, num):
    date[j][1] = float(f.readline())
print(date)

#подготовка данных
prev = 0
courses = []
for i in range(0, len(date)):
    cur = date[i][1]
    if prev == 0:
        prev = cur
    # сохраним разницу в списке
    value = [date[i][0], prev - cur, date[i][1]]
    prev = cur
    courses.insert(0, value)
print(courses)

min, max, sum =
print(courses[min])
print(courses[max])
print(sum)

f.close()
m.close()
