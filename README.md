Tweet Dissection
----------------
These set of codes does the following 5 things :

 1. Prints the output of sentiment of each tweet (the higher the score, the more positive is the tweet, if in negatives, as the magnitude increases, the higher the magnitude, more negative is the tweet.
 2. Tries to determine non-sentimental terms, which can be related to sentiments. Eg if the word soccer always appears in proximity with positive words like great and fun, then we can deduce that the term soccer itself carries a positive sentiment.
 3. Computes the term frequency histogram of the livestream twitter data.
 4. Prints the happiest state (USA only), based on number of positive tweets.
 5. Prints the top ten hash-tags (#), from the data obtained.

Instructions on setting up:

 - Enter the oauth keys in "twitterstream.py" and store output in a file Eg. "$ python twitterstream.py > tweets.txt". You can also modify the queries (instruction given in the code)
 - "tweet_sentiment.py" which accepts two arguments on the command line: a sentiment file and a tweet file and prints the sentiment of each tweet. To run it "$python tweet_sentiment.py AFFIN-111.txt tweet.txt "
