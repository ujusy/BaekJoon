import sys
N, K = map(int,sys.stdin.readline().split(' '))
s =[]
for _ in range(N):
    s.append(int(input()))
s.reverse()
answer = 0
a = 0
for i in range(len(s)):
    a = int(K/s[i])
    if a == 0:
        continue
    answer = answer + a
    K  = K%s[i]
print(answer)


