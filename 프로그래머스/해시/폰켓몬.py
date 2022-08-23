def solution(nums):
    answer = 0
    takeCnt = len(nums) / 2
    if takeCnt <= len(set(nums)):
        answer = takeCnt
    else:
        answer = len(set(nums))
    return answer