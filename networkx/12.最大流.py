'''
maximum_flow(flowG, _s, _t, capacity='capacity', flow_func=None, **kwargs)
flowG: 图
_s：起点
_t：终点
capacity:容量
flow_func:计算最大流的方法，默认是 preflow_push()，还有maximum_flow_value(), minimum_cut(), minimum_cut_value(), edmonds_karp(),, shortest_augmenting_path()

https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.flow.maximum_flow.html?highlight=maximum_flow

'''


import networkx as nx
import matplotlib.pyplot as plt

#构建graph
G = nx.DiGraph()
G.add_edge('x','a', capacity=3.0)
G.add_edge('x','b', capacity=1.0)
G.add_edge('a','c', capacity=3.0)
G.add_edge('b','c', capacity=5.0)
G.add_edge('b','d', capacity=4.0)
G.add_edge('d','e', capacity=2.0)
G.add_edge('c','y', capacity=2.0)
G.add_edge('e','y', capacity=3.0)
pos=nx.spring_layout(G)

#显示graph
edge_labels = nx.get_edge_attributes(G,'capacity')
nx.draw_networkx_nodes(G,pos)
nx.draw_networkx_labels(G,pos)
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_edge_labels(G, pos,edge_labels)
plt.axis('on')
plt.xticks([])
plt.yticks([])
plt.show()

#求最大流
flow_value, flow_dict = nx.maximum_flow(G, 'x', 'y')
print("最大流值: ",flow_value)
print("最大流流经途径: ",flow_dict)
