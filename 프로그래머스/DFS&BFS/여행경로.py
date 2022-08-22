def solution(tickets):
    answer = ["ICN"]
    tickets.sort()
    travel_dfs(answer, tickets)
    return answer
                             
def travel_dfs(way, tickets):
    for ticket in tickets:
        if ticket[0] == way[-1]:
            way.append(ticket[1])
            tickets.remove(ticket)
            travel_dfs(way, tickets)