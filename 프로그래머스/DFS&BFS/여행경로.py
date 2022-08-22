from collections import defaultdict


def solution(tickets):
    answer = []
    # routes = dict()
    routes = defaultdict(list)
    
    for start, end in tickets:
        # if start in routes:
        # defaultdict를 썼기 때문에 key가 존재하는지 체크할 필요 X
            routes[start].append(end)
        # else:
        #     routes[start] = [end]
            
    for r in routes.keys():
        # 도착지 알파벳 역순 정렬 > pop() 했을 때 알파벳순으로 뽑히도록
        routes[r].sort(reverse=True)
        
    stack = ["ICN"]
    while stack:
        top = stack[-1]
        # 아예 출발지 목록에 없음(더 이상 이동 불가능) or 갈 수 있는 도착지 없음(티켓 모두 사용)
        if (top not in routes) or (not routes[top]):
            answer.append(stack.pop())
        else:
            stack.append(routes[top].pop())
    
    return answer[::-1]

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets))