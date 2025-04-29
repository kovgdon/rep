def dfs(edges, a, b):
    # Проверка корректности a и b
    all_nodes = set()
    for u, v in edges:
        all_nodes.add(u)
        all_nodes.add(v)
    # Проверяем, что вершины a и b существуют в графе
    if a not in all_nodes:
        raise ValueError(f"Vertex {a} does not exist")
    if b not in all_nodes:
        raise ValueError(f"Vertex {b} does not exist")
    graph = {}
    for u, v in edges:
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)
    
    visited = set()
    # Обход в глубину для поиска пути от a до b
    stack = [(a, 0)]  # (вершина, расстояние)
    
    while stack:
        vertex, distance = stack.pop()
        if vertex == b:
            return distance
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph.get(vertex, []):
                stack.append((neighbor, distance + 1))
    return -1  # Путь не найден

# Пример использования:
edges = [(4, 2), (1, 3), (2, 4)]
print(dfs(edges, 2, 4))  # Вывод: 1
