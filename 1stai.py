from collections import deque

goal=((1,2,3),(4,5,6),(7,8,0))

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j]==0:
                return i,j

def bfs(start):
    q=deque([(start,[])])
    visited=set()

    while q:
        state,path=q.popleft()

        if state==goal:
            return path+[state]

        if state in visited:
            continue
        visited.add(state)

        x,y=find_zero(state)

        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx=x+dx
            ny=y+dy

            if 0<=nx<3 and 0<=ny<3:
                new=[list(r) for r in state]
                new[x][y],new[nx][ny]=new[nx][ny],new[x][y]
                new=tuple(tuple(r) for r in new)

                if new not in visited:
                    q.append((new,path+[state]))

print("Enter Initial State:")
start=[]

for i in range(3):
    row=tuple(map(int,input().split()))
    start.append(row)

start=tuple(start)

ans=bfs(start)

print("\nSolution Steps:")
for s in ans:
    for r in s:
        print(*r)
    print()
