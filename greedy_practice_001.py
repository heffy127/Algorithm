'''
N개의 정수가 들어있는 배열이 있음
배열이 주어질 때 주어진 수를 M번 더해서 가장 큰 수를 만들어야함
단, 특정 인덱스에 해당하는 수가 연속 K번을 초과할 수 없음
가장 큰 결과값을 구하시오
'''

import time

start_time = time.time()
#########################
import random

N, M, K = map(int, input().split(' '))
data = [random.randrange(1, 9) for i in range(N)]


def cal(N, M, K, arr):
    arr.sort()
    no1 = arr[-1]
    no2 = arr[-2]
    answer = 0
    cnt = K

    for _ in range(8):
        if cnt == 0:
            answer = answer + no2
            cnt = K
        else:
            answer = answer + no1
            cnt = cnt - 1

    return answer


fin = cal(N, M, K, data)
print(data)
print(fin)

#########################
end_time = time.time()
print('time :', end_time - start_time)
