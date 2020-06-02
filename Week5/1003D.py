a = int(input())
 
zero = [1,0,1]
one = [0,1,1]
 
def cal(num):
    length = len(zero)
    if length <= num:
        for i in range(length,num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print("%d %d"%(zero[num],one[num]))
 
for i in range(a):
    k = int(input())
    cal(k)





#입력 값 3에 대한 0 호출회수 = (입력 값 2에 대한 0 호출회수) + (입력 값 1에 대한 0 호출회수)
#입력 값 3에 대한 1 호출회수 = (입력 값 2에 대한 1 호출회수) + (입력 값 1에 대한 1 호출회수)
#fibonacci(4) = fibonacci(3) + fibonacci(2) 이므로,
#입력 값 4에 대한 0 호출회수 = (입력 값 3에 대한 0 호출회수) + (입력 값 2에 대한 0 호출회수)
#입력 값 4에 대한 1 호출회수 = (입력 값 3에 대한 1 호출회수) + (입력 값 2에 대한 1 호출회수)


