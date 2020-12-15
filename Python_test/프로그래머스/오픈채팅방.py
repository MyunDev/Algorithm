#나의시도
def solution(record):
    answer = []
    
    #record 리스트 명령문으로 구분해서 넣기
    new_list = []
    for i in range(len(record)):
        new_list.append(record[i].split())
    
    result = []
    user_dict = {}
    for i in range(len(new_list)):
        
        if new_list[i][0] == "Enter":
            result.append(new_list[i][2]+'님이 들어왔습니다.')
            user_dict[new_list[i][1]] = new_list[i][2]
       
        if new_list[i][0] == "Leave":
            result.append(user_dict[new_list[i][1]]+'님이 나갔습니다.')
            
        if new_list[i][0] == "Change":
            
            user_dict[new_list[i][1]] = new_list[i][2]
            
            
            
    print(user_dict)
    return result