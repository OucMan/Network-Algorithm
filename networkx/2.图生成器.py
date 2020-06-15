import networkx as nx
import matplotlib.pyplot as plt

# 小图图集生成器
# G = nx.graph_atlas()
# graph_atlas的图已经被定义,只需要按标号取出来就可以,下面将前10个取出来
# plt.subplots(2, 5, figsize=(15, 6))
# for ind in range(10):
#     G = nx.graph_atlas(ind)
#     plt.subplot(2, 5, ind + 1)
#     nx.draw(G, with_labels=True)
#     plt.axis('on') # 显示坐标轴
#     plt.title('graph_atlas_%s' % ind)
#     plt.xticks([]) # 横坐标不需要刻度
#     plt.yticks([]) # 纵坐标不需要刻度
# plt.show()
# plt.close()

# 经典图集

plt.subplots(2,2,figsize=(15,6))

K_5 = nx.complete_graph(5)
plt.subplot(221)
plt.title('complete_graph')
nx.draw(K_5, with_labels=True, font_weight='bold')
plt.axis('on')
plt.xticks([])
plt.yticks([])

K_3_5 = nx.complete_bipartite_graph(3, 5)
plt.subplot(222)
plt.title('complete_bipartite_graph')
nx.draw(K_3_5, with_labels=True, font_weight='bold')
plt.axis('on')
plt.xticks([])
plt.yticks([])

barbell = nx.barbell_graph(10, 10)
plt.subplot(223)
plt.title('barbell_graph')
nx.draw(barbell, with_labels=True, font_weight='bold')
plt.axis('on')
plt.xticks([])
plt.yticks([])

lollipop = nx.lollipop_graph(10, 20)
plt.subplot(224)
plt.title('lollipop_graph')
nx.draw(lollipop, with_labels=True, font_weight='bold')
plt.axis('on')
plt.xticks([])
plt.yticks([])

plt.show()

# 此外还有许多类型的图生成器，如社交网络、树、格子图等等
