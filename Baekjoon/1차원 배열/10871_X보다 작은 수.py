n, x = map(int, input().split())
n_list = list(map(int, input().split()))
for i in n_list:
    if x > i:
        print(i, end=" ")
