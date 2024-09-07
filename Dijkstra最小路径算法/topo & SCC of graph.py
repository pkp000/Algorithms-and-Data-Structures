# N a m e   :裴鲲鹏
# Student ID:202100172014
# Date&Time :2022/10/23 13:58

class Vertex:
    def __init__(self, id):
        self.id = id
        self.connected = {}

    def __str__(self):
        return f'vertex{self.id}'

    def creat_connection(self, neighbor_id, weight=0):
        self.connected[neighbor_id] = weight

    def get_connections(self):
        return self.connected.keys()


class Simple_Graphy:
    def __init__(self):
        self.storage = {}
        self.vertex_num = 0

    def __contains__(self, item):
        return item in self.storage

    def __str__(self):
        return f'grahy:{self.storage}'

    def insert_vertex(self, id):
        self.vertex_num += 1
        new_vertex = Vertex(id)
        self.storage[id] = new_vertex
        return new_vertex

    def insert_edge(self, front, next):
        if front not in self.storage:
            new_front_vertex = self.insert_vertex(front)
        if next not in self.storage:
            new_next_vertex = self.insert_vertex(next)
        self.storage[front].creat_connection(self.storage[next])


def topoSort(graph):
    in_degrees = dict((u, 0) for u in graph)  # Initialize all vertices to 0
    num = len(in_degrees)
    for u in graph:
        for v in graph[u]:
            in_degrees[v] += 1  # Calculate the ingress of each vertex
    Q = [u for u in in_degrees if in_degrees[u] == 0]  # Filter vertices with vertices of 0
    Seq = []
    while Q:
        u = Q.pop()  # By default, it is removed from the last one
        Seq.append(u)
        for v in graph[u]:
            in_degrees[v] -= 1  # Remove all of its outbounds
            if in_degrees[v] == 0:
                Q.append(v)  # Filter again for vertices with vertices of 0
    if len(Seq) == num:  # Whether the number of vertices in the output is equal to the vertices
        return Seq
    else:
        return None


def DFS(graph, s):
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)
    parent = {s: None}

    while stack:
        vertex = stack.pop()
        nodes = graph[vertex]
        for m in nodes:
            if m not in seen:
                stack.append(m)
                seen.add(m)
                parent[m] = vertex
        print(vertex, end=' ->  ')
    return parent


# Get the reverse graph
def G_rev(G):
    # Initialize Figure GT for flipping edges
    GT = dict()
    for u in G.keys():
        GT[u] = GT.get(u, set())
    # Flipping edges
    for u in G.keys():
        for v in G[u]:
            GT[v].add(u)
    return GT


# With a given start node, a single connectivity flux is obtained
def walk(G, s, S=None):
    if S is None:
        s = set()
    Q = []
    P = dict()
    Q.append(s)
    P[s] = None
    while Q:
        u = Q.pop()
        for v in G[u]:
            if v in P.keys() or v in S:
                continue
            Q.append(v)
            P[v] = P.get(v, u)
    # Returns a strong connectivity graph
    return P


# # Method two:
# def SCC(graph):
#     transpose_graph = get_transpose_graph(graph)
#     scc_list, seen = [], set()
#     for u in dfs_top_sort(graph):
#         if u in seen:
#             continue
#         component = walk(transpose_graph, u, seen)
#         seen.update(component)
#         scc_list.append(component)
#     return scc_list
#
#
# def get_transpose_graph(graph):
#     transposed = {}
#     for u in graph:
#         transposed[u] = set()
#     for u in graph:
#         for v in graph[u]:
#             transposed[v].add(u)
#     return transposed
#
#
# def dfs_top_sort(graph):
#     visited, res = set(), []
#
#     def recurse(u):
#         if u in visited:
#             return
#         visited.add(u)
#         for v in graph[u]:
#             recurse(v)
#         res.append(u)
#
#     for u in graph:
#         recurse(u)
#
#     res.reverse()
#     return res
#
#
# def walk(graph, start, s=None):
#     nodes, current = set(), dict()
#     current[start] = None
#     nodes.add(start)
#     while nodes:
#         u = nodes.pop()
#         for v in graph[u].difference(current, s):
#             nodes.add(v)
#             current[v] = u
#     return current


if __name__ == '__main__':
    G = {
        'q': 'swt',
        'r': 'uy',
        's': 'v',
        't': 'x',
        'u': 'y',
        'v': '',
        'w': 's',
        'x': 'z',
        'y': 'q',
        'z': ''
    }
    print('Depth-first search:')
    DFS(G, 'q')
    print('end\n', '\nThe following is a topological order:')
    print(topoSort(G))

    ## Method two:
    # print(SCC(G))

    seen = set()  # Record strongly connected components
    scc_list = []  # Store strong connectivity components
    GT = G_rev(G)
    for u in topoSort(G):
        if u in seen:
            continue
        C = walk(GT, u, seen)
        seen.update(C)
        scc_list.append(sorted(list(C.keys())))
    print('\nAfter SCC analysis is as follows:\n', scc_list)
