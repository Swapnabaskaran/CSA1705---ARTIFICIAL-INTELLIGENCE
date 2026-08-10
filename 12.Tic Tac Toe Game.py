board = [' '] * 9

def display():
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])
    print()

win = [(0,1,2),(3,4,5),(6,7,8),
       (0,3,6),(1,4,7),(2,5,8),
       (0,4,8),(2,4,6)]

for i in range(5):
    display()
    pos = int(input("Enter position (0-8): "))
    board[pos] = 'X'

    for a, b, c in win:
        if board[a] == board[b] == board[c] == 'X':
            display()
            print("Player X Wins")
            exit()

display()
print("Game Over")
