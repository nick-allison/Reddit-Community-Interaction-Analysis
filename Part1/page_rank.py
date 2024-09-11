import networkx as nx
import numpy
import scipy

#Read from CSV:
f = open("Part1/clean_all.csv", "r")

a = f.read()
b = a.split("\n")

edge_list = []
for i in b:
    if i != "":
        s = i.split(",")
        edge_list.append((s[0], s[1]))
f.close()

G = nx.DiGraph(edge_list)

pr = nx.pagerank(G)

sorted_pr = {k: v for k, v in sorted(pr.items(), key=lambda item: item[1], reverse=True)}

out = open("Part1/pagerank_values.txt", "w")
for i in sorted_pr:
    out.write(i + ": " + str(sorted_pr[i]) + "\n")

out.close()