import networkx as nx
import matplotlib.pyplot as plt


#定义图的节点和边
nodes = ['0', '1', '2', '3', '4', '5', 'a', 'b', 'c']
edges = [('0', '0', 1), ('0', '1', 1), ('0', '5', 1), ('0', '5', 2), ('1', '2', 3), ('1', '4', 5), ('2', '1', 7), \
         ('2', '4', 6), ('a', 'b', 0.5), ('b', 'c', 0.5), ('c', 'a', 0.5)]

# 无向图
# G = nx.Graph()
# G.add_nodes_from(nodes)
# G.add_weighted_edges_from(edges)
# nx.draw(G, with_labels=True)
# plt.show()

# 有向图
G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)
nx.draw(G, with_labels=True)
plt.show()

# 定义带平行边无向图
# G = nx.MultiGraph()
# G.add_nodes_from(nodes)
# G.add_weighted_edges_from(edges)
# nx.draw(G, with_labels=True)
# plt.show()

# 定义带平行边有向图
# G = nx.MultiDiGraph()
# G.add_nodes_from(nodes)
# G.add_weighted_edges_from(edges)
# nx.draw(G, with_labels=True)
# plt.show()

# matplotlib包不能显示平行边(两点之间存在多条边),自循环（起点和终点相同）这类的边,所以需要借助pydot包来显示
# https://blog.csdn.net/sinat_38653840/article/details/84776806
