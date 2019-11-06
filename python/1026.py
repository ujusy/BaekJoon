import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split(' ')))
B = list(map(int, sys.stdin.readline().split(' ')))
result = 0

for _ in range(N):
    result += A.pop(A.index(min(A))) * B.pop(B.index(max(B)))
print(result)