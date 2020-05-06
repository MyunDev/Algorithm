

import sys

N = list(sys.stdin.readline().split())

ans_num = []

num_list = []

def prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True




def find_num(N):
    for i in N:
        for j in N:
            if i + j == N and prime(i) and prime(j):
                ans_num.append(i)
                ans_num.append(j)
            print('Goldbachs conjecture is wrong.')
    if len(ans_num) > 2:
        for x in range(1,len(ans_num),2):
            num_list.append(ans_num[x] - ans_num[x - 1])
            num_list.sort()
    

    print( '{} = {} + {}'.format(N, num_list[-1], num_list[-2]))



print(find_num(N))













