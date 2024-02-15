n, m = map(int, input().split())
# basket = []
# for i in range(n):
#     basket.append(i+1)
basket = [i for i in range(1, n+1)]

# for _ in range(m):
#     a, b = map(int, input().split())
#     tmp = basket[a-1]
#     basket[a-1] = basket[b-1]
#     basket[b-1] = tmp

for _ in range(m):
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

for x in range(n):
    print(basket[x], end=' ')
