'''
COMP90024 Cluster and Cloud Computing Assignment 2
Team 22

Zizhao Li (1267416) zizhaol2@student.unimelb.edu.au (Suzhou, China)
Fu Zhu (1166186) fuzhu@student.unimelb.edu.au (Melbourne, Australia)
Chuting Wang (1074511) chutingw@student.unimelb.edu.au (Xi’an, China)
Xuezhu Wu (938808) xuezhuw@student.unimelb.edu.au (Hangzhou, China)
Yuepeng Sheng (1048382) yuepengs@student.unimelb.edu.au (Shanghai, China)
'''


import json
import couchdb
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from find_lga import *

def text_clean(text):
    text = re.sub(r"\s*@\S*?\s*(:| |$)", " ", text)  # remove @
    text = re.sub(r"\[\S+\]", "", text) #remove emoji
    text = re.sub(r"http\S+", "", text) #remove http
    return text.strip()

## text sentimental analysis
def sentimental(text):
    score = SentimentIntensityAnalyzer().polarity_scores(text)
    neg=score['neg']
    pos=score['pos']
    if neg>pos:
        out=-1
    elif neg<pos:
        out=1
    elif neg==pos:
        out=0
    return out


def exit_process(tweet):
    output={} 
    output['tweetID'] = tweet['id']
    output['userID'] = tweet['doc']['user']['id']
    output['datetime'] = ' '.join(str(v) for v in tweet['key'][1:])
    output['text'] = text_clean(tweet['doc']['text'])
    output['sentimental'] = sentimental(output['text'])
    output['geo'] = tweet['doc']['coordinates']
    output['location'] = find_lga(tuple(tweet['doc']['coordinates']['coordinates']))
    if any(key_word in output['text'].lower() for key_word in ['covid','covid-19','covid test spot','hospital','pandemic']):
        output['label'] = 'health'
    elif any(key_word in output['text'].lower() for key_word in ['house','housing','rent']):
        output['label'] = 'house'
    elif any(key_word in output['text'].lower() for key_word in ['train','tram','metro','bus','uber']):
        output['label'] = 'transportation'
    else:
        output['label'] = None
    return output

#Database connection
server = "http://admin:password@172.26.130.194:5984/"
couchclient = couchdb.Server(server)
try:
    db = couchclient['historytime_sent_new']
except:
    db = couchclient.create('historytime_sent_new')


f3 = open ('twitter-melb.json','r')
f3.readline()
for i in range(10000):
    line = f3.readline()
    if len(line)<=3:
        break
    if(line[-3]==']'):
        line = line[:-3]+',\n'
    if(line[-2]!=','):
        line=line[:-1]+',\n'   
    tweet=json.loads(line[:-2])
    if (not tweet['doc']['text'].startswith('RT')) and (tweet['doc']['coordinates'] != None):
        data=exit_process(tweet)
        if (not data['label'] == None) and (not data['location'] == None):
            db.save(data)
f3.close()