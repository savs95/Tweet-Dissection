import sys  
import json 
import codecs

def main(): 
    happiness={}
    #you can add your own states too.
    states={'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'}
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary  
    for line in sent_file:
        term, score = line.split("\t") # The file is tab-delimited. "\t" means "tab character"  
        scores[term] = int(score) # Convert the score to an integer.  
    for line in tweet_file:
        a = json.loads(line)
        if 'place' in a and a['place'] is not None  : 
            if 'user' in a and a['user'] is not None and a['user']['location'] is not None:
                location=a['user']['location'].split(' ')
                if len(location)==2 and len(location[1])==2 and location[1] in states :
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
       
