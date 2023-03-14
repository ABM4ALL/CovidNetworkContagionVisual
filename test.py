# -*- coding:utf-8 -*-
# @Time: 2023/1/8 9:27
# @Author: Zhanyi Hou
# @Email: 1295752786@qq.com
# @File: test.py.py

import networkx as nx
import ast

G = nx.read_gexf('out.gexf', node_type=ast.literal_eval)
print(G.nodes[(0, 0)]['viz'])
