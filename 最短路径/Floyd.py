import copy
def Floyd(graph: list) -> list:
    '''
    弗洛伊德算法：最短路径
    :param graph: whole graph
    :return: the graph of shortest paths
    '''
    short_graph = copy.deepcopy(graph)
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                print('Comparing short_graph[%s][%s] and {short_graph[%s][%s]+short_graph[%s][%s]}' % (i, j, i, k, k, j))
                print('Former short_graph[%s][%s] = %s' % (i, j, short_graph[i][j]))
                short_graph[i][j] = min(short_graph[i][j], short_graph[i][k] + short_graph[k][j])
                print('Present short_graph[%s][%s] = %s\n' % (i, j, short_graph[i][j]))
    return short_graph

if __name__ == "__main__":
    # inf = float('inf')
    # graph = [[0, 1, 12, inf, inf, inf],
    #           [inf, 0, 9, 3, inf, inf],
    #           [inf, inf, 0, inf, 5, inf],
    #           [inf, inf, 4, 0, 13, 15],
    #           [inf, inf, inf, inf, 0, 4],
    #           [inf, inf, inf, inf, inf, 0]]
    # short_graph = Floyd(graph)
    # print(short_graph)
