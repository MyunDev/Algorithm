# https://programmers.co.kr/learn/courses/30/lessons/17682
# https://www.youtube.com/watch?v=_MrSCUdMJ34

import re
def solution(dartResult):
    result = []
    #문자 변환에 필요한 딕셔너리
    charConv = {'S': '**1', 'D': '**2', 'T': '**3', '#': '*-1'}
    
    # 1. 입력된 문자열 분할
    parser = re.sub('([SDT][*#]?)', '\g<1> ',dartResult).split()
    
    # 2. 분할된 문자열을 문제의 요구사항에 맞춰서 변환
    for parse in parser: 
        for word in parse:
            #딕셔너리의 get 메소드 활용
            #charConv['S']  == charConv.get('S')
            #.get() 메소드의 두번 째 파라미터는 첫번째 키값 파라미터가 존재하지 않으면
            # 두번째 파라미터를 출력함
            #replace(a, b) a를 b로 대체함
            parse = parse.replace(word, charConv.get(word, word))
        
        if parse[-1] == '*':
            parse += '2'
            #result에 값이 존재한다면
            if result:
                result[-1] = result[-1][:-1] + '*2+'
        parse += '+'       
        result.append(parse)
    
    # 3. 변환된 문자열의 연산값 반환 
    return eval(''.join(result)[:-1])