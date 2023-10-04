import heapq

def dijkstra(graph, source):
    # Initialize distances and visited set
    distances = {vertex: float('infinity') for vertex in graph}
    distances[source] = 0
    visited = set()
    
    # Create a priority queue to store vertices and their distances
    priority_queue = [(0, source)]
    
    while priority_queue:
        # Get the vertex with the smallest distance from the priority queue
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Skip if already visited
        if current_vertex in visited:
            continue
        
        # Mark the current vertex as visited
        visited.add(current_vertex)
        
        # Update the distances to neighbors
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

source_vertex = 'A'
shortest_distances = dijkstra(graph, source_vertex)
print("Shortest distances from", source_vertex, "to each vertex:", shortest_distances)
