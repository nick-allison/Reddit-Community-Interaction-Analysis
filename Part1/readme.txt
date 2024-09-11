Immediately after I began to consider how I might process the data, I realized that there was a lot of information included in the dataset that I would not need, the dataset was in a weird format, and it would make more sense for title and body links to all be combined.  I was required to do a little bit of cleaning.

I wrote a basic Python program, "clean_data.py", which I used to generate the "clean_all.csv" file from the .tsv files that composed my dataset.  Clean_all.csv only contains the basic information that I need to build a graph, and is in a format that I am more used to working with.

My next step was to use the Networkx library to create a graph and rank each node by PageRank.  This took me a little bit of playing around, since I have never used Networkx to determine PageRank, but I was able to create "page_rank.py" which outputs a text file containing every node's page rank value in sorted order.

The PageRank rankings for the data set can be seen in "pagerank_values.txt".  This first task was a success.

I thought that I might have some problems with Page Rank due to the size of my data set, but I was able to perform the desired calculations in a very reasonable amount of time.  This makes sense in hind-sight, because ranking web sites would involve a much larger data set than the one I am working with, so it is logical that page rank can handle large amounts of data.  I assumed that since it was more challenging for me to calculate Page Rank than centralities on paper, that a computer would have a similar experience; this was not the case.