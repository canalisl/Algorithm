import sys
sys.stdin = open('11720.txt')
input = sys.stdin.readline

# rstrip() 안쓰니까 런타임에러(ValueError) 뜸
# readline() 쓸 때는 습관적으로 rstrip()을 써주자!
N = int(input().rstrip())
numbers = list(map(int, input().rstrip()))
print(sum(numbers))

# print(type(int('2\n'))) -> <class 'int'>
