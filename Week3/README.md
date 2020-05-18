백준 10845번](https://www.acmicpc.net/problem/10845)

알고리즘의 가장 기초 부분이라 할 수 있는 큐를 구현해 보았습니다.

 큐는 먼저 집어 넣은 데이터가 먼저 나오는 **FIFO(First In First Out)** 구조로 저장하는 형식을 말한다. 영어 단어 queue는 표를 사러 일렬로 늘어선 사람들로 이루어진 줄을 말하기도 하며, 먼저 줄을 선 사람이 먼저 나갈 수 있는 상황을 연상하면 된다.

출처: 위키백과

```python
import sys

# 몇 줄의 명령어를 입력할 것인지 변수 N에 저장 후 출력
N = int(sys.stdin.readline())
#명령어를 저장할 공간이자 큐를 구현할 빈 리스트 선언 
qu = []

#여기서 k는 의미가 없는건가?!
for k in range(N):
  	#명령어 리스트로 받아오기
    cmd_list = list(sys.stdin.readline().split())
    if cmd_list[0] == 'push':
      	#push 1을 입력할 경우 ['push','1'] 이런 형식으로 들어가므로 cmd_list[1]을 append해야 한다.
        qu.append(cmd_list[1])
    elif cmd_list[0] == 'pop':
        if qu:
            print(qu[0])
            # 0 번째 인덱스 값 pop
            qu.pop(0)
        else:
            print(-1)
    elif cmd_list[0] == 'size':
        print(len(qu))
    elif cmd_list[0] == 'empty':
        if qu:
            print(0)
        else:
            print(1)
    elif cmd_list[0] == 'front':
        if qu:
            print(qu[0])
        else:
            print(-1)
    elif cmd_list[0] == 'back':
        if qu:
            print(qu[-1])
        else:
            print(-1)
```





