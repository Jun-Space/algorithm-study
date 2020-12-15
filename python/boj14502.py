from collections import deque
import copy
def queue(x, y):
    q = deque()
    q.append((x,y))
    while q:
        i, j = q.popleft()
        for k in range(4):
            nx = i+dx[k]
            ny = j+dy[k]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if mgraph[nx][ny] != 0:
                continue
            if mgraph[nx][ny] == 0:
                q.append((nx,ny))
                mgraph[nx][ny] = 2


dx = [-1,1,0,0]
dy = [0,0,1,-1]

#입력값 저장
N, M = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

mcount = 0


# bruteForce로 각 벽을 세울 수 있는 경우의 수를 모드 적용해보자
# 각 case 별로 적용할 ngraph 생성
for x in range(N):
    for y in range(M):
        if graph[x][y] != 0:
            continue
        ngraph = copy.deepcopy(graph)
        ngraph[x][y] = 1 #첫번째 벽 생성. 첫번째 벽이 지정된 그래프는 ngraph
        kx, ky = x, y
        while True:
            kgraph = copy.deepcopy(ngraph) #두번째 벽을 저장할 그래프는 kgraph로 지정

            ky+=1
            if ky==M:
                kx+=1
                ky=0
                if kx==N:
                    break
            if kgraph[kx][ky]!=0:
                continue
            else:
                kgraph[kx][ky]=1 #두번째 벽 생성
                mx, my = kx, ky
                while True:
                    mgraph = copy.deepcopy(kgraph)  #세번째 벽을 저장할 그래프는 mgraph로 지정
                    my+=1
                    if my==M:
                        mx+=1
                        my=0
                        if mx==N:
                            break
                    if mgraph[mx][my]!=0:
                        continue
                    else:
                        mgraph[mx][my]=1 #세번째 벽 생성
                    
                    for i in range(N): #bfs 진행
                        for j in range(M):
                            if mgraph[i][j] == 2:
                                queue(i,j)
                    numof0 = 0

                    for a in range(N):
                        for b in range(M):
                            if mgraph[a][b] == 0:
                                numof0+=1
                    if numof0>mcount:
                        mcount = numof0
                        

print(mcount)


#벽을 세우는 방법에서 매우 크게 고민함
#count를 적용해서 벽이 3개인 것을 계산해 가면서 하면 쉽게 할 수 있었다.(재귀함수 이용)
#어차피 첫행부터 순서대로 적용하는 것이므로