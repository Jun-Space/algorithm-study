def chicken_selection(sub_chicken_house,i):  # M개의 치킨집을 선정해서 결과 제공
    global M
    global dist

    if len(sub_chicken_house) == M:
        ndist=house_check(sub_chicken_house)
        dist = min(dist,ndist)
        return
    
    for k in range(i,len(chicken_house)):
        sub_chicken_house.append(chicken_house[k])
        chicken_selection(sub_chicken_house,k+1)
        sub_chicken_house.pop()
    
    

def house_check(sub_chicken_house):           #계산을 진행할 집을 선정하는 함수
    cdist=[]
    result=0
    for i in range(N):
        for j in range(N):
            if city[i][j]==1:
                cdist.append(getdist(i,j,sub_chicken_house))
    for a in cdist:
        result += a
    return result

def getdist(x,y,sub_chicken_house):  # 해당 집에서 최소 거리를 구할 함수
    predist=99999
    for a,b in sub_chicken_house:
        subdist = abs(a-x)+abs(b-y)
        predist = min(subdist,predist)
    return predist




N, M = map(int,input().split())
city = []
chicken_house=[]
sub_chicken_house=[]
dist=9999

for _ in range(N):
    city.append(list(map(int,input().split())))
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken_house.append([i,j])

chicken_selection(sub_chicken_house,0)
print(dist)