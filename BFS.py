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

def bfs(graph, start, finish):
    parent = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]

    deq = deque([start])
    try:
        is_visited[start] = True
    except IndexError:
        return f'Из вершины {start} нельзя попасть в {finish}'
    print(f'is_visited = {list(is_visited)}')

# -----------------------------------------------------
    while len(deq) > 0:
        len_deq = len(deq)
        current = deq.pop()
        print(f'while len(deq) > 0 = {len_deq} CURRENT = {current}')

        if current == finish:
            # return parent
            break

        for i, vertex in enumerate(graph[current]):
            # print(f'graph[current] = {graph[current]}')
            # print(f'for i, vertex in enumerate, i = {i}, vertex = {vertex}, is_visited[i] = {is_visited[i]}')

            if vertex == 1 and not is_visited[i]:
                # print(f'IF v=1 not is_visited[i] = {is_visited[i]}')
                is_visited[i] = True
                # print(f'is_visited = {list(is_visited)}')
                parent[i] = current
                print(f'i = {i}, parent = {list(parent)}')
                deq.appendleft(i)
                # print(f'---deq.appendleft(i) = {list(deq)}')

    else:
        return f'Из вершины {start} нельзя попасть в {finish}'

    cost = 0
    way = deque([finish])
    i = finish
    print(f'cost=0, WAY_finish = {list(way)}, i = finish = {i}')

    while parent[i] != start:
        print(f'while parent[i] != start, i = {i}, PARENT = {list(parent)}, parent[i] = {parent[i]}')
        cost += 1
        print(f'COST = {cost}')
        way.appendleft(parent[i])
        print(f'way.appendleft(parent[i]), WAY = {list(way)}')
        i = parent[i]
        print(f'i = parent[i], i = {i}')

    cost += 1
    print(f'cost = {cost}')
    way.appendleft(start)
    print(f'way.appendleft(start), WAY = {list(way)}')

    return f'Кратчайший путь {list(way)} длиной в {cost} условных единиц'

while True:
    start_vertex = input('От какой вершины идти: ')
    finish_vertex = input('До какой вершины идти: ')

    if not start_vertex.isdigit():
        continue

    if not finish_vertex.isdigit():
        continue

    print(bfs(graph_desc, int(start_vertex), int(finish_vertex)))
    break