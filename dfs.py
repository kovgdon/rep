def dfs(edges, start):
    graph = {}
    for u, v in edges:
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)
    
    visited = set()
    stack = [(a, 0)]
    
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