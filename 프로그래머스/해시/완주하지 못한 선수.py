from collections import defaultdict

def solution(participant, completion):
    answer = ''
    marathon = defaultdict(int)
    for person in participant:
        marathon[person] += 1
    for human in completion:
        marathon[human] -= 1
    for key, value in marathon.items():
        if value != 0:
            answer = key
    return answer