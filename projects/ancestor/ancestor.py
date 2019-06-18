'''
UNDERSTANDING THE PROBLEM
    write a function that
    returns earliest known ancestor (ID)
    if the earliest ancestor is a tie, return the lower numeric ID
    if there are no parents, return -1

DEVISING A PLAN
    BFT Graph
    Break case - if no ancestors, return -1
    Create an empty set to story visited nodes
    create an empty queue and enqueue the starting vertex
    While the queue is not empty...
        Dequeue the first vertex
        If that vertex has not been visited.
            Mark it as visited
            Then add it's neighbors to the queue



IMPLIMENTING THE PLAN

ITERATING
'''

from util import Queue, Graph, Stack


class Graph():
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def earliest_ancestor(self, starting_vertex):
        visited = set()
        q = Queue()
        q.enqueue(starting_vertex)
        while q.size() > 0:
            current = q.dequeue()
            if current not in visited:
                visited.add(current)
                # print(current)
                for neighbor in self.vertices[current]:
                    q.enqueue(neighbor)
        if current == starting_vertex:
            print(f"starting_vertex: {starting_vertex}; earliest known ancestor: ", -1)
        else:
            print(f"starting_vertex: {starting_vertex}; earliest known ancestor: ", current, "\n\n")
if __name__ == '__main__':
    graph = Graph()
    graph.add_vertex(10)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(4)
    graph.add_vertex(11)
    graph.add_vertex(3)
    graph.add_vertex(5)
    graph.add_vertex(8)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_vertex(9)
    graph.add_edge(3, 1)
    graph.add_edge(3, 2)
    graph.add_edge(6, 3)
    graph.add_edge(6, 5)
    graph.add_edge(7, 5)
    graph.add_edge(5, 4)
    graph.add_edge(8, 4)
    graph.add_edge(9, 8)
    graph.add_edge(8, 11)
    graph.add_edge(1, 10)

    graph.earliest_ancestor(10)  #  Should print -1
    graph.earliest_ancestor(1)  #  Should print 10
    graph.earliest_ancestor(3)  #  Should print 10
    graph.earliest_ancestor(6)  #  Should print 10
    graph.earliest_ancestor(2)  #  Should print -1
    graph.earliest_ancestor(5)  #  Should print 4
    graph.earliest_ancestor(4)  #  Should print -1
    graph.earliest_ancestor(7)  #  Should print 4
    graph.earliest_ancestor(8)  #  Should print 4
    graph.earliest_ancestor(9)  #  Should print 4
    graph.earliest_ancestor(11)  #  Should print -1
