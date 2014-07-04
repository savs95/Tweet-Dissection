import sys
import json

def main():
    tweet_file = open(sys.argv[1])
    freq={}
    for line in tweet_file:
        a = json.loads(line)
        if "text" in a:
            tweet = a["text"]
            tweet_lst=tweet.split()
            for i in tweet_lst :
                if i in freq :
                    freq[i]=freq[i]+1
                else :
                    freq[i]=1
    sum=0                
    for key in freq :
        sum+=freq[key]
    for key in freq :
        print key, freq[key]/float(sum)

if __name__ == '__main__':
    main()
            
                          
                    
    