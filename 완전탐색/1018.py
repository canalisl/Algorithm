import sys, pprint
sys.stdin = open('1018.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
new = [[] * 8 for _ in range(8)]
cnt = []
for i in range(N - 7):  # i : 0 1 2
    for j in range(M - 7):  # j : 0 1 2 3 4 5
        # 시작점을 주어진대로 할 필요 X
        # 시작점도 B or W를 선택해서 칠할 수 있음
        w_start = 0 # 시작점을 W로 해서 체스판을 만들 경우
        b_start = 0 # 시작점을 B로 해서 체스판을 만들 경우
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                # 가로세로 위치 합이 짝수면 시작점 색이랑 같아야함
                if (a + b) % 2 == 0:
                    if board[a][b] == 'B':
                        w_start += 1
                    elif board[a][b] == 'W':
                        b_start += 1
                else:   # 홀수면 달라야함
                    if board[a][b] == 'B':
                        b_start += 1
                    elif board[a][b] == 'W':
                        w_start += 1
        cnt.append(w_start)
        cnt.append(b_start)
print(min(cnt))

