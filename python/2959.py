abcd=list(map(int,input().split()))
abcd.remove(max(abcd))
print(min(abcd)*max(abcd))
