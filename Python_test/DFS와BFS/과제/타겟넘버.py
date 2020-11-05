def solution(numbers, target):
    sup = [0]
    for i in numbers:
        sub = []
        for j in sup : 
            sub.append(j+i)
            sub.append(j-i)
        sup = sub
    return print(sup.count(target))

solution([1,1,1,1,1], 3)