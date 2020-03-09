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

    myqueue = deque()
    chain = deque()
    parents = [None]*len(mygraph)
    is_touch = [False]*len(mygraph)

    parents[startv] = startv
    is_touch[startv] = True

    for i, item in enumerate(mygraph[startv]):
        if item == 1:
            parents[i] = startv
            myqueue.append(i)
    # print(f'ИТОГ_старт - list(parents)={list(parents)}, is_touch={list(is_touch)}, myqueue={myqueue}')

    while len(myqueue) > 0:
        current_v = myqueue.popleft()
        if current_v == finishv:
            # print(f'Цепочка {startv} - {finishv} установлена')
            while current_v != startv:
                chain.append(current_v)
                current_v = parents[current_v]
            chain.append(startv)
            chain.reverse()
            print(f'Цепочка = {list(chain)}, длина = {len(chain)-1}')
            break
        else:
            for j, vert in enumerate(mygraph[current_v]):
                if vert == 1 and parents[j] == None:
                    parents[j] = current_v
                    myqueue.append(j)
                    # is_touch[j] = True
            is_touch[current_v] = True
            # print(f'ИТОГ_между - list(parents)={list(parents)}, is_touch={list(is_touch)}, myqueue={myqueue}')

    # print(startv, finishv)


# Диалог
while True:
    first_point = input('Введите начальную вершину: ')
    second_point = input('Введите результирующую вершину: ')

    if not first_point.isdigit() or not second_point.isdigit():
        print('Вы ввели не числовые значение. Попробуйте снова: ')
        continue
    elif int(first_point) < 0 or int(second_point) < 0 \
            or int(first_point) > len(graph_desc)-1 or int(second_point) > len(graph_desc)-1:
        print(f'Таких вершин в графе нет. Введите от 0 до {len(graph_desc)-1}: ')
        continue
    elif int(first_point) == int(second_point):
        print(f'Поиск бессмысленный, введите различающиеся значения')
        continue
    else:
        break

def BFSmynew(graph, first_point, second_point):
    fif = deque()
    fif.append(first_point)
    parent = [None]*len(graph)
    is_vis = [False]*len(graph)

    parent[first_point] = first_point
    is_vis[first_point] = True

    while len(fif) > 0:
        current = fif.pop()

        if current == second_point:
            break

        for i, item in enumerate(graph[current]):
            if item == 1 and not is_vis[i]:
                parent[i] = current
                is_vis[i] = True
                fif.appendleft(i)

    chain = deque()
    chain.appendleft(second_point)
    curr_v = second_point
    while curr_v != first_point:
        chain.appendleft(parent[curr_v])
        curr_v = parent[curr_v]

    print(f'Цепь = {list(chain)}. Длина цепи = {len(chain)-1}. \nPS: {list(parent)}, {list(is_vis)}.')



BFSmynew(graph_desc, int(first_point), int(second_point))