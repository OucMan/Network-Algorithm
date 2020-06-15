def Kruskal(graph:list) -> (list, int):
    '''
    克鲁斯卡尔算法：找最小生成树
    :param graph: whole graph
    :return: minimum spanning tree and minimum weight
    '''
    total_weight = 0
    min_tree = []
    graph_edges = []
    n = len(graph)
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0 and graph[i][j] != float('inf'):
                graph_edges.append([i, j, graph[i][j]])
    graph_edges.sort(key=lambda x: x[2])
    group = [[i] for i in range(n)]
    for edge in graph_edges:
        for i in range(len(group)):
            if edge[0] in group[i]:
                j = i
            if edge[1] in group[i]:
                k = i
        if j != k:
            min_tree.append(edge)
            total_weight += edge[2]
            group[j] = group[j] + group[k]
            group[k] = []
    return min_tree, total_weight

if __name__ == "__main__":
    # inf = float('inf')
    # graph = [[0, 1, 12, inf, inf, inf],
    #           [inf, 0, 9, 3, inf, inf],
    #           [inf, inf, 0, inf, 5, inf],
    #           [inf, inf, 4, 0, 13, 15],
    #           [inf, inf, inf, inf, 0, 4],
    #           [inf, inf, inf, inf, inf, 0]]
    # l, w = Kruskal(graph)
    # print(l)
    # print(w)
