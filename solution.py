import heapq
from math import inf

def dijkstra(node, edges, origin):
    adjacent_list = {}
    for i in range(1, node + 1):
        adjacent_list[i] = []
    for a, b, c in edges:
        adjacent_list[a].append((b, c))
        adjacent_list[b].append((a, c))
    distance = {}
    previous = {}
    for i in range(1, node + 1):
        distance[i] = inf
        previous[i] = None
    distance[origin] = 0
    priority_queue = [(0, origin)]
    while priority_queue:
        current_distance, u = heapq.heappop(priority_queue)
        if current_distance > distance[u]:
            continue
        for v, weight in adjacent_list[u]:
            new_distance = current_distance + weight
            if new_distance < distance[v]:
                distance[v] = new_distance
                previous[v] = u
                heapq.heappush(priority_queue, (new_distance, v))
    return distance, previous   