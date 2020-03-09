from collections import deque

graph_desc = [
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0],
]

def BFSmy(mygraph, startv, finishv):
    myqueue=deque()
    parents=[None]*len(mygraph)
    is_touch=[False]*len(mygraph)
    parents[startv]=startv
    is_touch[startv]=True
    print(f'list(parents)={list(parents)}, is_touch={list(is_touch)}')

    for i, item in enumerate(mygraph[startv]):
        if item == 1:
            parents[i]=startv
            myqueue.append(i)
    print(f'ИТОГ1 - list(parents)={list(parents)}, is_touch={list(is_touch)}, myqueue={myqueue}')

    while len(myqueue) > 0:
        current_v=myqueue.popleft()
        print(f'get Q={current_v}')
        print(f'mygraph[current_v]={mygraph[current_v]}')
        for j, vert in enumerate(mygraph[current_v]):
            if vert == 1 and not is_touch[j]:
                parents[j] = current_v
                is_touch[j] = True
        print(f'ИТОГ2 - list(parents)={list(parents)}, is_touch={list(is_touch)}, myqueue={myqueue}')

# Диалог
while True:
    first_point=input('Введите начальную вершину: ')
    second_point=input('Введите результирующую вершину: ')

    if not first_point.isdigit() or not second_point.isdigit():
        print('Вы ввели не числовые значение. Попробуйте снова: ')
        continue
    elif int(first_point) < 0 or int(second_point) < 0 \
            or int(first_point) > len(graph_desc)-1 or int(second_point) > len(graph_desc)-1:
        print(f'Таких вершин в графе нет. Введите от 0 до {len(graph_desc)-1}: ')
        continue
    else:
        break

BFSmy(graph_desc, int(first_point), int(second_point))