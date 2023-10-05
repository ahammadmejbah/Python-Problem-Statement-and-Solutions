# **Dijkstras Algorithm**

Dijkstra's algorithm is a popular graph search algorithm used to find the shortest path from a source vertex to all other vertices in a weighted graph. It works by maintaining a set of vertices whose shortest distance from the source vertex is known and continually updates the distance values of the remaining vertices as it explores the graph.

Here is a high-level overview of Dijkstra's algorithm:

1. Create a list to store the shortest distance from the source vertex to each vertex in the graph. Initialize the distance of the source vertex to 0 and all other vertices to infinity.

2. Create a set to keep track of visited vertices.

3. While there are unvisited vertices:
   a. Select the unvisited vertex with the smallest distance from the source vertex. This can be done using a priority queue or a min-heap data structure.
   b. Mark the selected vertex as visited.
   c. For each neighbor of the selected vertex that is unvisited:
      - Calculate the distance from the source vertex to the neighbor through the selected vertex.
      - If this distance is shorter than the current known distance to the neighbor, update the neighbor's distance value.
   
4. Repeat step 3 until all vertices have been visited.

Now, let's implement Dijkstra's algorithm in Python:

```python
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
```

In this example, we have a weighted graph represented as a dictionary, where the keys are vertices, and the values are dictionaries of neighboring vertices and their edge weights. The `dijkstra` function returns the shortest distances from the source vertex 'A' to all other vertices in the graph.


# **Markov Algorithm**
A Markov algorithm, also known as a Markov procedure or Markov process, is a mathematical model used in computer science and mathematics for solving problems and manipulating strings or sequences of symbols. It's a type of algorithm that works by repeatedly applying a set of rules or transformations to a string until a specific condition is met. Markov algorithms are often used for tasks like string manipulation, pattern matching, and text processing.

Here, I'll provide a basic overview of how a Markov algorithm works and some Python code to illustrate the concept.

### Markov Algorithm Basics

A Markov algorithm consists of a set of rules, each of which has two parts: a pattern to match in the input string and a replacement string. The algorithm starts with an initial input string and repeatedly applies these rules in a specific order until no more rules can be applied.

The algorithm continues until it reaches a halting state or until no further rules can be applied. It's important to ensure that the algorithm eventually halts, which can be achieved by having a rule that transforms the input into a state where no more rules apply.

### Example Markov Algorithm in Python

Let's consider a simple example of a Markov algorithm in Python that replaces "A" with "B" in a given string.

```python
def markov_algorithm(input_string):
    rules = [
        ("A", "B"),
    ]

    while True:
        applied = False  # Flag to track whether a rule was applied in this iteration

        for pattern, replacement in rules:
            if pattern in input_string:
                input_string = input_string.replace(pattern, replacement)
                applied = True

        if not applied:
            break  # No rules were applied, so we're done

    return input_string

# Test the Markov algorithm
initial_string = "AAAAABAAA"
result = markov_algorithm(initial_string)
print("Initial String:", initial_string)
print("Final Result:", result)
```

In this example, we have one rule that replaces "A" with "B". The algorithm repeatedly checks the input string for occurrences of the pattern "A" and replaces them with "B" until no more "A" characters are present. When no rules can be applied in an iteration, the algorithm terminates.

### Usage

You can customize the `rules` list to define more complex transformations or apply multiple rules in a specific order to achieve the desired output for your particular problem. Markov algorithms can be used for various text-processing tasks, and their flexibility makes them a useful tool for string manipulation.

# Cumulative Standard Deviation
Cumulative standard deviation is a statistic that measures the dispersion or variability of a dataset as it accumulates over time or as new data points are added. It helps you understand how the spread of data changes as you incorporate more observations. To calculate the cumulative standard deviation, you'll need to keep track of the mean and variance as you add each new data point.

Here's the formula for calculating the cumulative standard deviation:

```
Cumulative Standard Deviation (σ_cumulative) = sqrt(Σ[(X_i - μ_cumulative)^2] / N)
```

Where:
- σ_cumulative is the cumulative standard deviation.
- X_i is each individual data point.
- μ_cumulative is the cumulative mean.
- N is the number of data points.

Here's a Python code snippet to calculate the cumulative standard deviation as you add new data points:

```python
import math

def cumulative_std_dev(data):
    cumulative_mean = 0  # Initialize the cumulative mean
    cumulative_variance = 0  # Initialize the cumulative variance
    cumulative_std_deviation = []  # List to store cumulative standard deviations

    for i, x in enumerate(data, 1):
        # Update the cumulative mean
        cumulative_mean = (cumulative_mean * (i - 1) + x) / i

        # Update the cumulative variance
        cumulative_variance = (cumulative_variance * (i - 1) + (x - cumulative_mean) ** 2) / i

        # Calculate the cumulative standard deviation
        cumulative_std_dev = math.sqrt(cumulative_variance)

        cumulative_std_deviation.append(cumulative_std_dev)

    return cumulative_std_deviation

# Example usage:
data = [1, 2, 3, 4, 5]
cumulative_std = cumulative_std_dev(data)
print(cumulative_std)
```

In this code:

- `cumulative_mean` keeps track of the cumulative mean as new data points are added.
- `cumulative_variance` keeps track of the cumulative variance as new data points are added.
- `cumulative_std_deviation` is a list that stores the cumulative standard deviations after each data point is added to the sequence.

The function `cumulative_std_dev` takes a list of data points as input and returns a list of cumulative standard deviations. You can add new data points to the `data` list, and the function will update the cumulative standard deviation accordingly.
