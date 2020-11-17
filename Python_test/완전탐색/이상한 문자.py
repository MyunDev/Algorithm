
# https://pjs21s.github.io/make-weird-sentence/

def solution(s):
    new_list = s.split()
    new_word = ""
    for word in new_list:
        for i, spell in enumerate(word):
            if i % 2 == 0:
                new_word += spell.upper()
            else:
                new_word += spell.lower()
        answer += " "
    
    return new_word[:-1]
