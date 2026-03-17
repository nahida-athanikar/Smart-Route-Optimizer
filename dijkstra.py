import heapq

def dijkstra(graph, start):
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    parent = {node: None for node in graph}

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        for neighbor, weight in graph[curr_node]:
            distance = curr_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parent[neighbor] = curr_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, parent