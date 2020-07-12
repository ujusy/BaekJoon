a = input()
b = a.split('-')
for i in range(len(b)):
    answer = 0
    if '+' in b[i]:
        c =list(map(int,b[i].split('+')))
        for j in range(len(c)):
            answer = answer + c[j]
        b[i] = answer
    else:
        b[i] = int(b[i])
answer = b[0]
for i in range(1,len(b)):
    answer = answer-b[i]
print(answer)