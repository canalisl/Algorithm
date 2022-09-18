from collections import defaultdict

def solution(survey, choices):
    answer = ''
    score = defaultdict(int)
    for i in range(len(survey)):
        if choices[i] > 4:
            score[survey[i][1]] += choices[i] - 4
        elif choices [i] < 4:
            score[survey[i][0]] += 4 - choices[i]
        else:
            pass
        
    types = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    for type in types:
        type.sort()
        if score[type[0]] >= score[type[1]]:
            answer += type[0]
        else:
            answer += type[1]
            
    return answer