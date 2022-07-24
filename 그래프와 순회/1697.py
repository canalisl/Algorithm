import sys
sys.stdin = open('1697.txt')
input = sys.stdin.readline


def find_kids(n, k):
    global time
    print(f'n - {n} // k - {k} // time - {time}')
    if abs(2*n - k) < abs(n - k):
        # 순간이동 한 위치 ~ 동생 위치 < 지금 위치 ~ 동생위치
        # 일때만 순간이동 하는게 이득임
        time += 1
        find_kids(2*n, k)
    else:
        time += abs(n - k)


N, K = map(int, input().split())
time = 0
find_kids(N, K)
print(time)