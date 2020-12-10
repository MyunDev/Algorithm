# https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = [0, 0]
    cnt = 1

    for idx in range(1, len(words)):
        word = words[idx]
        cnt %= n

        if(word in words[0: idx]) or (words[idx - 1][-1] != word[0]):
            answer = [cnt + 1, 1 + idx// n]
            return answer
        cnt += 1

    return answer

