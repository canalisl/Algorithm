# set을 이용한 풀이
def solution(nums):
    answer = 0
    takeCnt = len(nums) / 2
    if takeCnt <= len(set(nums)):
        answer = takeCnt
    else:
        answer = len(set(nums))
    return answer


# hash(딕셔너리)를 이용한 풀이
from collections import defaultdict

def solution(nums):
    answer = 0
    pokemon = defaultdict(int)
    for cnt in nums:
        pokemon[cnt] += 1
    takeCnt = len(nums) / 2
    if takeCnt <= len(pokemon):
        answer = takeCnt
    else:
        answer = len(pokemon)
    return answer