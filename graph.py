# adjacency Matrix= ana adjencency ia s square martrix or you can sys its is 2D matrix and the element of the matrix indicate whether pair of vertices adjencenr or not

#adjacency list = an adjacency list a coolection of unordered list used to reprent a graph each listt describe the set of neighbors of vertex in the graph

# A:[B,C,D]
# B:[A,E]
# C:[A,B]
# D:[A,C,E]
# E:[B,D]




class Graph:

    def __init__(self):
        self.adjencency_list = {}

    # Add a vertex
    def add_vertex(self, vertex):
        if vertex not in self.adjencency_list:
            self.adjencency_list[vertex] = []
            return True
        return False

    # Add an edge
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjencency_list and vertex2 in self.adjencency_list:
            self.adjencency_list[vertex1].append(vertex2)
            self.adjencency_list[vertex2].append(vertex1)
            return True
        return False

    # Remove an edge
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjencency_list and vertex2 in self.adjencency_list:

            if vertex2 in self.adjencency_list[vertex1]:
                self.adjencency_list[vertex1].remove(vertex2)

            if vertex1 in self.adjencency_list[vertex2]:
                self.adjencency_list[vertex2].remove(vertex1)

            return True

        return False

    # Remove a vertex
    def remove_vertex(self, vertex):
        if vertex in self.adjencency_list:

            # Remove vertex from all its neighbors
            for other_vertex in self.adjencency_list[vertex]:
                self.adjencency_list[other_vertex].remove(vertex)

            # Delete the vertex
            del self.adjencency_list[vertex]

            return True

        return False

    # Print graph
    def print_graph(self):
        for vertex in self.adjencency_list:
            print(vertex, ":", self.adjencency_list[vertex])


# Create graph
graph = Graph()

# Add vertices
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')

# Add edges
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'D')
graph.add_edge('B', 'C')
graph.add_edge('D', 'E')

# Print original graph
print("Original Graph:")
graph.print_graph()

# Remove an edge
graph.remove_edge('A', 'B')

print("\nAfter removing edge A-B:")
graph.print_graph()

# Remove a vertex
graph.remove_vertex('C')

print("\nAfter removing vertex C:")
graph.print_graph()