# 하노이 다시 생각해보기
n = int(input())

answer = []
def hn(n,a,b,c):
    if  n == 1:
        print(a, c)
    else:
        hn(n-1,a,c,b)
        print(a, c)
        hn(n-1,b,a,c)

sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1
print(sum)
hn(n, 1, 2, 3)