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
