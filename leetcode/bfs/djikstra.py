def djikstra(graph, start):
    visited = set()
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    queue = [start]
    while queue:
        node = queue.pop(0)
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                new_distance = distances[node] + graph[node][neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
    return distances

result = djikstra({
    "A": {"B": 1, "C": 4},
    "B": {"C": 2, "D": 5},
    "C": {"D": 1},
    "D": {}
}, "A")
print(result)