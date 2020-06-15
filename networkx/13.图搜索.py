'''
https://networkx.github.io/documentation/stable/reference/algorithms/traversal.html
'''
import networkx as nx
import matplotlib.pyplot as plt

#################广度优先搜索（BFS）
#构建一个长度为10的路径
# G = nx.path_graph(10)
#
# #显示graph
# nx.draw_spring(G,with_labels=True)
# plt.axis('on')
# plt.xticks([])
# plt.yticks([])
# plt.show()
#
# #以4为顶点,广度遍历
# print(list(nx.bfs_tree(G,4)))

#################深度优先搜索（DFS）

#构建一个长度为10的路径
G = nx.path_graph(10)

#显示graph
nx.draw_spring(G,with_labels=True)
plt.axis('on')
plt.xticks([])
plt.yticks([])
plt.show()

#以5为顶点,深度遍历,限定深度为3
T = nx.dfs_tree(G, source=5, depth_limit=3)
print(list(T))

