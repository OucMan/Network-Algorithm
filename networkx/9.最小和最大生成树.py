'''
https://networkx.github.io/documentation/stable/reference/algorithms/tree.html
https://www.cnblogs.com/wushaogui/p/9239959.html
'''

import networkx as nx
import matplotlib.pyplot as plt

# 生成graph
G = nx.Graph()
G.add_weighted_edges_from(
    [('0', '1', 2), ('0', '2', 7), ('1', '2', 3), ('1', '3', 8), ('1', '4', 5), ('2', '3', 1), ('3', '4', 4)])

# 边和节点信息
edge_labels = nx.get_edge_attributes(G, 'weight')
labels = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4'}

# 生成节点位置
pos = nx.spring_layout(G)

# 把节点画出来
nx.draw_networkx_nodes(G, pos, node_color='g', node_size=500, alpha=0.8)

# 把边画出来
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, edge_color=['b', 'r', 'b', 'r', 'r', 'b', 'r'])

# 把节点的标签画出来
nx.draw_networkx_labels(G, pos, labels, font_size=16)

# 把边权重画出来
nx.draw_networkx_edge_labels(G, pos, edge_labels)

# 显示graph
plt.title('weighted graph')
plt.axis('on')
plt.xticks([])
plt.yticks([])
plt.show()

###############最小生成树

# 求得最小生成树,algorithm可以是kruskal(克鲁斯卡尔),prim(普里姆),boruvka(博鲁夫卡)一种,默认是kruskal
KA = nx.minimum_spanning_tree(G, algorithm='kruskal')
print(KA.edges(data=True))

# 直接拿到构成最小生成树的边,algorithm可以是kruskal,prim,boruvka一种,默认是kruskal
mst = nx.minimum_spanning_edges(G, algorithm='kruskal', data=False)
edgelist = list(mst)
print(edgelist)

################最大生成树

# 返回无向图G上的最大生成树或森林。
T = nx.maximum_spanning_tree(G)
print(sorted(T.edges(data=True)))

# 直接拿到构成最大生成树,algorithm可以是kruskal,prim,boruvka一种,默认是kruskal
mst = nx.tree.maximum_spanning_edges(G, algorithm='kruskal', data=False)
edgelist = list(mst)
print(edgelist)
