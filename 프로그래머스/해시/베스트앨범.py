# 첫번째 오답
from collections import defaultdict

def solution(genres, plays):
    answer = []
    playlist = defaultdict(list)
    for i in range(len(genres)):
        playlist[genres[i]].append(plays[i])
    sorted_dict = sorted(playlist.items(), key=lambda x: sum(x[1]), reverse=True)
    for key, value in sorted_dict:
        value.sort(key=lambda x: (-x, plays.index(x)))
    for key, value in sorted_dict:
        answer.append(plays.index(value[0]))
        plays[plays.index(value[0])] = -1
        answer.append(plays.index(value[1]))
    return answer

# 두번째 오답
from collections import defaultdict

def solution(genres, plays):
    answer = []
    playlist = defaultdict(list)
    for i in range(len(genres)):
        playlist[genres[i]].append((plays[i], i))
    sorted_dict = sorted(playlist.items(), key=lambda x: sum(x[1][0]), reverse=True)
    for key, value in sorted_dict:
        value.sort(key=lambda x: (-x[0], x[1]))
    for key, value in sorted_dict:
        answer.append(value[0][1])
        answer.append(value[1][1])
    return answer