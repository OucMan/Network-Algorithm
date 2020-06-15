def TSA(edges: list, nums: int) -> list:
    '''
    对DGA进行拓扑排序
    :param edges: 有向无环图的边集
    :param nums: 节点数目
    :return: 拓扑排序列表
    '''
    nodes = [[0, i, []] for i in range(nums)]
    for edge in edges:
        nodes[edge[0]][2].append(edge[1])
        nodes[edge[1]][0] += 1
    queue = []
    visited = set()
    sorted_list = []
    for node in nodes:
        if node[0] == 0:
            queue.append(node)
            visited.add(node[1])
    while queue:
        node = queue.pop(0)
        sorted_list.append(node[1])
        for j in node[2]:
            nodes[j][0] -= 1
        for j in nodes:
            if j[0] == 0 and j[1] not in visited:
                queue.append(j)
                visited.add(j[1])
    return sorted_list if len(sorted_list) == nums else []
    
if __name__ == "__main__":
    # dga = [[0, 1], [0, 2], [0, 4], [1, 3], [2, 1], [2, 3], [4, 2], [4, 3]]
    # print(TSA(dga, 5))
