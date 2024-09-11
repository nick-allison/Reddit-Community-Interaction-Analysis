import networkx as nx


#Read from CSV:
f = open("Part3/clean_all.csv", "r")

a = f.read()
b = a.split("\n")

edge_list = []
for i in b:
    if i != "":
        s = i.split(",")
        edge_list.append((s[0], s[1]))
f.close()

G = nx.from_edgelist(edge_list)

dc = nx.degree_centrality(G)
sorted_dc = {k: v for k, v in sorted(dc.items(), key=lambda item: item[1], reverse=True)}

bc = nx.betweenness_centrality(G)
sorted_bc = {k: v for k, v in sorted(bc.items(), key=lambda item: item[1], reverse=True)}

cc = nx.closeness_centrality(G)
sorted_cc = {k: v for k, v in sorted(cc.items(), key=lambda item: item[1], reverse=True)}

out = open("Part3/degree_centrality.txt", "w")
for i in sorted_dc:
    out.write(i + ": " + str(sorted_dc[i]) + "\n")
out.close()

out = open("Part3/betweenness_centrality.txt", "w")
for i in sorted_bc:
    out.write(i + ": " + str(sorted_bc[i]) + "\n")
out.close()

out = open("Part3/closeness_centrality.txt", "w")
for i in sorted_cc:
    out.write(i + ": " + str(sorted_cc[i]) + "\n")
out.close()