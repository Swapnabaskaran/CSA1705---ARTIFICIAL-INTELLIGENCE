from itertools import permutations

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = [1, 2, 3]
min_cost = 9999
best_path = ()

for p in permutations(cities):
    cost = graph[0][p[0]]
    for i in range(len(p)-1):
        cost += graph[p[i]][p[i+1]]
    cost += graph[p[-1]][0]

    if cost < min_cost:
        min_cost = cost
        best_path = (0,) + p + (0,)

print("Best Path:", best_path)
print("Minimum Cost:", min_cost)
