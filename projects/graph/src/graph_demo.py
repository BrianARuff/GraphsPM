#!/usr/bin/python

"""
Demonstration of Graph functionality.
"""

from sys import argv

from graph import Graph, Node


def main():
    graph = Graph()  # Instantiate your graph
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_directed_edge(5, 3)
    graph.add_directed_edge(6, 3)
    graph.add_directed_edge(7, 1)
    graph.add_directed_edge(4, 7)
    graph.add_directed_edge(1, 2)
    graph.add_directed_edge(7, 6)
    graph.add_directed_edge(2, 4)
    graph.add_directed_edge(3, 5)
    graph.add_directed_edge(2, 3)
    graph.add_directed_edge(4, 6)
    for node in graph.vertices:
        print(node, graph.vertices[node].edges)
    print(graph.all_vertices())

main()
