def Prim(graph:list) ->(list, int):
    '''
    普里姆算法：最小生成树
    :param graph: whole graph
    :return: minimum spanning tree and minimum weight
    '''
    n = len(graph)
    current_list = [0]
    remaining_list = [i for i in range(1, n)]
    total_weight = 0
    min_tree = []
    while len(remaining_list) > 0:
        point1, point2, weight = 0, 0, float('inf')
        for cur_node in current_list:
            for next_node in remaining_list:
                if graph[cur_node][next_node] == 0 or graph[cur_node][next_node] == float('inf'):
                    continue
                else:
                    if weight > graph[cur_node][next_node]:
                        weight = graph[cur_node][next_node]
                        point1 = cur_node
                        point2 = next_node
        total_weight += weight
        min_tree.append([point1, point2, weight])
        current_list.append(point2)
        remaining_list.remove(point2)
    return min_tree, total_weight
 
 if __name__ == "__main__":
    # inf = float('inf')
    # graph = [[0, 1, 12, inf, inf, inf],
    #           [inf, 0, 9, 3, inf, inf],
    #           [inf, inf, 0, inf, 5, inf],
    #           [inf, inf, 4, 0, 13, 15],
    #           [inf, inf, inf, inf, 0, 4],
    #           [inf, inf, inf, inf, inf, 0]]
    # l, w = Prim(graph)
    # print(l)
    # print(w)
