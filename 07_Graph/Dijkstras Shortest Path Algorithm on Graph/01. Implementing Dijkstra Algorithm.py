import heapq

def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}
print(calculate_distances(example_graph, 'X'))
# => {'U': 1, 'W': 2, 'V': 2, 'Y': 1, 'X': 0, 'Z': 2}



''' 
Analysis of Dijkstra’s Algorithm

Building the distances dictionary takes O(V)O(V) time since we add every vertex in the graph to the dictionary.

The while loop is executed once for every entry that gets added to the priority queue. An entry can only be added when we explore an edge, so there are at most O(E)O(E) iterations of the while loop.

The for loop is executed at most once for every vertex, since the current_distance > distances[current_vertex] check ensures that we only process a vertex once. The for loop iterates over outgoing edges, so among all iterations of the while loop, the body of the for loop executes at most O(E)O(E) times.

Finally, if we consider that each priority queue operation (adding or removing an entry) is O(\log E)O(logE), we conclude that the total running time is O(V + E \log E)O(V+ElogE).
# Time: O(V * E * log(E))
'''