import networkx as nx
import matplotlib.pyplot as plt
from math import ceil

# 该函数由于显示一组graph,传上来的是一组graph和这些graph的描述.
def ShowGraph(glists, ginfo, rowsize=3):
    # 每行放rowsize个,计算可以放多少行
    row = ceil(len(glists) / rowsize)

    # 定义组图
    plt.subplots(row, rowsize, figsize=(15, 3))

    # 开始画图
    for ind in range(len(glists)):
        # 定义子图
        plt.subplot(row, rowsize, ind + 1)
        nx.draw(glists[ind], with_labels=True, font_weight='bold')
        # 设置图片
        plt.title(ginfo[ind])
        plt.axis('on')
        plt.xticks([])
        plt.yticks([])
    plt.show()

# #添加单个节点
# G1 = nx.Graph()
# G1.add_node(1)
# G1.add_node('spam')
#
# #添加一组节点
# G2 = nx.Graph()
# G2.add_nodes_from([2, 3])
# G2.add_nodes_from('spam')
#
# #使用生成器
# G3 = nx.Graph()
# H = nx.path_graph(10)
# G3.add_nodes_from(H)
#
#
# glists=[G1, G2, G3]
# ginfo = ['add a node','add nodes','using generator']
# ShowGraph(glists,ginfo)

#添加单边
G1 = nx.Graph()
G1.add_edge(1,2)
G1.add_edge(3, 'm')

#添加一组边
G2 = nx.Graph()
e = (2,3)
G2.add_edge(*e)

#添加多组边
G3 = nx.Graph()
G3.add_edges_from([(3,4), (4,2)])

#使用边生成器
G4 = nx.Graph()
H = nx.path_graph(10)
G4.add_edges_from(H.edges)

#添加一组有权边
G5=nx.Graph()
G5.add_weighted_edges_from([('a', 'b', 5.0), ('b', 'c', 3.0), ('a', 'c', 1.0), ('c', 'd', 7.3)])  #边上权重显示看设置graph信息->指定边属性

glists=[G1, G2, G3, G4, G5]
ginfo=['add edge','add edge','add edges','using generator','weight edges']
ShowGraph(glists, ginfo, rowsize=5)
