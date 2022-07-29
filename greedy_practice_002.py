'''
숫자가 쓰인 카드들이 N(행) X M(열) 형태로 놓여있음
뽑고자 하는 카드가 포함된 행을 우선 선택
그 다음 선택된 행에 포함된 카드들 중 가장 낮을 카드를 뽑았을 때
최종적으로 가장 높은 카드를 골라야 함
'''
import time

start_time = time.time()
#########################
N,M = map(int, input().split(' '))
data = []
for i in range(N):
  data.append(list(map(int, input().split(' '))))


def main(N,M,arr):
  sort_arr = [ sorted(i) for i in arr ]
  first_arr = [ i[0] for i in sort_arr]
  return max(first_arr)


print(main(3,3,data))
  
  

#########################
end_time = time.time()
print('time :', end_time - start_time)