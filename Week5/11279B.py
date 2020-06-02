import heapq
import sys
heap = []

#파이썬 내부 모듈에는 최소 힙인 heapq만 지원해 최대 힙으로 바꾸기 위해 음수로 바꿔준 후 최대값을 출력한다.
#https://hooongs.tistory.com/130

for _ in range(int(input())):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (-num))
    else:
        if not heap:
            print(0)
        else:
            print(-1 * heapq.heappop(heap))