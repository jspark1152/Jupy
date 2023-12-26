N = int(input())

listx = []
listy = []
for i in range(N):
    A, B = map(int, input().split())
    listx.append(A)
    listy.append(B)

listx.sort()
listy.sort()

result = (listx[-1]-listx[0])*(listy[-1]-listy[0])
print(result)