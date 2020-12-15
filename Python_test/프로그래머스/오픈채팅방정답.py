# https://programmers.co.kr/learn/courses/30/lessons/42888
# https://www.youtube.com/watch?v=IqaMiOjJBM4

def solution(records):
    records = list(map(lambda r: r.split(), records))
    
    users = {}
    for record in records:
        if len(record) > 2: 
            users[record[1]] = record[2]
     
    msg = { 'Enter': '님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    msgs = []
    for record in records:     
        #Change인 경우는 위에서 걸렀음
        if record[0] != 'Change':
            msgs.append(users[record[1]]+ msg[record[0]])
        
    return msgs