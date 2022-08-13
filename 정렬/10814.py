import sys
sys.stdin = open('10814.txt')
input = sys.stdin.readline

N = int(input())
info = []
for _ in range(N):
    age, name = input().split()
    age = int(age)
    info.append((age, name))
# info.sort()   이걸 쓰면 나머지 요소가 뒤섞임
info.sort(key=lambda x: x[0])   # 나머지 요소 기존 순서 유지
for (age, name) in info:
    print(age, name)