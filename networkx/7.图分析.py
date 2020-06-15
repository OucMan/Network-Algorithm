
'''
无向图
连通子图
nx.connected_components(G)

有向图
强连通：有向图中任意两点v1、v2间存在v1到v2的路径（path）及v2到v1的路径。
nx.strongly_connected_components(G)
弱联通：将有向图的所有的有向边替换为无向边，所得到的图称为原图的基图。如果一个有向图的基图是连通图，则有向图是弱连通图。
nx.weakly_connected_components(G)
'''

import networkx as nx
import matplotlib.pyplot as plt

####### 连通子图

# # 定义图的节点和边
# nodes=['0','1','2','3','4','5','a','b','c']
# edges=[('0','0',1),('0','1',1),('0','5',1),('0','5',2),('1','2',3),('1','4',5),('2','1',7),('2','4',6),('a','b',0.5),('b','c',0.5),('c','a',0.5)]
#
# # 定义graph
# G = nx.Graph()
# G.add_nodes_from(nodes)
# G.add_weighted_edges_from(edges)
#
# # 找到所有连通子图
# print('connected_components of graph: ', list(nx.connected_components(G)))
#
# # 显示该graph
# nx.draw(G, with_labels=True, font_weight='bold')
# plt.axis('on')
# plt.xticks([])
# plt.yticks([])
# plt.show()

##############弱连通
# 定义graph
# G = nx.path_graph(4, create_using=nx.DiGraph())
# G.add_edges_from([(7, 8), (8, 3)])
# G.add_edges_from([(5, 6), (6, 9)])
#
# # 找出所有的弱连通图
# for c in nx.weakly_connected_components(G):
#     print(c)
#
# # 由大到小的规模判断弱连通子图
# print([len(c) for c in sorted(nx.weakly_connected_components(G), key=len, reverse=True)])
#
# nx.draw(G, with_labels=True, font_weight='bold')
# plt.axis('on')
# plt.xticks([])
# plt.yticks([])
# plt.show()

##############强连通

# #定义图
# G = nx.path_graph(4, create_using=nx.DiGraph())
# G.add_edges_from([(3, 8), (8, 1)])
#
# #找出所有的强连通子图
# con = nx.strongly_connected_components(G)
# print(con,type(con),list(con))
#
# #显示该图
# nx.draw(G, with_labels=True, font_weight='bold')
# plt.axis('on')
# plt.xticks([])
# plt.yticks([])
# plt.show()

##############子图

# #定义图
# G = nx.DiGraph()
# G.add_edges_from([(5, 6), (6, 7), (7, 8)])
# #抽取图G的节点作为子图
# sub_graph = G.subgraph([5, 6, 8])
#
# plt.subplots(1,2,figsize=(15,5))
# #画原图
# plt.subplot(121)
# nx.draw(G, with_labels=True, font_weight='bold')
# plt.title('Graph')
# plt.axis('on')
# plt.xticks([])
# plt.yticks([])
#
# #画子图
# plt.subplot(122)
# nx.draw(sub_graph, with_labels=True, font_weight='bold')
# plt.title('Subgraph')
# plt.axis('on')
# plt.xticks([])
# plt.yticks([])
#
# plt.show()

############条件过滤

#过滤函数
def flt_func_draw():
    flt_func = lambda d: d['id'] != 1
    return flt_func

#定义有向图
G = nx.DiGraph()
road_nodes = {'a': {'id': 1}, 'b': {'id': 1}, 'c': {'id': 3}, 'd': {'id': 4}}
road_edges = [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'd')]
G.add_nodes_from(road_nodes.items())
G.add_edges_from(road_edges)


plt.subplots(1,2,figsize=(15,5))

#画出原图
plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
plt.title('Before')
plt.axis('on')
plt.xticks([])
plt.yticks([])

flt_func = flt_func_draw()
part_G = G.subgraph(n for n, d in G.nodes(data=True) if flt_func(d))
#画出子图
plt.subplot(122)
nx.draw(part_G, with_labels=True, font_weight='bold')
plt.title('Before')
plt.axis('on')
plt.xticks([])
plt.yticks([])

plt.show()
