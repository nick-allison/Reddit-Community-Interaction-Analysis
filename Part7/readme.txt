I was determined to identify communities of subbreddits, but the most natural starting point was no longer an option.  Logic would dictate that if finding the max clique required too much computing power, then so would finding things such as the max k-plex, the max k-club, or the max k-clan.  Each of these takes more nodes into account at each step and results in larger subgraphs at every step.

The next community identification strategy I tried was using the girvan newman algorithm to identify hierarchical communities of subreddits.  This would also allow me to compare different layers of a hierarchy, which would open the door for quite a bit of additional interesting analysis.

I copied over the appropriate clean data file and wrote some Python code, however once again the code failed to finish after several hours.

This part of the project was unsuccessful.