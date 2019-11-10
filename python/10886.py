import sys
n = int(sys.stdin.readline())
num =0;num2 = 0
for i in range(n):
    a=int(input())
    if a == 1:
        num=num+1
    elif a == 0:
        num2=num2+1

if num>num2: print("Junhee is cute!")
else: print("Junhee is not cute!")