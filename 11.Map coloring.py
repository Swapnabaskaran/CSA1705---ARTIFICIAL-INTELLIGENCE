graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']
result = {}

def is_safe(node, color):
    for neighbor in graph[node]:
        if result.get(neighbor) == color:
            return False
    return True

def color_map():
    for node in graph:
        for color in colors:
            if is_safe(node, color):
                result[node] = color
                break

color_map()

print("Map Coloring Solution:")
for node in result:
    print(node, "->", result[node])
