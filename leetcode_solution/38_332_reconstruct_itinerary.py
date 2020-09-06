# 38 Reconstruct Itinerary
# 일정 재구성

import collections

def findItinerary_1(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)
    
    for a, b in sorted(tickets):
        graph[a].append(b)
        
        
    route = []
    
    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)
        
    dfs('JFK')
    return route[::-1]
    


def findItinerary_2(self, tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)

    for a, b in sorted(tickets, reverse = True):
        graph[a].append(b)


    route = []

    def dfs(a):
        while graph[a]:
             dfs(graph[a].pop()) # O(1)
        route.append(a)

    dfs('JFK')
    return route[::-1]