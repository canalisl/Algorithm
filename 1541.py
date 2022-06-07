import sys
sys.stdin = open('1541.txt')
input = sys.stdin.readline


# 문제 제대로 읽자!! 최소로!!

# 스플릿을 여러 개 기준으로 하는 법
# print(re.split('[+|-]', expression))

expression = input()

minusless = expression.split('-')
group = []
for num1 in minusless:
    sum2 = 0
    plusless = num1.split('+')
    for num2 in plusless:
        sum2 += int(num2)
    group.append(sum2)

min_result = group[0]
for i in range(1, len(group)):
    min_result -= group[i]

print(min_result)