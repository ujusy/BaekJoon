import sys
a,b = map(int,input().split())

matrix=[]

for i in range(a):
    c=list(input())
    c=list(map(int,c))
    matrix.append(c)


dx=[0,0,1,-1]
dy=[-1,1,0,0]
visit = [ [0 for j in range(b)]  for i in range(a)]
queue = []
queue.append((0,0))
visit[0][0] = 1

while queue:
    x,y = queue.pop(0)
    for i in range(4):
        mvx = x+dx[i]
        mvy = y+dy[i]  
        if mvx>=0 and mvx<a and  mvy<b and mvy>=0:
            if visit[mvx][mvy]==0 and matrix[mvx][mvy] == 1:
                visit[mvx][mvy] = visit[x][y] + 1 
                queue.append((mvx, mvy))
    if x == a-1 and y ==b-1:
        print(visit[x][y])
        break



