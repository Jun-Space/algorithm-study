import copy
def change(turn):
    global move
    global typem

    if typem =='y':
        typem ='x'
        if turn=='D':
            a=move[0]
            b=move[1]
            move=[b,a]
        else:
            a=move[0]
            b=move[1]*(-1)
            move=[b,a]
    else:
        typem ='y'
        if turn=='D':
            a=move[0]*(-1)
            b=move[1]
            move=[b,a]
        else:
            a=move[0]
            b=move[1]
            move=[b,a]


N = int(input())
apple_count = int(input())
apple_position = []
for _ in range(apple_count):
    apple_position.append(list(map(int,input().split())))
sneak = [[1,1]]
new_sneak=[]
move_count = int(input())
t=0
move_time=[]
move_act=[]
move=[0,1]
typem ='y'
for _ in range(move_count):
    k = list(map(str,input().split()))
    move_time.append(int(k[0]))
    move_act.append(k[1])


while True:
    t+=1
    new_sneak.append([sneak[0][0]+move[0],sneak[0][1]+move[1]])
    if new_sneak[0][0]==(N+1) or new_sneak[0][0]<1 or new_sneak[0][1]==(N+1) or new_sneak[0][1]<1 :
        break
    if new_sneak[0] in sneak:
        break

    if new_sneak[0] in apple_position:
        apple_position.remove(new_sneak[0])
        for i in range(len(sneak)):
            new_sneak.append(sneak[i])
    else:
        for i in range(len(sneak)-1):
            new_sneak.append(sneak[i])

    sneak = copy.deepcopy(new_sneak)
    new_sneak=[]


    if len(move_time)==0:
        continue

    if t == move_time[0]:
        del move_time[0]
        v = move_act[0]
        del move_act[0]
        change(v)
    



print(t)