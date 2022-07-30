'''
정수 N이 입력되면 00시00분00초부터 N시00분00초까지의 모든 시각 중 
3이 하나라도 포함되어 있는 시각의 개수를 구하라.
'''
import time

start_time = time.time()
#########################

N = int(input())
cnt = 0

for hour in range(N+1):
  for minute in range(60):
    for second in range(60):
      time_list = [hour, minute, second]
      time_str = "".join(map(str,time_list))
      if '3' in time_str:
        cnt = cnt + 1

print(cnt)

#########################
end_time = time.time()
print('time :', end_time - start_time)