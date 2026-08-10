def minimax(depth, node, maximizing, values):

    if depth == 2:
        return values[node]

    if maximizing:
        return max(
            minimax(depth + 1, node * 2, False, values),
            minimax(depth + 1, node * 2 + 1, False, values)
        )
    else:
        return min(
            minimax(depth + 1, node * 2, True, values),
            minimax(depth + 1, node * 2 + 1, True, values)
        )

print("Enter 4 leaf node values:")
values = []

for i in range(4):
    values.append(int(input()))

result = minimax(0, 0, True, values)

print("Optimal Value =", result)
