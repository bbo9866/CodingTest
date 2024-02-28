n = int(input())
cnt = n

for i in range(n):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:  # word[j] 와 다음 문자가 같으면
            pass   # j+1로 넘어가기
        elif word[j] in word[j+1:]:  # word[j] != word[j+1] 다르고, word[j+1] 이후에 word[j]와 같은 문자가 있으면
            cnt -= 1  # cnt - 1
            break
print(cnt)
