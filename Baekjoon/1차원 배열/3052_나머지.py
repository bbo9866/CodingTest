n = []
for _ in range(10):
    a = int(input()) % 42
    n.append(a)

print(len(set(n)))
