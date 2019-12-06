n = int(input())
wh = []
for _ in range(n):
    wh.append(int(input()))
wh.sort()
for i in range(n):
    wh[i] = wh[i]*(n-i)
print(max(wh))

# 로프
# 주어진 로프의 무게를 배열로 넣고 정렬
# 정렬 후 각각 정렬 한 곳에 로프의 개수를 곱해주어 가장 큰거 뽑기