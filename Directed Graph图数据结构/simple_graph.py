class SimpleDGraph:
    def __init__(self):
        self.adj_list = {}

    def insert_node(self, name):
        if name not in self.adj_list:
            self.adj_list[name] = {'neighbors': {}}

    def insert_edge(self, n1, n2, weight=1):
        if n1 not in self.adj_list:
            self.adj_list[n1] = {'neighbors': {}}

        if n2 not in self.adj_list:
            self.adj_list[n2] = {'neighbors': {}}

        self.adj_list[n1]['neighbors'][n2] = weight

    def __str__(self):
        graph = ''
        for k in self.adj_list.keys():
            graph += k
            if 'order' in self.adj_list[k]:
                graph += '_{}'.format(self.adj_list[k]['order'])
            graph += ': '
            for n in self.adj_list[k]['neighbors'].keys():
                graph += n + ', '
            graph += '\n'
        return graph

    def gen_reverse_graph(self):
        # Generate G reverse where each directed edge is reversed
        for k in self.adj_list.keys():
            self.adj_list[k]['reverse'] = {}

        for k in self.adj_list.keys():
            for n in self.adj_list[k]['neighbors'].keys():
                self.adj_list[n]['reverse'][k] = self.adj_list[k]['neighbors'][n]

    def del_reverse_graph(self):
        for k in self.adj_list.keys():
            del self.adj_list[k]['reverse']


def topo_sort(graph):
    # Mark each node as unvisited.
    for k in graph.adj_list.keys():
        graph.adj_list[k]['visited'] = False

    current_label = len(graph.adj_list)
    for v in graph.adj_list.keys():
        if not graph.adj_list[v]['visited']:
            current_label = dfs(graph, v, current_label)


def dfs(graph, v, current_label):
    graph.adj_list[v]['visited'] = True
    for u in graph.adj_list[v]['neighbors'].keys():
        if graph.adj_list[u]['visited']:
            continue
        current_label = dfs(graph, u, current_label)
    graph.adj_list[v]['order'] = current_label
    current_label -= 1

    return current_label


def dfs_rev(graph, v, finish_list):
    graph.adj_list[v]['visited'] = True
    for u in graph.adj_list[v]['reverse'].keys():
        if graph.adj_list[u]['visited']:
            continue
        dfs_rev(graph, u, finish_list)
    finish_list.append(v)


def dfs_2ed(graph, v, one_scc):
    graph.adj_list[v]['visited'] = True
    for u in graph.adj_list[v]['neighbors'].keys():
        if graph.adj_list[u]['visited']:
            continue
        dfs_2ed(graph, u, one_scc)
    one_scc.append(v)


def kosaraju_scc(graph):
    # 1st pass
    # Mark each node as unvisited.
    for k in graph.adj_list.keys():
        graph.adj_list[k]['visited'] = False

    graph.gen_reverse_graph()

    finish_list = []
    for v in graph.adj_list.keys():
        if not graph.adj_list[v]['visited']:
            dfs_rev(graph, v, finish_list)

    graph.del_reverse_graph()

    # 2ed pass
    for k in graph.adj_list.keys():
        graph.adj_list[k]['visited'] = False

    strong_connected_components = {}
    for v in finish_list[::-1]:
        if not graph.adj_list[v]['visited']:
            strong_connected_components[v] = []
            dfs_2ed(graph, v, strong_connected_components[v])

    return strong_connected_components


def graph1():
    one_graph = SimpleDGraph()
    one_graph.insert_edge('s', 'v')
    # one_graph.insert_edge('v', 'w')
    one_graph.insert_edge('w', 's')
    one_graph.insert_edge('q', 's')
    one_graph.insert_edge('q', 'w')
    one_graph.insert_edge('q', 't')
    # one_graph.insert_edge('t', 'y')
    one_graph.insert_edge('y', 'q')
    one_graph.insert_edge('t', 'x')
    one_graph.insert_edge('x', 'z')
    one_graph.insert_edge('r', 'y')
    one_graph.insert_edge('r', 'u')
    one_graph.insert_edge('u', 'y')
    return one_graph


def graph2():
    one_graph = SimpleDGraph()
    one_graph.insert_edge('s', 'v')
    one_graph.insert_edge('v', 'w')
    one_graph.insert_edge('w', 's')
    one_graph.insert_edge('q', 's')
    one_graph.insert_edge('q', 'w')
    one_graph.insert_edge('q', 't')
    one_graph.insert_edge('t', 'y')
    one_graph.insert_edge('y', 'q')
    one_graph.insert_edge('t', 'x')
    one_graph.insert_edge('x', 'z')
    one_graph.insert_edge('r', 'y')
    one_graph.insert_edge('r', 'u')
    one_graph.insert_edge('u', 'y')
    return one_graph

# def graph2():
#     one_graph = SimpleDGraph()
#     one_graph.insert_edge('a', 'b')
#     one_graph.insert_edge('b', 'c')
#     one_graph.insert_edge('b', 'd')
#     one_graph.insert_edge('c', 'a')
#     one_graph.insert_edge('c', 'h')
#     one_graph.insert_edge('c', 'k')
#     one_graph.insert_edge('d', 'e')
#     one_graph.insert_edge('d', 'g')
#     one_graph.insert_edge('e', 'f')
#     one_graph.insert_edge('f', 'g')
#     one_graph.insert_edge('g', 'e')
#     one_graph.insert_edge('h', 'g')
#     one_graph.insert_edge('h', 'i')
#     one_graph.insert_edge('h', 'j')
#     one_graph.insert_edge('i', 'j')
#     one_graph.insert_edge('i', 'f')
#     one_graph.insert_edge('j', 'k')
#     one_graph.insert_edge('k', 'h')
#     return one_graph


if __name__ == '__main__':
    my_graph = graph1()
    print('Graph:')
    print(my_graph)
    topo_sort(my_graph)
    print('Topo sort:')
    topo_sort = sorted(my_graph.adj_list, key=lambda v: my_graph.adj_list[v]['order'])
    print(topo_sort)

    my_graph = graph2()
    sccs = kosaraju_scc(my_graph)
    print('{} Strongly connected components.'.format(len(sccs.keys())))
    for i, key in enumerate(sccs.keys()):
        print('Component {}: {}'.format(i, sccs[key]))
