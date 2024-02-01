H, M = map(int, input().split())
M1 = int(input())

H += M1 // 60
M += M1 % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H, M)
