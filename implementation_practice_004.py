'''
첫째줄 : 맵의 세로크기 X 가로크기
둘째줄 : 게임 캐릭터의 좌표, 방향 (0~3)(북동남서)
셋째줄 : 맵 크기에 따라 육지는 0, 바다는 1
캐릭터는 육지만 다닐 수 있으며 한번 갔던곳은 다시 못감
무조건 육지에서 스타팅되며 왼쪽으로만 돌면서 걸을 수 있음
캐릭터가 방문한 칸의 수 구하라.
'''
import time

start_time = time.time()
#########################
import sys

map_size = list(map(int, sys.stdin.readline().rstrip().split(" ")))
player = list(map(int, sys.stdin.readline().rstrip().split(" ")))
player_pos = player[:2]
direction = player[-1]

# 좌로 보기
def turn_left():
  global direction
  direction = direction - 1
  if direction == -1:
    direction = 3

def success_setting(next_x, next_y):
  global game_map
  global player_pos
  global condition
  global cnt
  game_map[next_x][next_y] = 1
  player_pos = [next_x, next_y]
  condition = 0
  cnt = cnt + 1

# 이동 카운트
cnt = 0

game_map = [ list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(map_size[0])]
print(game_map)

# 이동 시도 카운트
condition = 0

# 최초 지점 처리
game_map[player_pos[0]][player_pos[1]] = 1
cnt = cnt + 1

while True:
  if condition == 4:
    break
  turn_left()
  if direction == 0 : # 북
    next_x = player_pos[0]
    next_y = player_pos[1]-1
    if next_y == 0 or game_map[next_x][next_y] == 1:
      condition = condition + 1
      continue
    success_setting(next_x, next_y)
    
  elif direction == 1: # 동
    next_x = player_pos[0]-1
    next_y = player_pos[1]
    if next_x == 0 or game_map[next_x][next_y] == 1:
      condition = condition + 1
      continue
    success_setting(next_x, next_y)
    
  elif direction == 2: # 남
    next_x = player_pos[0]
    next_y = player_pos[1]+1
    if next_y == map_size[1] or game_map[next_x][next_y] == 1:
      condition = condition + 1
      continue
    success_setting(next_x, next_y)
  
  else:  #서
    next_x = player_pos[0]+1
    next_y = player_pos[1]
    if next_x == map_size[0] or game_map[next_x][next_y] == 1:
      condition = condition + 1
      continue
    success_setting(next_x, next_y)

print(cnt)


#########################
end_time = time.time()
print('time :', end_time - start_time)
