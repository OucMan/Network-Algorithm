def Dijkstra(start: int, graph: list) -> (list, dict):
    '''
    迪杰斯特拉算法：最短路径
    :param start: start node index, int
    :param mgraph: whole graph
    :return: list about shortest distances from start node to remaining nodes, dict about shortest paths
    '''
    passed = [start]
    no_passed = [x for x in range(len(graph)) if x != start]
    short_paths = {}
    for i in range(len(graph)):
        short_paths[i] = [start]

    short_distance = graph[start]

    while len(no_passed):
        idx = no_passed[0]
        for i in no_passed:
            if short_distance[i] < short_distance[idx]:
                idx = i

        no_passed.remove(idx)
        passed.append(idx)
        short_paths[idx].append(idx)

        for i in no_passed:
            if short_distance[idx] + graph[idx][i] < short_distance[i]:
                short_distance[i] = short_distance[idx] + graph[idx][i]
                short_paths[i].append(idx)
    return short_distance, short_paths
    
    if __name__ == "__main__":
    # inf = float('inf')
    # graph = [[0, 1, 12, inf, inf, inf],
    #           [inf, 0, 9, 3, inf, inf],
    #           [inf, inf, 0, inf, 5, inf],
    #           [inf, inf, 4, 0, 13, 15],
    #           [inf, inf, inf, inf, 0, 4],
    #           [inf, inf, inf, inf, inf, 0]]

    # dis, path = Dijkstra(0, graph)
    # print(dis)
    # print(path)
    pass
