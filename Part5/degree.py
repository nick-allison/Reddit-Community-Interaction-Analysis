import networkx as nx

#Read from CSV:
f = open("Part5/clean_all.csv", "r")

a = f.read()
b = a.split("\n")

edge_list_2013 = []
edge_list_2014 = []
edge_list_2015 = []
edge_list_2016 = []
edge_list_2017 = []

for i in b:
    if i != "":
        s = i.split(",")
        if s[2] == "13":
            edge_list_2013.append((s[0], s[1]))
        elif s[2] == "14":
            edge_list_2014.append((s[0], s[1]))
        elif s[2] == "15":
            edge_list_2015.append((s[0], s[1]))
        elif s[2] == "16": 
            edge_list_2016.append((s[0], s[1]))
        elif s[2] == "17":
            edge_list_2017.append((s[0], s[1]))
f.close()

def outputInDegree(edge_list, filename):
    G = nx.DiGraph(edge_list)
    l = list(G.in_degree(G.nodes))
    l.sort(key= lambda a : a[1], reverse=True)
    f = open(filename, "w")
    for i in l:
        f.write(i[0] + ": " + str(i[1]) + "\n")
    f.close()

def outputOutDegree(edge_list, filename):
    G = nx.DiGraph(edge_list)
    l = list(G.in_degree(G.nodes))
    l.sort(key= lambda a : a[1], reverse=True)
    f = open(filename, "w")
    for i in l:
        f.write(i[0] + ": " + str(i[1]) + "\n")
    f.close()

outputInDegree(edge_list_2013, "Part5/2013_in_degree_values")
outputOutDegree(edge_list_2013, "Part5/2013_out_degree_values")
outputInDegree(edge_list_2014, "Part5/2014_in_degree_values")
outputOutDegree(edge_list_2014, "Part5/2014_out_degree_values")
outputInDegree(edge_list_2015, "Part5/2015_in_degree_values")
outputOutDegree(edge_list_2015, "Part5/2015_out_degree_values")
outputInDegree(edge_list_2016, "Part5/2016_in_degree_values")
outputOutDegree(edge_list_2016, "Part5/2016_out_degree_values")
outputInDegree(edge_list_2017, "Part5/2017_in_degree_values")
outputOutDegree(edge_list_2017, "Part5/2017_out_degree_values")


