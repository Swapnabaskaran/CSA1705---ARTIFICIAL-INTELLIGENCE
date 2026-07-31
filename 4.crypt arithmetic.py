from itertools import permutations

letters = ('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y')

for P in permutations(range(10), len(letters)):
    S, E, N, D, M, O, R, Y = P

    if S != 0 and M != 0:  # Leading digits cannot be zero
        send = S * 1000 + E * 100 + N * 10 + D
        more = M * 1000 + O * 100 + R * 10 + E
        money = M * 10000 + O * 1000 + N * 100 + E * 10 + Y

        if send + more == money:
            print("Solution Found")
            print("SEND =", send)
            print("MORE =", more)
            print("MONEY =", money)
            break
