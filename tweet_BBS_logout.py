#!/usr/bin/env python
# tweet.py by Alex Eames http://raspi.tv/?p=5908
# Modified to tweet BBS connections

import tweepy, sys, datetime

# Consumer keys and access tokens, used for OAuth
consumer_key = 'Dle8m1UT0PPDiClP3G5EwAfyd'
consumer_secret = 'Jh1ziP42axm2Mv6tMOk0JkLFaLLImkeCGoAr7MV9moEtutQcK6'
access_token = '947191999425339394-lFRJF4z42gYMH55wdCrxbqObJeDHkrw'
access_token_secret = 'vDkyVC79HIzXzK84Arjnmw9zMEHN5PiR9svtc5TpokDDf'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)
time = datetime.datetime.now()
timenow = '{:%H:%M:%S}'.format(time)

if len(sys.argv) >= 2:
    tweet_text = sys.argv[1] + " while leaving wonders .. is that a real poncho or is that a Sears poncho? @ " + str(timenow)

else:
    tweet_text = "Still messing about with tweepy and twitter API. :)"

if len(tweet_text) <= 280:
    api.update_status(status=tweet_text)
else:
    tweet_text = "UserName too long!"
