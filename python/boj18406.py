N = int(input())
count=10
length=1
front = 0
rear = 0
while True:
    if count>N:
        break
    count*=10
    length+=1
half = length//2
count = count//10
for i in range(half):
    a = N//count
    N = N%count
    front += a
    count//=10
while count !=0:
    a = N//count
    N = N%count
    rear += a
    count//=10
if front==rear:
    print("LUCKY")
else:
    print("READY")