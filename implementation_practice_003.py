'''
8X8의 체스판이 있다.
a1, c5와 같이 좌표를 입력했을 때
나이트(L자 움직임)가 이동할 수 있는 경우의 수를 구하라.
'''

import time

start_time = time.time()
#########################

N = input()
knight = [N[0], N[1]]
hori = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
stadium = [8, 8]
cnt = 0

if knight[0] in hori:
    knight[0] = hori.index(knight[0]) + 1
    knight[1] = int(knight[1])

if knight[0] - 2 > 0:  # 왼쪽
    if knight[1] - 1 > 0 and knight[1] + 1 < 9:
        cnt = cnt + 2
    else:
        cnt = cnt + 1

if knight[0] + 2 < 9:  # 오른쪽
    if knight[1] - 1 > 0 and knight[1] + 1 < 9:
        cnt = cnt + 2
    else:
        cnt = cnt + 1

if knight[1] - 2 > 0:  # 위
    if knight[0] - 1 > 0 and knight[0] + 1 < 9:
        cnt = cnt + 2
    else:
        cnt = cnt + 1

if knight[1] + 2 < 9:  # 아래
    if knight[0] - 1 > 0 and knight[0] + 1 < 9:
        cnt = cnt + 2
    else:
        cnt = cnt + 1

print(cnt)

#########################
end_time = time.time()
print('time :', end_time - start_time)
