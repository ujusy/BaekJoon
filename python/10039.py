import sys
answer=0
for _ in range(5):
    score=int(sys.stdin.readline())
    if score < 40:
        score=40
    answer=answer+score

print(int(answer/5))
