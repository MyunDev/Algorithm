# https://scarletbreeze.github.io/articles/2019-07/pythonKit%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4(4)%ED%83%90%EC%9A%95%EB%B2%95%ED%81%B0%EC%88%98
# https://programmers.co.kr/learn/courses/30/lessons/42883
def solution(number, k):
    collected = []  # 숫자를 모아서 큰 수를 만들 때 쓰일 배열
    # 문자열에도 모을 수 있지만 문자열은 immutable(값이 변하지 않는)특성을 가지기에 코드 효율은 리스트(mutable)다 더 좋다
    # call by value , call by reference와 동일한 개념
    for i, num in enumerate(number):
        # k개 만큼의 숫자를 빼냈을 때, i의 인덱스를 기억하기 위해서 i를 사용
        while len(collected) > 0 and collected[-1] < num and k > 0:
            # 1. 맨 마지막 문자만 비교를 하면 될까? -> 그렇다. 지금까지 원칙을 지켜서 쌓아 왔다면 지금까지 쌓인 숫자들은 내림차순으로 되어있다.
            # 2. collected의 마지막 원소는 한 문자로 이루어진 문자열이다. num 또한 한 글자 짜리 문자열이다. 이걸 정수로 변환하지 않고,
            # 두개의 문자열에 대해서 대소관계를 이용해도 괜찮은가? -> 괜찮다. 알파벳 순서에 따르면 0은 1보다 작고, 3은 2보다 크고, 수의 크기 대소관계와 같다.
            # ※ 길이가 2 이상이라면, 사전에 나타난 숫자가 되겠지만, 지금은 한글자 짜리기 때문에 정수 변환이 필요없다.
            collected.pop()  # 리스트이 맨 끝에 있는 원소 하나를 없앤다.
            k -= 1
        if k == 0:
            collected += list(number[i:])
            break
        collected.append(num)
    
    
    collected = collected[:-k] if k > 0 else collected
    # k가 0 이면 빈 리스트가 되기 때문에 if를 이용해서 조건을 걸어준다.
    answer = ''.join(collected)
    return answer