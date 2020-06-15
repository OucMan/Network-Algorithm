import networkx as nx
import matplotlib.pyplot as plt

# 设置图的属性
G = nx.Graph(day="Friday")
print('Assign graph attributes when creating a new graph: ',G.graph)
G.graph['day'] = "Monday"
print('Assign graph attributes when have a graph: ',G.graph)

# 设置节点的属性
# G.add_node(1, time='5pm')
# G.nodes[1]['room'] = 714
# G.nodes[1]['color'] = 'b'
# G.add_nodes_from([3, 4], time='2pm', color='g')
# nx.draw(G, with_labels=True)
# plt.show()
# print(G.nodes.data())

# 设置边的属性
# 创建时设置
G.add_edge(1, 2, weight=4.7)
G.add_edges_from([(3, 4), (4, 5)], color='red', weight=10)
G.add_edges_from([(1, 2, {'color': 'blue'}), (4, 5, {'weight': 8})])
# 直接设置
G[1][2]['weight'] = 4.7
G[1][2]['color'] = "blue"
G.edges[3, 4]['weight'] = 4.2
G.edges[1, 2]['color'] = 'green'
print('edge 1-2: ', G.edges[1, 2])
print('edge 3-4: ', G.edges[3, 4])


#生成节点标签
labels={}
labels[1]='1'
labels[2]='2'
labels[3]='3'
labels[4]='4'
labels[5]='5'

#获取graph中的边权重
edge_labels = nx.get_edge_attributes(G, 'weight')
print('weight of all edges:', edge_labels)

#生成节点位置
pos = nx.circular_layout(G)
print('position of all nodes:', pos)

#把节点画出来
nx.draw_networkx_nodes(G, pos, node_color='g', node_size=500, alpha=0.8)

#把边画出来
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, edge_color='b')

#把节点的标签画出来
nx.draw_networkx_labels(G, pos, labels, font_size=16)

#把边权重画出来
nx.draw_networkx_edge_labels(G, pos, edge_labels)

plt.axis('on')
#去掉坐标刻度
plt.xticks([])
plt.yticks([])
plt.show()
