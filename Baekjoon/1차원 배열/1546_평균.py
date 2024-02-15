n = int(input())

score = list(map(int, input().split()))
max_score = max(score)

new_score = []
for i in score:
    a = i/max_score*100
    new_score.append(a)

avg = sum(new_score) / n
print(avg)
