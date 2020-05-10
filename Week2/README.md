### 최대공배수와 최소공배수

문제 링크 : [백준 2609번](https://www.acmicpc.net/problem/2609)

이 문제를 해결하기 위해 유클리드가 발견한 최대공약수의 성질을 이용했습니다.

> 유클리드가 발견한 최대공약수의 성질은 다음과 같습니다.
>
> * a 와 b의 최대공약수는 'b'와 'a를 b로 나눈 나머지'의 최대공약수와 같습니다. 즉, gcd(a,b) = gcd(b, a%b) 입니다.
> * 어떤 수와 0의 최대 공약수는 자기 자신입니다. 즉, gcd(n, 0) = n 입니다.
> * 최소공배수는 이러한 최대공약수로 두 수를 곱한 값을 나누면 구해집니다. 
>   
>   - 두 수 num1 과 num2가 있다고 할 때, A와 B는 각각 x * gcd(num1, num2), y*gcd(num1, num2)입니다. 따라서 num1 * num2 // gcd(num1, num2)를 해주면 최소공배수가 됩니다. 이 수가 최소공배수인 이유는 이 수를 A로 나눠도 나누어 떨어지고 B로 나눠도 나누어 떨어지는 수 중에서 가장 작은 수이기 때문입니다.

​		코드는 다음과 같습니다.

```python
import sys
# 두 숫자 받아오기
num1, num2 = list(map(int, sys.stdin.readline().split()))

def gcd(a, b):
  	# b가 0이 나오면 재귀호출을 종료한다.
    if b == 0:
        return a
    return gcd(b, a % b)


#최대공약수
print(gcd(num1,num2))
#최소공배수
print(num1 * num2 // gcd(num1,num2))

```



***



### 소수 찾기

문제링크 [백준 1978번](https://www.acmicpc.net/problem/1978)

소수의 정의 : 소수는 1과 자기자신 이외의 어떤 수로도 나누어지지 않는 수를 의미합니다. Prime number 라고 부릅니다.

```python
import sys


N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
#정답을 저장할 변수 ans 선언
ans = 0

def prime(num):
    if num == 1:
        #숫자 1은 소수가 아니므로 False를 return한다.
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        #range(2,num) 은 2부터 자기 자신을 제외한 수까지의 수들을 의미한다.
        if num % i == 0:
            #나누어 떨어지는 수가 있다면 소수가 아니므로 False를 return한다.
            return False
    return True


for i in num_list:
    #prime(i)가 True라면 소수개수를 저장하는 변수 ans의 개수를 늘려준다.
    if prime(i):
        ans += 1

print(ans)


```



***



### 골드 바흐의 추측

[백준 6588번](https://www.acmicpc.net/problem/6588)

 이 문제는 풀이하기 위해 많은 어려움이 있었다. 테스트 개수가 100,000개로 지정되어 있었기 때문에 최대한 효율적으로 풀지 않으면 코드가 맞더라도 시간초과가 발생하는 경우가 많았다.

먼저 이 문제에서는 백준 1978번 문제의 소수찾기 개념이 들어가는데 여기서는 소수를 찾을때도 최대한 효율적으로 찾아야 한다... 1978번 문제대로 풀게 되면 100% 시간초과가 발생할 수 있다.

이를 해결하기 위해서 소수를 찾는 효율적인 알고리즘 '에라토스테네스의 체'를 알아야한다.

> '에라토스테네스의 체' 알고리즘의 성질은 다음과 같다.
>
> * 2부터 소수를 구하고자 하는 구간까지의 모든 수를 나열하고 2는 소수이므로 먼저 소수를 모아둔 곳에 적어둔 다음 모든 2의 배수를 지웁니다.
> * 다음 남아있는 수 중에서 2로 나누어지지 않은 3이 소수이므로 소수를 모아두는 곳에 또 적어 둡니다. 그리고 모든 3의 배수를 지워줍니다.
> * 그러면 이제 다음으로 남아있는 5도 소수이므로 소수를 모아두는 곳에 적어둡니다. 다시 자기 자신인 5를 제외한 모든 5의 배수를 지워줍니다. 
> * 이 과정을 계속 반복하면 원하는 구간의 모든 소수를 구할 수 있습니다.



이러한 '에라토스테네스의 체' 알고리즘을 통해 소수를 구하면 더욱 쉽고 빠르게 원하는 숫자 구간 사이의 소수를 구할 수 있습니다. 이를 토대로 풀이 코드를 적어보면 다음과 같습니다.

```python
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    # n + 1 이어야 정확히 끝의 숫자까지 검사후 내뱉는다 주의!
    prime_check = [True] * (n + 1)
 
    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if prime_check[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n + 1, i): # i이후 i의 배수들을 False 판정
                prime_check[j] = False
 
    # 소수 목록 산출
    return [[i for i in range(2, n + 1) if prime_check[i] == True], prime_check]


primary_nums = prime_list(1000000)[0] # 실제 숫자 출력 리스트 
primary_bools = prime_list(1000000)[1] #True, False로 소수 구분되어 표시된 리스트

import sys
input = sys.stdin.readline

while(True): 
    N = int(input()) 
    if N == 0:  #0이 입력되면 반복문 바로 종료
        break 
    for i in range(N // 2):  
      # N//2까지 검사하면 웬만큼 다 검사한걸로 보면된다. 100,000전부 검사하면 시간초과 발생!
        if primary_bools[N-primary_nums[i]] == True:
             print("{} = {} + {}".format(N, primary_nums[i], N-primary_nums[i])) 
             break


```



***

### 프로그래머스 문제 : level1 실패율

[문제링크 프로그래머스 실패율](https://programmers.co.kr/learn/courses/30/lessons/42889)

 이 문제는 지금까지 풀어온 문제들과는 다르게 딕셔너리를 이용해서 푸는 문제였다. 그래서 그런지 아무리 고민해도 풀이 방법이 떠오르지 않았... 계속해서 리스트로만 풀려고 하다보니 답이 생각나지 않은 것 같다. 항상 모든 경우를 잘 생각해야 겠다.

그리고 count 함수를 항상 생각하자... 리스트 내에 해당값이 몇 번 출현하는지 개수를 구하는 문제는 많이 출제 되는 것 같다.

파이썬 count 함수 사용법 : **리스트이름.count(찾고자 하는 값)** 



```python
def solution(N, stages):
    #실패율이 저장될 딕셔너리 result
    result = {}
    #플레이어 수를 먼저 구해서 num에 담아준다.
    num = len(stages)

    #스테이지는 1번부터 있으므로 1부터 스테이지의 총 개수인 N까지 들어가기 위하여 N + 1로 선언
    for stage in range(1, N+1):
        # 플레이어 수가 0이 아니라면 
        if num != 0:
            #user 변수에 해당 스테이지에 머무르고 있는 플레이어가 몇 명인지 넣는다.
            user = stages.count(stage)
            #플레이어 수를 바탕으로 실패율을 구해준다. 
            #딕셔너리의 특징 '딕셔너리명[키] = 값' 이라고 선언하면 해당 딕셔너리에 저장된다. 
            result[stage] = user / num
            #플레이어 수만큼 다음 스테이지의 실패율을 구할 때 총 인원에서 빼준다.
            num -= user
        else:
            #이 문제에서 가장 중요한 부분 만약 총 스테이지가 5스테이지인데 3스테이지에서 전부 머무를 경우
            #그 다음 4스테이지, 5스테이지에 대한 실패율은 전부 0이 되는데 예외처리를 하지 않으면
            #오류가 발생하므로 반드시 예외처리를 해서 for문이 오류없이 끝까지 돌 수 있도록 해준다.
            result[stage] = 0
            
		#내림차순으로 출력하라 했으므로 reverse = True / 기준은 lambda 함수를 이용해서 실패율로 잡아준다.
    return sorted(result, key=lambda x : result[x], reverse=True)
```



