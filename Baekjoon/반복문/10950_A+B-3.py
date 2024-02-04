t = int(input())
sum = []
for i in range(0, t):
    a, b = map(int, input().split())
    sum.append(a+b)

for j in range(len(sum)):
    print(sum[j])
