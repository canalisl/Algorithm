from collections import defaultdict

def solution(clothes):
    answer = 1
    clothesDict = defaultdict(list)
    for item in clothes:
        clothesDict[item[1]].append(item[0])
    # 각 종류마다 (종류 + 1)의 경우의 수 있음
    # ex. 모자 : a, b -> 모자 a 쓰기, 모자 b 쓰기, 아무것도 안쓰기
    for array in clothesDict.values():
        answer = answer * (len(array) + 1)
    # 아무 종류의 옷도 안 입는 경우 빼주기
    return answer - 1