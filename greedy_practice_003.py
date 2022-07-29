'''
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 수행하고자 함
단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택 가능
 1. N에서 1빼기
 2. N을 K로 나누기
'''
import time

start_time = time.time()
#########################

N, K = map(int, input().split(' '))


def main(N, K):
    cnt = 0
    while True:
        cnt = cnt + 1

        if N % K:
            N = N - 1
        else:
            N = N // K

        if N == 1:
            break

    print(cnt)


main(N, K)

#########################
end_time = time.time()
print('time :', end_time - start_time)
