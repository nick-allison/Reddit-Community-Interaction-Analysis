import networkx as nx

#Read from CSV:
f = open("Part4/clean_all.csv", "r")

a = f.read()
b = a.split("\n")

edge_list = []
for i in b:
    if i != "":
        s = i.split(",")
        edge_list.append((s[0], s[1]))
f.close()

G = nx.DiGraph(edge_list)

l = list(G.in_degree(G.nodes))
l.sort(key= lambda a : a[1], reverse=True)

f = open("Part4/in_degree.txt", "w")
for i in l:
    f.write(i[0] + ": " + str(i[1]) + "\n")
f.close()

l = list(G.out_degree(G.nodes))
l.sort(key= lambda a : a[1], reverse=True)

f = open("Part4/out_degree.txt", "w")
for i in l:
    f.write(i[0] + ": " + str(i[1]) + "\n")
f.close()