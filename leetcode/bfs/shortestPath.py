from collections import deque

# Initialize the graph
graph = {
    "home": ["A", "B"],
    "A": ["C", "D"],
    "B": ["E", "F"],
    "C": ["uni"],
    "D": [],
    "E": ["H"],
    "H": ["uni"],
    "F": [],
    "uni": []
}

def breadthFirstSearch(start, target):
    search_queue = deque()
    search_queue.append((start, [start]))
    searched = []

    while search_queue:
        (node, path) = search_queue.popleft()
        if node not in searched:
            if node == target:
                return path
            else:
                for neighbor in graph.get(node, []):
                    search_queue.append((neighbor, path + [neighbor]))
                searched.append(node)
    return []

# Example usage
path = breadthFirstSearch("home", "uni")
print("Shortest path from home to uni:", path)