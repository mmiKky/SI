
class Graph:
    def __init__(self):
        self.adjacency_list = dict()

    def add_vertex(self, vertex):
        if not vertex in self.adjacency_list:
            self.adjacency_list[vertex] = set() 

    def add_edge(self, vertex, edge):
        if vertex in self.adjacency_list:
            self.adjacency_list[vertex].add(edge)
        else:
            self.adjacency_list[vertex] = set()
            
    def get_vertices(self):
        return list(self.adjacency_list.keys())

    def get_edges(self, vertex):
        if vertex in self.adjacency_list:
            return self.adjacency_list[vertex]


class Vertex:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __hash__(self):
        values = vars(self).values()
        return hash(tuple(sorted(str(value) for value in values)))
    
    def __eq__(self, other):
        return hash(self) == hash(other)
    
    def __lt__(self, other):
        return hash(self) < hash(other)

    def __str__(self):
        vertex_str = ''
        for arg in vars(self).values():
            vertex_str += f'{arg}, '
        return vertex_str 


class Edge:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __hash__(self):
        values = vars(self).values()
        return hash(tuple(sorted(str(value) for value in values)))
    
    def __eq__(self, other):
        return hash(self) == hash(other)
    