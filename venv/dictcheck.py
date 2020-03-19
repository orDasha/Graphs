from collections import OrderedDict, deque
import hashlib
import unicodedata
from sys import getdefaultencoding

dict_check = {
    'name': 'Myname',
    'Age': '33',
    'City': 'Moscow',
    'Lang': 'RU',
}

dict_check = OrderedDict(dict_check)
print(dict_check)
dict_check.move_to_end('City', last=False)
print(dict_check)

queue = deque()
queue.append(1)
queue.append(3)
queue.append(7)
p = queue.pop()
print(queue)
print(p)

arr = [0, 1, 2, 13, 4, 5, 6, 7, 8, 9]
num = 921158446
arr_new = arr[:2] + [num] + arr[2:]
print(arr_new)

a, b = 0, 0
while num > 0:
    if num % 2 == 0:
        a += 1
    else:
        b += 1
    num = num // 10

print(a, b)

imin, imax = 0, 0
for i in range(len(arr)):
    if arr[i] < arr[imin]:
        imin = i
        # print(f'imin = {imin}')
    elif arr[i] > arr[imax]:
        imax = i
        # print(f'imax = {imax}')

print(f'imin = {imin}')
print(f'imax = {imax}')
print(len(arr))

