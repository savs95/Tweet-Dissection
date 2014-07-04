import sys
import json
import codecs

def main():
    hash_tags={}
    tweet_file = open(sys.argv[1])
    for line in tweet_file:
        a = json.loads(line)
        if "entities" in a:
            if "hashtags"  in a["entities"]:
                lst=(a["entities"]["hashtags"])
                if len(lst) > 0:
                    tag= lst[0]["text"]
                    if tag not in hash_tags:
                        hash_tags[tag]=1
                    else:
                        hash_tags[tag]+=1
    sorted_names = sorted(hash_tags.iteritems(), key=lambda (k, v): (-v, k))[:10]   #change argument here to get top n - [:n]
    for x,y in sorted_names:
        print x, y                 
                    

if __name__ == '__main__':
    main()        
