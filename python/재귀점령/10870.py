n = int(input())
        
def fibo(n):
    a,b = 1,0
    for _ in range(n):
        a,b = b, a+b
    return b

print(fibo(n))