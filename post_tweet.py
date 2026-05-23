import tweepy
import os

client = tweepy.Client(
    consumer_key=os.environ["API_KEY"],
    consumer_secret=os.environ["API_SECRET"],
    access_token=os.environ["ACCESS_TOKEN"],
    access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]
)

tweet_text = """🚨 NEET UG Paper Leak — Demand Justice!

The Cockroach Janata Party demands removal of Education Minister Dharmendra Pradhan.

1,50,000+ people have already signed. Join now!

#NEETScam #NEETPaperLeak #RemoveDharmendraPradhan #StudentsDeserveJustice"""

client.create_tweet(text=tweet_text)
print("Tweet posted successfully!")
