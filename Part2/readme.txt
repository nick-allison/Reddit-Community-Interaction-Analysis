While analyzing my results from part 1 of this project, I was not very much surprised by any of the top subReddits.  Things like askreddit and videos make sense at the top of this ranking.  I was however a bit interested in lines 24-26 of my output from part 1.  These are all subrettits about political topics.  The data in my dataset is from 2013 to 2017, and includes interactions that took place leading up to and during the 2016 election.  My next step would be to compare the page rank of different subreddits for each year!

I made some modifications to the "clean_data.py" file I used in part 1 to include the last 2 digits of the year for each node.

I then made some similar modifications to my "page_rank.py" file from part 1 so that it would create a graph for each year between 2013 and 2017, then calculate pagerank for the nodes of these graphs.

The results can be seen in each of the 20xx_pagerank_values files.  This part was also a success!

My analysis of the results is that the page rank of more political subrettits tended to increase year by year, with the "the_donald" subreddit in particular ending very close to the top.  I would have expected a peak for political subreddits in 2015 and 2016, however it seems that the trend continued even after the election.