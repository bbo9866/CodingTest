chess = [1, 1, 2, 2, 2, 8]

a = list(input().split())

for i in range(len(chess)):
    print(chess[i] - int(a[i]), end=' ')
