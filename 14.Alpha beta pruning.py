MAX = 1000
MIN = -1000

def alphabeta(depth, node, maxi, values, alpha, beta):
    if depth == 2:
        return values[node]

    if maxi:
        return max(alphabeta(depth+1, node*2, False, values, alpha, beta),
                   alphabeta(depth+1, node*2+1, False, values, alpha, beta))
    else:
        return min(alphabeta(depth+1, node*2, True, values, alpha, beta),
                   alphabeta(depth+1, node*2+1, True, values, alpha, beta))

values = list(map(int, input("Enter 4 leaf node values: ").split()))

print("Leaf Node Values:", values)
print("Optimal Value =", alphabeta(0, 0, True, values, MIN, MAX))
