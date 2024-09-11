Since figuring out different centralities was going to be just about impossible for me, I decided that the next best thing would be calculating in and out degree for each of the nodes in the graph, then comparing these results to the page rank of each reddit.

I used the same clean_data file as I did in part 1, and I wrote some simple Python code to calculate the in-degree for each node and rank these values, then do the same with out degree.

The results showed that in degree tends to correlate with page rank moreso than out degree (which I would have guessed), but I felt that out degree was also an interesting metric to look at.

This part of the project was a success