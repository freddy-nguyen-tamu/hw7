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
def backtrack(previous, destination):
    path = []
    current = destination
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    return path
if __name__ == "__main__":
    n = 36
    edges = [
        (1, 11, 1), (1, 2, 1), (11, 10, 1), (12, 11, 2), 
        (11, 17, 1), (17, 18, 2), (18, 19, 2), (2, 3, 1), 
        (3, 4, 1), (4, 5, 1), (5, 22, 1), (5, 7, 1), 
        (5, 6, 2), (6, 7, 2), (7, 8, 1), (8, 9, 1), 
        (9, 19, 1), (12, 13, 2), (13, 14, 1), (14, 15, 1), 
        (15, 20, 1), (20, 21, 1), (13, 21, 1), (21, 22, 2), 
        (21, 2, 1), (21, 20, 2), (22, 20, 1), (3, 8, 2), 
        (9, 10, 1), (3, 21, 1), (4, 21, 1), (13, 16, 1), 
        (16, 15, 1), (10, 18, 2), (14, 16, 1), (14, 20, 1)
    ]
    current_node = 1
    a, b = dijkstra(n, edges, current_node)
    print("Shortest distances from node", current_node)
    for node in [6,8,9,15,16,22]:
        path = backtrack(b, node)
        print(f"Node {node}: Distance = {a[node]}, Path = {path}")