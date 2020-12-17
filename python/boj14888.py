def make_order():
    while True:
        pre_order.append(D.pop())
        if len(pre_order)==(N-1):
            if pre_order not in order:
                order.append(pre_order)
            else:
                pre_order.pop()



N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = []
for _ in range(B[0]):
    C.append('+')
for _ in range(B[1]):
    C.append('-')
for _ in range(B[2]):
    C.append('*')
for _ in range(B[3]):
    C.append('/')

order = [[]] #순서를 지정하는 리스트 만들기
pre_order = []
D = C
while D:
    make_order()

print(C)
#연산할 때는 순서에 해당하는 것에 맞춰 if연산을 통해 값을 계산해 나간다.