# https://programmers.co.kr/learn/courses/30/lessons/67257
# https://www.youtube.com/watch?v=5UPS-lvZL2g


import re
import itertools
def solution(expression):
    operators = list(itertools.permutations(['-', '+', '*'], 3))
    expression = re.split('([-+*])', expression)
    
    answer = 0
    results = []
    
    for operator in operators:
        exp = expression[:]
        for op in operator:
            while op in exp:
                idx = exp.index(op)
                exp[idx-1] = str(eval(exp[idx-1]+op+exp[idx+1]))
                del exp[idx:idx+2]     
        results.append(abs(int(exp[0])))
    
    return max(results)