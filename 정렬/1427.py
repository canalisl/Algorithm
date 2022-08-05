import sys
sys.stdin = open('1427.txt')
input = sys.stdin.readline

# readline으로 입력 받을 때는 rstrip() 항상 주의!
# rstrip() 안 붙이니까 백준에서 ValueError 계속 발생!
N = list(map(int, input().rstrip()))
N = sorted(N, reverse=True)
print("".join(map(str, N)))