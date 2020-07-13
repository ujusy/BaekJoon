# The candy war : 9037

------------

## 문제

알고리즘 유치원 선생님인 영희는 간식시간이 되자 아이들에게 사탕을 나누어 주려고 하였다. 하지만 욕심 많고 제멋대로인 유치원 아이들은 차례대로 받으라는 선생님의 말을 무시한 채 마구잡이로 사탕을 집어 갔고 많은 사탕을 집어 간 아이가 있는가 하면 사탕을 거의 차지하지 못하고 우는 아이도 있었다. 

말로 타일러도 아이들이 말을 듣지 않자 영희는 한 가지 놀이를 제안했다. 일단 모든 아이들이 원으로 둘러 앉는다. 그리고 모든 아이들은 동시에 자기가 가지고 있는 사탕의 절반을 오른쪽 아이에게 준다. 만약 이 결과 홀수개의 사탕을 가지게 된 아이가 있을 경우 선생님이 한 개를 보충해 짝수로 만들어 주기로 했다. 흥미로워 보이는 이 놀이에 아이들은 참여 했고 이 과정을 몇 번 거치자 자연스럽게 모든 아이들이 같은 수의 사탕을 가지게 되어 소란은 종료되었다.

자기가 가진 사탕의 반을 옆에 오른쪽에 앉은 아이에게 주는 과정과 선생님이 사탕을 보충해 주는 과정을 묶어서 1 순환이라고 할 때 몇 번의 순환을 거치면 모든 아이들이 같은 수의 사탕을 가지게 되는지 계산 해보자. 단, 처음부터 홀수개의 사탕을 가지고 있으면 선생님이 짝수로 보충을 먼저 해주며 이 경우 순환수에 들어가지 않는다. 선생님은 충분한 수의 사탕을 갖고 있다고 가정하자.

## 입력

입력은 표준입력(standard input)을 통해 받아들인다. 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 각각의 테스트 케이스의 첫 줄에는 아이의 인원 N (1 ≤ N ≤ 10)이 주어지고 그 다음 줄에는 각 아이들이 초기에 가지고 있는 사탕의 개수 Ci ( 1 ≤ i ≤ N, 1 ≤ Ci ≤ 30)가 주어진다. 분배 시 C1의 오른쪽에는 C2가, C2의 오른쪽에는 C3가…… 같은 식으로 앉게 되며 CN의 오른쪽에는 C1이 앉게 된다.

## 출력

출력은 표준출력(standard output)을 통하여 출력한다. 각 테스트 케이스에 대하여 모든 아이가 같은 개수의 사탕을 가질 때까지 몇 순환이 걸리는지 출력하시오.

 ## Think

>총 두개의 리스트를 두어 입력을 받으면 좋을 것 같다고 생각했다. 입력받은 인원 수 많을 저장하는 리스트와 각각 리스트의 사탕개수 리스트를 두었다. 지금 이 문제의 목표는 **오른쪽 아이에게 주는 과정 + 선생님이 사탕을 보충해주는 과정** 의 순환수를 물어보는 것인데. 맨 처음에 보충해주는 것은 순환수에 포함이 되지 않으므로 나는 주는 과정을 중심으로 순환수를 계산하였다. 
>
>모두 같은 수를 만들기 위해 반복하기 전 내가 정의한 함수 makeList를 이용하여 홀수인 부분을 짝수로 만들어 주었다. 그리고 한번에 모두 같은 수가 된경우 (set을 이용하여 중복제거하여 그 길이가 1인것으로 판별) 결과를 반환할 리스트에 append해주었다. 
>
>이러한 경우가 아닌경우 while문으로 들어가 반을 나누어 옆사람에게(shift right - rotate 지정 함수 사용) 주고 홀수를 짝수로 만들고를 반복하며 또 다시 set을 이용하여 모든 같은 수가 된 경우를 판별해 주었다. 



## Code

```python
import sys
T = int(sys.stdin.readline())
memeber = []
allList = []
def makeList(mlist):
    for j in range(len(mlist)):
        if mlist[j] % 2 == 1:
            mlist[j] = mlist[j] + 1
    return mlist
def rotate(l, n):
    return l[-n:] + l[:-n]
for _ in range(T):
    memeber.append(int(sys.stdin.readline()))
    candy = list(map(int, sys.stdin.readline().split()))
    allList.append(candy)
result = []
shiftlist = []
cnt = 0
check = True
for i in range(T):
    check = True
    makeList(allList[i])
    if (len(list(set(allList[i]))) == 1):
        check = False
        result.append(cnt)
    while check:
        cnt = cnt + 1
        tmplist = [item // 2 for item in allList[i]]
        shiftlist = rotate(tmplist, 1)
        allList[i] = [x+y for x,y in zip(shiftlist,tmplist)]
        allList[i] = makeList(allList[i])
        if(len(list(set(allList[i]))) == 1):
            check = False
            result.append(cnt)
            cnt =0
for item in result:
    print(item)
```



## 느낀점

>일단 문제자체가 딱 처음에 읽고 이해가 쉽지않았다. 명확히 생각나는 자료구조도 없었을 뿐더러 구현을 하면 할 수록 복잡해 짐을 느꼇다. 
>
>나름 나누어본다고 공통으로 사용되는 몇가지는 함수로 만들어 사용했으나 코드의 가독성이 떨어지고 시간복잡도와 공간복잡도가 높은등 좋은 코드는 아니라고 생각한다. .. 노력해야겠다. ㅜ



## 다른 사람의 코드로 공부해 보자

https://chancoding.tistory.com/75

이 분의 코드를 보았는데.. 내것이랑 너무 차이난다. ㅋㅋㅋㅋㅋㅋ 

