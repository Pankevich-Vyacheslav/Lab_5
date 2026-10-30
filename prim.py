def prim(graph, start=0):
    """
    Алгоритм Прима для побудови мінімального кістякового дерева (МКД).
    Graph - матриця суміжності з вагами ребер
    Start - індекс початкової вершини
    """
    n = len(graph)
    selected = [False] * n
    selected[start] = True

    mst = []
    total_weight = 0

    print("Початкова вершина:", start + 1)
    print("\n --- Побудова МКД за алгоритмом Прима ---")

    # МКД повинно містити n - 1 ребро
    for step in range(1, n):

        min_weight = float('inf')
        best_u = -1
        best_v = -1

        # Пошук ребра з найменшою вагою
        for u in range(n):
            if selected[u]:
                for v in range(n):

                    # Перевіряємо допустимість ребра
                    if not selected[v] and graph[u][v] > 0:

                        # Знаходимо мінімальну вагу
                        if graph[u][v] < min_weight:
                            min_weight = graph[u][v]
                            best_u = u
                            best_v = v

        # Перевірка зв'язності графа
        if best_u == -1:
            print("Граф незв'язний. Побудова неможлива.")
            return None

        # Додаємо нову вершину до МКД
        selected[best_v] = True

        # Записуємо ребро в порядку номерів вершин
        edge = tuple(sorted((best_u + 1, best_v + 1)))
        mst.append((edge[0], edge[1], min_weight))

        # Обчислюємо загальну вагу
        total_weight += min_weight

        print(f"Крок {step}: ({edge[0]}, {edge[1]}) "
              f"= {min_weight}")
        print(f"Загальна вага: {total_weight}\n")

    return mst, total_weight


# Матриця суміжності графа варіанта №15
G = [
    [0, 8, 2, 4, 3, 0, 0, 0],
    [8, 0, 0, 0, 6, 3, 0, 0],
    [2, 0, 0, 6, 0, 7, 0, 4],
    [4, 0, 6, 0, 1, 0, 0, 0],
    [3, 6, 0, 1, 0, 0, 4, 0],
    [0, 3, 7, 0, 0, 0, 3, 1],
    [0, 0, 0, 0, 4, 3, 0, 5],
    [0, 0, 4, 0, 0, 1, 5, 0]
]

# Моделювання для варіанта №15
result = prim(G, start=0)

if result is not None:
    mst, total_weight = result

    print("--- Мінімальне кістякове дерево ---")
    for u, v, w in mst:
        print(f"({u}, {v}) = {w}")

    print("\n Загальна вага МКД:", total_weight)
