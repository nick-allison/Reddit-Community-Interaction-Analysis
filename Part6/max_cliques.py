import networkx as nx

#Read from CSV:
f = open("Part6/clean_all.csv", "r")

a = f.read()
b = a.split("\n")

edge_list = []
for i in b:
    if i != "":
        s = i.split(",")
        edge_list.append((s[0], s[1]))
f.close()

G = nx.from_edgelist(edge_list)

print({n: sum(1 for c in nx.find_cliques(G) if n in c) for n in G})

