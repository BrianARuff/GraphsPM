class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self, start=None, end=None):
        self.vertices = {} # individual nodes on graph
    
    def add_vertex(self, value):
        if value not in self.vertices:
                self.vertices[value] = Node(value)
    
    def add_directed_edge(self, starting_node_value, node_to_connect):
        if len(self.vertices[starting_node_value].edges):
            print(f"No edges for node at {self.vertices[starting_node_value]}.")
        self.vertices[starting_node_value].edges.add(node_to_connect)

    def all_vertices(self):
        result = []
        for node in self.vertices:
            result.append({node: list(self.vertices[node].edges)})
        return result
class Node:
    def __init__(self, value):
        self.value = value
        self.edges = set() # set of objects where nodes connect