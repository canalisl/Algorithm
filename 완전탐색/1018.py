import sys, pprint
sys.stdin = open('1018.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
new = [[] * 8 for _ in range(8)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 'W' and board[i][j+2] == 'B':
            new[i][j].append(board[i][j])
