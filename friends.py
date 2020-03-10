from collections import deque

def friends(num_friends):
    matrix = [[0 for x in range(num_friends)] for y in range(num_friends)]

    matrix_str = 0
    count = 0
    while matrix_str < num_friends:
        for i, item in enumerate(matrix[matrix_str]):
            if i > matrix_str:
                matrix[matrix_str][i] = 1
                count += 1
                # print(f'matrix[matrix_str] = {matrix[matrix_str]}, item = {item}, i={i}, matrix_str={matrix_str}')
        matrix_str += 1

    # print(f'Матрица друзей: {list(matrix)}, всего рукопожатий: {count}')
    print(f'Всего рукопожатий: {count}')

while True:
    num_friends = input(f'Сколько друзей встретились? ')
    if not num_friends.isdigit() or int(num_friends) < 2:
        print('Ввели некорректные значения, еще раз.')
        continue
    else:
        friends(int(num_friends))
        break