import sys
sys.stdin = open('1427.txt')
input = sys.stdin.readline

N = list(map(int, input()))
N = sorted(N, reverse=True)
new_str = ''
for num in N:
    new_str += str(num)
print(new_str)