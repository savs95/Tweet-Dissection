import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    final_dict={}
    for line in tweet_file:
        a = json.loads(line)
        if "text" in a:
            tweet = a["text"]
            tweet_lst=tweet.split()
            sum=0
            for i in tweet_lst:
                if i in scores:
                    sum+=scores[i]
            print sum

if __name__ == '__main__':
    main()
