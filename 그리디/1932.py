n = int(input())    # 회의 수

ct = []
b = []
answer = 0
start  = 0
for _ in range(n):
    ct.append(list(map(int, input().split())))
ct = sorted(ct, key = lambda x:x[0])
ct = sorted(ct, key = lambda x:x[1])

for i in range(len(ct)):
    if ct[i][0] >= start:
        start = ct[i][1]
        answer += 1
print(answer)