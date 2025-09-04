from collections import defaultdict

def reconstructItinerary(tickets: list):
    path = []
    graph = defaultdict(list)
    
    for s,e in sorted(tickets, reverse=True):
        graph[s].append(e)

    def dfs(v):
        path.append(v)

        if graph[v]:
            next = graph[v].pop()
            dfs(next)

    dfs("JFK")
    
    return path

# tickets = [["MUC", "LHR"],["JFK", "MUC"],["SFO", "SJC"],["LHR", "SFO"]]
tickets = [["JFK", "SFO"],["JFK", "ATL"],["SFO", "ATL"],["ATL", "JFK"],["ATL", "SFO"]]
print(reconstructItinerary(tickets))