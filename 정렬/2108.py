import sys
sys.stdin = open('2108.txt')
input = sys.stdin.readline

N = int(input())
array = [int(input()) for _ in range(N)]
array.sort()

av = round(sum(array)/N)
mean = array[N // 2]
print(av)
print(mean)
cnt = []
max_list = []
set_array = set(array)
for num in set_array:
    cnt.append(array.count(num))
# print(set_array)
for k in range(len(cnt)):
    if cnt[k] == max(cnt):
        max_list.append(list(set_array)[k])
# print(max_list)
if len(max_list) >= 2:
    max_list.sort()
    print(max_list[1])
print(max(array) - min(array))