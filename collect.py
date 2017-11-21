
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from secrets import *
from initialize import Tweet
import json
import twitter

Base = declarative_base()

engine = create_engine('postgresql://tweetsql:tweetsql@tweetsql.cggizg1efi9f.us-east-1.rds.amazonaws.com/tweetsql')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.rollback()
session = DBSession()


TRACK = 'teaching'

twitter_auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_stream = twitter.TwitterStream(auth=twitter_auth)

statuses = twitter_stream.statuses.filter(track=TRACK)

for t in statuses:
    new_tweet = Tweet(data = json.dumps(t))
    session.add(new_tweet)
    session.commit()
    print(t)




