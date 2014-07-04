import sys
import json

def main():
    
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    stop_words=["a"] #Add stop words if you wish to like a, the, etc (google search => stop words)
    scores={}
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    final_dict={}
    new_lst=[]
    score_lst=[]
    for line in tweet_file:
        a = json.loads(line)
        if "text" in a:
            tweet = a["text"]
            tweet_lst=tweet.split()
            sum=0
            for i in tweet_lst:
                if i in scores:
                    sum+=scores[i]
            if sum != 0 :
                for j in tweet_lst:
                    if j not in stop_words and j not in scores:
                        new_lst.append(j)
                        score_lst.append(sum)
    new_words={}                    
    for t in range (0,len(new_lst)):
        if new_lst[t] in new_words:
            new_words[new_lst[t]]+=[score_lst[t]] 
        else:
            new_words[new_lst[t]]=[score_lst[t]]        
    for key in new_words:
        l=new_words[key]
        avg= reduce(lambda x, y: x + y, l) / len(l)
        print key, avg
                                                
                    
    

if __name__ == '__main__':
    main()
