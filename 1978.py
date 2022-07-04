import sys
sys.stdin = open('1978.txt')
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
no_prime = []

for num in numbers:
    # 1은 소수 아님
    if num == 1:
        no_prime.append(1)
    else:
        for i in range(1, num + 1):
            if (i != 1 and i != num) and num % i == 0:
                # remove로 지워버리면 첫 반복문에서 다음 num 찾을 때 건너뜀
                # [1, 3, 4, 5, 7] -> 4지우면 그 다음 num = 7
                # 소수 아닌걸 지우지 말고 새로운 배열에 추가하는 방향으로!
                no_prime.append(num)
                break

print(len(numbers) - len(no_prime))