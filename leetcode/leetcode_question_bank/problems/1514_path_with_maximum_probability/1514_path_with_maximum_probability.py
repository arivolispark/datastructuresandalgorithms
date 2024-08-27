from collections import *

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Dictionary to hold the graph representation
        graph = defaultdict(list)
      
        # Building the graph where each edge is associated with its success probability
        for (node1, node2), success_prob in zip(edges, succProb):
            graph[node1].append((node2, success_prob))
            graph[node2].append((node1, success_prob))
      
        # Priority queue to store the nodes along with their probability so far
        # We use negative probabilities in the priority queue because heapq is a min heap
        queue = [(-1, start_node)]
      
        # List to hold the maximum success probability to reach each node
        probabilities = [0] * n
        probabilities[start_node] = 1  # Probability to reach start node from itself is 1
      
        # Process the queue until it's empty
        while queue:
            # Get the node with maximum success probability
            negative_w, current = heappop(queue)
            w = -negative_w
          
            # If we have already found a better way to the current node, skip it
            if probabilities[current] > w:
                continue
          
            # Explore neighbors of the current node
            for neighbor, edge_prob in graph[current]:
                # Calculate new success probability via this edge
                new_prob = probabilities[current] * edge_prob
                # If it's better than the existing probability to the neighbor, update it
                if probabilities[neighbor] < new_prob:
                    probabilities[neighbor] = new_prob
                    # Push the new probability for the neighbor into the queue
                    heappush(queue, (-new_prob, neighbor))
      
        # Return the maximum success probability to reach the end node
        return probabilities[end_node]
