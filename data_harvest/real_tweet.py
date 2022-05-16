## tweepy == 3.10.0
'''
COMP90024 Cluster and Cloud Computing Assignment 2
Team 22

Zizhao Li (1267416) zizhaol2@student.unimelb.edu.au (Suzhou, China)
Fu Zhu (1166186) fuzhu@student.unimelb.edu.au (Melbourne, Australia)
Chuting Wang (1074511) chutingw@student.unimelb.edu.au (Xi’an, China)
Xuezhu Wu (938808) xuezhuw@student.unimelb.edu.au (Hangzhou, China)
Yuepeng Sheng (1048382) yuepengs@student.unimelb.edu.au (Shanghai, China)
'''



import tweepy
import json
import couchdb
import time
import re
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

## set location boundary 
mel_coor = [-37.840935,144.946457]
vic_coor = [140.96,-39.2,150.03,-33.98]


## get api set 
apiset=[]
for i in json.load(open("api.json"))['API']:
    auth = tweepy.OAuthHandler(i['consumer_key'], i['consumer_secret'])
    auth.set_access_token(i['access_token'], i['access_token_secret'])
    apiset.append(tweepy.API(auth))


#Define Database connection creds
server = "http://admin:password@172.26.130.194:5984/"
couchclient = couchdb.Server(server)
# 确保每次Realtime数据库里都是最新爬到的信息
# if 'realtime' in couchclient:
#     couchclient.delete('realtime')
try:
    db = couchclient['realtime_sent_new']
except:
    db = couchclient.create('realtime_sent_new')

## remove @,emoji,http from text
def text_clean(text):
    text = re.sub(r"\s*@\S*?\s*(:| |$)", " ", text)  # remove @
    text = re.sub(r"\[\S+\]", "", text) #remove emoji
    text = re.sub(r"http\S+", "", text) #remove http
    return text.strip()

## text sentimental analysis
def sentimental(text):
    score = SentimentIntensityAnalyzer().polarity_scores(text)
    # max(zip(score.values(), score.keys()))[1]
    neg=score['neg']
    pos=score['pos']
    if neg>pos:
        out=-1
    elif neg<pos:
        out=1
    elif neg==pos:
        out=0
    return out

## extract the needed information from tweet
def process(data):
    out={}
    out['tweetID']=data['id']
    out['userID'] = data['user']['id']
    out['datetime'] = ' '.join(data['created_at'].split(' ')[1:4])
    out['text']=text_clean(data['text'])
    out['sentimental'] = sentimental(out['text'])
    out['geo'] = data['coordinates']
    if any(key_word in out['text'].lower() for key_word in ['covid','covid-19','covid test spot','hospital','pandemic']):
        out['label'] = 'health'
    elif any(key_word in out['text'].lower() for key_word in ['house','housing','rent']):
        out['label'] = 'house'
    elif any(key_word in out['text'].lower() for key_word in ['train','tram','metro','bus','uber']):
        out['label'] = 'transportation'
    else:
        out['label'] = None
    return out


# 继承 StreamListener
class MyStreamListener(tweepy.StreamListener):
    def __init__(self,db):
        super().__init__()
        ## limit the max tweets number
        self.max_tweets = 100000
        self.tweet_count = 0
        self.db=db
        
    def on_data(self, raw_data):
        if(self.tweet_count==self.max_tweets):
            return(False)
        else:
            decoded = json.loads(raw_data)
            ## ignore retweet
            if  (decoded['retweeted']==False) and (not decoded['text'].startswith('RT')):
                self.process_data(decoded)
                self.tweet_count+=1

    def process_data(self,raw_data):
        output = process(raw_data)
        if not output['label'] == None:
            self.db.save(output)

    # returning False in on_error disconnects the stream
    def on_error(self, status_code):
        if status_code == 420:
            return False 

## stream tweets from each TwitterAPI

for api in apiset:
    try:
        twitterStream = tweepy.Stream(api.auth,MyStreamListener(db))
        twitterStream.filter(track=['covid','covid-19','pandemic','covid test spot','hospital','house','housing','rent','train','tram','metro','bus','uber'],languages=['en'],locations=vic_coor,stall_warnings=True)
    except Exception as e:
        print('Disconnected...')
        time.sleep(5)
        continue