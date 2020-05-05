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








