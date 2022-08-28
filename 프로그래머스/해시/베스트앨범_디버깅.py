from collections import defaultdict

def solution(genres, plays):
    answer = []
    playlist = defaultdict(list)
    for i in range(len(genres)):
        playlist[genres[i]].append((plays[i], i))
    # print(playlist)
    sorted_dict = sorted(playlist.items(), key=lambda x: sum(x[1][0]), reverse=True) # ??
    print("sorted_dict:", sorted_dict)
    for key, value in sorted_dict:
        value.sort(key=lambda x: (-x[0], x[1]))
    print("sorted_dict:", sorted_dict)
    for key, value in sorted_dict:
        print("value:", value)
        answer.append(value[0][1])
        answer.append(value[1][1])
    return answer

genres = ["1", "2", "2", "3", "3"]
plays = [100, 200, 500, 300, 200]
solution(genres, plays)