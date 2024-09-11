import networkx as nx
import numpy
import scipy

#Read from CSV:
f = open("Part2/clean_all.csv", "r")

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

def outputFunciton(edge_list, filename):
    G = nx.DiGraph(edge_list)
    pr = nx.pagerank(G)
    sorted_pr = {k: v for k, v in sorted(pr.items(), key=lambda item: item[1], reverse=True)}
    out = open(filename, "w")
    for i in sorted_pr:
        out.write(i + ": " + str(sorted_pr[i]) + "\n")
    out.close()

outputFunciton(edge_list_2013, "Part2/2013_pagerank_values")
outputFunciton(edge_list_2014, "Part2/2014_pagerank_values")
outputFunciton(edge_list_2015, "Part2/2015_pagerank_values")
outputFunciton(edge_list_2016, "Part2/2016_pagerank_values")
outputFunciton(edge_list_2017, "Part2/2017_pagerank_values")


