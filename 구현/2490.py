from collections import Counter

counter=[[int(x) for x in input().split()] for y in range(3)]

dic={1: 'A',2: 'B',3: 'C',4: 'D',0: 'E'}
for i in range(3):
    counter[i] = Counter(counter[i])
    b = counter[i][0]
    print(dic[b])