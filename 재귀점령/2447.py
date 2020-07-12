# n = int(input())
# a=[]
# b=[]
# for _ in range(n):
#     s, o = map(int,input().split(' '))
#     a.append(s)
#     b.append(o)

# print(a)
# print(b)

# def min(a,b):
#     for i in range(len(a)):

people = list(map(int,input().split()))

limit =  int(input())
def solution(people, limit):
    answer = 0
    people.sort()
    people.reverse()
    for _ in range(len(people)):
        if len(people) ==1 :
            people.remove(people[0])
            answer += 1
        elif len(people) == 0:
            answer += 0
        elif people[0] == limit:
            people.remove(people[0])
            answer += 1
        elif people[0] + people[len(people)-1] <= limit:
            people.remove(people[0])
            people.remove(people[len(people)-1])
            answer +=1
        else:
            people.remove(people[0])
            answer += 1

    return answer
print(solution(people,limit))