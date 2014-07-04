Tweet Dissection
----------------
These set of codes does the following 5 things :

 1. Prints the output of sentiment of each tweet (the higher the score, the more positive is the tweet, if in negatives, as the magnitude increases, the higher the magnitude, more negative is the tweet.
 2. Tries to determine non-sentimental terms, which can be related to sentiments. Eg if the word soccer always appears in proximity with positive words like great and fun, then we can deduce that the term soccer itself carries a positive sentiment.
 3. Computes the term frequency histogram of the livestream twitter data.
 4. Prints the happiest state (USA only), based on number of positive tweets.
 5. Prints the top ten hash-tags (#), from the data obtained.

Instructions on setting up:

 - Enter the oauth keys in "twitterstream.py" and store output in a file Eg. "$ python twitterstream.py > tweets.txt". You can also modify the queries (instruction given in the code). Run it for 10 min. and don't forget to end the process.
 - "tweet_sentiment.py" which accepts two arguments on the command line: a sentiment file and a tweet file and prints the sentiment of each tweet. To run it "$python tweet_sentiment.py AFFIN-111.txt tweet.txt " .
 - "term_sentiment.py" tries to determine non-sentimental term. Run "$ python term_sentiment.py AFFIN111.txt tweet.txt" .
 - "frequency.py" computes histogram of livestream data ie tweet.txt. Run "$ python frequency.py tweet.txt" .
 - "happiest_state.py" prints the happiest state (US only). Run "$python happiest_state.py AFFIN-111.txt tweet.txt" .
 - "top_ten.py" computes the top ten hashtags from tweet.txt. Run " $python top_ten.py tweet.txt" .

Note : This works with python 2.7 , and you might need to install a few libraries, before this can function. 

## Happy Disecting Data :) !!!
