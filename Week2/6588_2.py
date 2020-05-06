def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * (n + 1)
 
    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n + 1, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False
 
    # 소수 목록 산출
    return [[i for i in range(2, n + 1) if sieve[i] == True], sieve]


primary_nums = prime_list(1000000)[0] 
primary_bools = prime_list(1000000)[1]
r = 100000

import sys
input = sys.stdin.readline

while(True): 
    N = int(input()) 
    if N == 0: 
        break 
    for i in range(N // 2): 
        if primary_bools[N-primary_nums[i]] == True:
             print("{} = {} + {}".format(N, primary_nums[i], N-primary_nums[i])) 
             break

