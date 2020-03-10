n = 102
sieve = [i for i in range(n)]
print(f'sieve = {sieve}')

sieve[1] = 0 # ------------- 1 -> 0

for i in range(2, n):
    if sieve[i]:
        j = i + i
        # print(f'j = {j}, i = {i}')

        while j < n:

            sieve[j] = False

            j = j + i # ------------- +1 -> j+i
        # print(f'sieve = {sieve}')

# print(f'sieve = {sieve}')

mystr = [
    'Name',
    'Surname',
    'Age',
    'City',
]

def mysort(func):
    for i in range(len(func) // 2):
        func[i], func[len(func) - i - 1] = func[len(func) - i - 1], func[i]
    print(list(func))

print(list(mystr))
mysort(list(mystr))