import sys
n = int(input())
time = list(map(int,sys.stdin.readline().split(' ')))
time.sort()
answer = 0
for i in range(1,n):
    time[i] = time[i] + time[i-1]
for i in range(n):
    answer = answer + time[i]
print(answer)
