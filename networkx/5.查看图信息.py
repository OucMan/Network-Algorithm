import networkx as nx
import matplotlib.pyplot as plt

# 生成图
G = nx.path_graph(8)
nx.draw(G, with_labels=True)
plt.axis('on')
plt.xticks([])
plt.yticks([])
plt.show()
# 查看图中节点和边的个数
print('number of nodes:', G.number_of_nodes())
print('number of edges:', G.number_of_edges())

# 查看图中的所有节点和边
print('all nodes:', G.nodes())
print('all edges:', G.edges())

# 查看某些节点的度
print('degree of some nodes', G.degree([2, 3]))

# 查看节点和边的信息
G.nodes[1]['room'] = 714
G.nodes[1]['color'] = 'b'
G[1][2]['weight'] = 4.7
G[1][2]['color'] = 'blue'
print('information of node 1:', G.nodes[1])
print('information of all nodes:', G.nodes.data())
print('information of edge 1<->2:', G[1][2])
print('information of all edges:', G.edges.data())

# 遍历图
FG = nx.Graph()
FG.add_weighted_edges_from([(1, 2, 0.125), (1, 3, 0.75), (2, 4, 1.2), (3, 4, 0.375)])

#遍历邻接矩阵
for n, nbrs in FG.adj.items():
    for nbr, eattr in nbrs.items():
        wt = eattr['weight']
        # 权重小于0.5的输出
        if wt < 0.5:
            print('way1-(%d, %d, %.3f)' % (n, nbr, wt))

#遍历所有边
for (u, v, wt) in FG.edges.data('weight'):
    #权重小于0.5的输出
    if wt < 0.5:
        print('way2-(%d, %d, %.3f)' % (u, v, wt))
