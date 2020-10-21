str_list = input()
result = []
value = 0

for x in str_list:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
        
#알파벳을 오름차순으로 정렬
result.sort()

if value != 0:
    result.append(str(value))

#최종 결과 출력 리스트를 문자로
print(''.join(result))