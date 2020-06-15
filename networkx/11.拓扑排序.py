import networkx as nx
import matplotlib.pyplot as plt


DG = nx.DiGraph([('a', 'b'), ('a', 'c'),('b', 'e'), ('b', 'd'),('c', 'e'), ('c', 'd'),('d', 'f'), ('f', 'g'), ('e', 'g')])

#显示graph
nx.draw_spring(DG,with_labels=True)
plt.title('DAG')
plt.axis('on')
plt.xticks([])
plt.yticks([])
plt.show()

#这个graph拓扑排序序列有很多,这里只给出一种
print('扑排序序列:',list(nx.topological_sort(DG)))
print('逆扑排序序列:',list(reversed(list(nx.topological_sort(DG)))))
