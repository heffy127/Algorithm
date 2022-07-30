'''
여행가 A는 N X N 크기의 정사각형 공간위에 있다.
가장 왼쪽 위는 (1,1)이며 가장 오른쪽 아래는 (N,N)이다.
정사각형을 벗어나는 이동은 무효라 할 때
입력된 루트에 따른 여행가의 위치 좌표를 구하라.
'''
import time

start_time = time.time()
#########################
import sys

N = int(input()) # 공간 크기
ROUTE = sys.stdin.readline().rstrip() # 루트

route_list = ROUTE.split(" ")
travler = [1,1] # 행열


for way in route_list:
  if way == 'R':
    if travler[1] == N:
      continue
    travler[1] = travler[1] + 1
    
  elif way == 'L':
    if travler[1] == 1:
      continue
    travler[1] = travler[1] - 1
    
  elif way == 'U':
    if travler[0] == 1:
      continue
    travler[0] = travler[0] - 1
  else: # 'D'
    if travler[0] == N:
      continue
    travler[0] = travler[0] + 1

print(' '.join(map(str, travler)))
    
#########################
end_time = time.time()
print('time :', end_time - start_time)