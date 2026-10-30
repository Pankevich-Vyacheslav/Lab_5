def find(parent, v):
    """
    Пошук представника множини для вершини v.
    Використовується стиснення шляху.
    """
    if parent[v] != v:
        parent[v] = find(parent, parent[v])

    return parent[v]


def union(parent, rank, u, v):
    """
    Об'єднання двох компонент зв'язності.
    Повертає False, якщо утворюється цикл.
    """
    root_u = find(parent, u)
    root_v = find(parent, v)

    # Перевірка на утворення циклу
    if root_u == root_v:
        return False

    # Об'єднання множин за рангом
    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v

    elif rank[root_u] > rank[root_v]:
        parent[root_v] = root_u

    else:
        parent[root_v] = root_u
        rank[root_u] += 1

    return True


def kruskal(n, edges):
    """
    Алгоритм Крускала для побудови МКД.
    n: кількість вершин графа
    edges: список ребер (u, v, вага)
    """
    # Сортування ребер за вагою та номерами вершин
    edges = sorted(edges, key=lambda e: (e[2], e[0], e[1]))

    # Ініціалізація структури DSU
    parent = list(range(n + 1))
    rank = [0] * (n + 1)

    mst = []
    total_weight = 0

    print("--- Побудова МКД за алгоритмом Крускала ---")

    # Переглядаємо ребра за зростанням ваги
    for step, (u, v, w) in enumerate(edges, start=1):

        # Додаємо ребро, якщо воно не утворює цикл
        if union(parent, rank, u, v):
            mst.append((u, v, w))
            total_weight += w

            print(f"Крок {step}: ({u}, {v}) = {w} "
                  f"— ребро додано")
            print(f"Загальна вага: {total_weight}\n")

        else:
            print(f"Крок {step}: ({u}, {v}) = {w} "
                  f"— пропущено (утворюється цикл)\n")

        # МКД повинно містити n - 1 ребро
        if len(mst) == n - 1:
            break

    # Перевірка зв'язності графа
    if len(mst) != n - 1:
        print("Граф незв'язний. МКД не побудовано.")
        return None

    return mst, total_weight


# Ребра графа варіанта №15: (вершина, вершина, вага)
edges = [
    (1, 2, 8),
    (1, 3, 2),
    (1, 4, 4),
    (1, 5, 3),
    (2, 5, 6),
    (2, 6, 3),
    (3, 4, 6),
    (3, 6, 7),
    (3, 8, 4),
    (4, 5, 1),
    (5, 7, 4),
    (6, 7, 3),
    (6, 8, 1),
    (7, 8, 5)
]

# Моделювання для варіанта №15
result = kruskal(8, edges)

if result is not None:
    mst, total_weight = result

    print("--- Мінімальне кістякове дерево ---")

    for u, v, w in mst:
        print(f"({u}, {v}) = {w}")

    print("\n Загальна вага МКД:", total_weight)
