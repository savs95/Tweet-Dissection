import sys  
import json 
import codecs

def main(): 
    happiness={}
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary  
    for line in sent_file:
        term, score = line.split("\t") # The file is tab-delimited. "\t" means "tab character"  
        scores[term] = int(score) # Convert the score to an integer.  
    for line in tweet_file:
        a = json.loads(line)
        if 'place' in a and a['place'] is not None and a['place']['country_code']=='US' : # You can choose your country
            if 'user' in a and a['user'] is not None and a['user']['location'] is not None:
                location=a['user']['location'].split(' ')
                if len(location)==2 and len(location[1])==2:
                    if 'text' in a:
                        sent_score=0
                        words = a['text'].split()
                        for word in words: 
                            if word in scores:
                                sent_score+=scores[word]
                        if location[1] not in happiness:
                            happiness[location[1]]=sent_score
                        else:
                            happiness[location[1]]+=sent_score
    sorted_names = sorted(happiness.iteritems(), key=lambda (k, v): (-v, k))[0]  #get n number of states - [:n]                           
    f=sorted_names[0].encode('ascii', 'ignore')
    print f
            

if __name__ == '__main__':
    main()
       
