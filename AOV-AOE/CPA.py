def CPA(edges: list, nums: int) -> list:
    '''
    求解关键路径
    :param edges: 有权有向无环图的边集
    :param nums: 节点数目
    :return: 关键路径
    '''
    graph = {}
    for edge in edges:
        graph[(edge[0], edge[1])] = edge[2]
    # print(graph)
    edges_without_weight = [e[:2] for e in edges]
    sort_topo = TSA(edges_without_weight, nums)
    # 有环
    if not sort_topo:
        return []
    tasks = {}
    for i in sort_topo:
        tmp = {'rely': [], 'to': [], 'es': 0, 'le': 0}
        tasks[i] = tmp
    for edge in edges:
        if edge[0] not in tasks[edge[1]]['rely']:
            tasks[edge[1]]['rely'].append(edge[0])
        if edge[1] not in tasks[edge[0]]['to']:
            tasks[edge[0]]['to'].append(edge[1])

    # 前向计算，得到最早开始时间
    for i in sort_topo:
        max_value = 0
        for j in tasks[i]['rely']:
            if max_value < graph[(j, i)] + tasks[j]['es']:
                max_value = graph[(j, i)] + tasks[j]['es']
            tasks[i]['es'] = max_value

    # 后向计算，得到最晚开始时间
    tasks[sort_topo[-1]]['le'] = tasks[sort_topo[-1]]['es']
    for i in sort_topo[::-1]:
        min_value = tasks[sort_topo[-1]]['es']
        for j in tasks[i]['to']:
            if min_value > tasks[j]['le'] - graph[(i, j)]:
                min_value = tasks[j]['le'] - graph[(i, j)]
        tasks[i]['le'] = min_value
    # 得到结果
    res = []
    for i in sort_topo:
        if tasks[i]['es'] == tasks[i]['le']:
            res.append(i)
    return res

if __name__ == "__main__":

    dga = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [1, 4, 3], [2, 4, 2], [3, 4, 5], [3, 5, 2],\
           [4, 6, 1], [4, 7, 3], [5, 8, 4], [7, 8, 1], [6, 9, 2], [7, 9, 7], [8, 9, 5]]

    print(CPA(dga, 10))
