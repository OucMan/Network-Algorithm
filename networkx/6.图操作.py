import networkx as nx
import matplotlib.pyplot as plt

########删除边或者节点
# 生成图
#
# G = nx.path_graph(8)
# plt.subplots(1, 2, figsize=(15, 5))
# plt.suptitle('Remove')
#
# # 画出未操作前的graph
# plt.subplot(121)
# nx.draw(G, with_labels=True, font_weight='bold')
# plt.title('Before')
# plt.axis('on')
# plt.xticks([])
# plt.yticks([])
#
# # 移除部分节点和边,移除所有的点和边使用G.clear()
# G.remove_node(2)
# G.remove_nodes_from([1, 5])
# G.remove_edge(3, 4)
#
# #画出操作后的graph
# plt.subplot(122)
# nx.draw(G, with_labels=True, font_weight='bold')
# plt.title('After')
# plt.axis('on')
# plt.xticks([])
# plt.yticks([])
#
# #显示graph
# plt.show()

############合并操作

# plt.subplots(1, 3, figsize=(15,5))
# plt.suptitle('Union')
#
# # 生成graph1
# G1 = nx.path_graph(8)
# plt.subplot(131)
# nx.draw(G1, with_labels=True, font_weight='bold')
# plt.title('Graph1')
# plt.axis('on')
# plt.xticks([])
# plt.yticks([])
#
# # 生成graph2
# G2 = nx.complete_graph(3)
# plt.subplot(132)
# nx.draw(G2, with_labels=True, font_weight='bold')
# plt.title('Graph2')
# plt.axis('on')
# plt.xticks([])
# plt.yticks([])
# # 合并
# G3 = nx.disjoint_union(G1,G2)
# plt.subplot(133)
# nx.draw(G3, with_labels=True, font_weight='bold')
# plt.title('After union',)
# plt.axis('on')
# plt.xticks([])
# plt.yticks([])
#
# # 显示graph
# plt.show()


#################无向图转有向图

# plt.subplots(1,2,figsize=(15,3))
# plt.suptitle('Graph ---> DiGraph')
#
# #定义无向图
# G = nx.path_graph(8)
# #转换为有向图
# G2 = G.to_directed()
#
# plt.subplot(121)
# nx.draw(G, with_labels=True, font_weight='bold')
# plt.title('Before')
# plt.axis('on')
# plt.xticks([])
# plt.yticks([])
#
# plt.subplot(122)
# nx.draw(G2, with_labels=True, font_weight='bold')
# plt.title('After')
# plt.axis('on')
# plt.xticks([])
# plt.yticks([])
# plt.show()

##################有向图转无向图

plt.subplots(1,2,figsize=(15,3))
plt.suptitle('DiGraph ---> Graph')

#定义有向图
G = nx.path_graph(8, create_using=nx.DiGraph())
#转换为无向图
G2 = G.to_undirected()

plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
plt.title('Before')
plt.axis('on')
plt.xticks([])
plt.yticks([])

plt.subplot(122)
nx.draw(G2, with_labels=True, font_weight='bold')
plt.title('After')
plt.axis('on')
plt.xticks([])
plt.yticks([])
plt.show()
