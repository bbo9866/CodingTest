dial_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()

time = 0

for unit in dial_list:
    for x in unit:
        for i in word:
            if i == x:
                time += dial_list.index(unit)+3

print(time)
