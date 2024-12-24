import os
from collections import deque

# Reading the input file
current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, "input.txt")

with open(input_file_path, "r") as file:
    lines = file.readlines()

# Build adjacency list
adj = {}
for line in lines:
    x, y = line.strip().split("-")
    if x not in adj:
        adj[x] = []
    adj[x].append(y)
    if y not in adj:
        adj[y] = []
    adj[y].append(x)

# Find all connected components using BFS
visited = set()
subgraphs = set()


def bfs(start):
    q = deque([start])
    subgraph = []
    visited.add(start)
    while q:
        current = q.popleft()
        subgraph.append(current)
        for neighbor in adj[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
    return subgraph


# Traverse the graph and collect all connected components
for node in adj:
    for neighbor in adj[node]:
        if neighbor not in subgraphs:
            subgraphs.add(adj)
    # if node not in visited:
    #     subgraph = bfs(node)
    #     subgraphs.append(subgraph)

# Check if a subset is fully connected


def is_fully_connected(subset):
    # A fully connected subset should have (n * (n - 1)) / 2 edges
    n = len(subset)
    expected_edges = (n * (n - 1)) // 2
    edge_count = 0
    subset_set = set(subset)

    # Count the edges within the subset
    for node in subset:
        for neighbor in adj[node]:
            if neighbor in subset_set:
                edge_count += 1

    # Since we count each edge twice (once for each node), we divide by 2
    edge_count //= 2

    return edge_count == expected_edges


# Find the largest fully connected subset
largest_fully_connected = []

for subgraph in subgraphs:
    # Check all subsets of the current subgraph
    for size in range(len(subgraph), 1, -1):  # Start from the largest subset
        # Generate subsets of the subgraph of this size
        from itertools import combinations
        for subset in combinations(subgraph, size):
            if is_fully_connected(subset):
                # If fully connected and larger than previous, update
                if len(subset) > len(largest_fully_connected):
                    largest_fully_connected = subset

# Sort the largest fully connected subset alphabetically
if largest_fully_connected:
    largest_fully_connected = sorted(largest_fully_connected)
    # Create the password by joining the names with commas
    password = ",".join(largest_fully_connected)
    print(password)
else:
    print("No fully connected subgraph found.")
