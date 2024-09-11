import networkx as nx
import itertools

#Read from CSV:
f = open("Part7/clean_all.csv", "r")

a = f.read()
b = a.split("\n")

edge_list = []
for i in b:
    if i != "":
        s = i.split(",")
        edge_list.append((s[0], s[1]))
f.close()

G = nx.from_edgelist(edge_list)

gn = nx.community.girvan_newman(G)

for communities in itertools.islice(gn, 9):
    print(tuple(sorted(c) for c in communities))
