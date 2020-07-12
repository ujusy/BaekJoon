import sys
from collections import Counter
a = int(input())
b = int(input())
c = int(input())
result=list(str(a*b*c))
counter=Counter(result)
counter=sorted(counter.items())

answer=[0 for  i in range(10)]
for i in range(len(counter)):
    b=int(counter[i][0])
    answer[b]=counter[i][1]

for i in range(len(answer)):
    print(answer[i])
    