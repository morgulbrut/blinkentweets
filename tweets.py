#!/usr/bin/env python3

# https://www.storybench.org/how-to-collect-tweets-from-the-twitter-streaming-api-using-python/

import opc, time, sys
import settings, hashtags
import tweepy

numLEDs = 512

counts = [0]*numLEDs
pixels = [ (0,0,0) ] * numLEDs

client = opc.Client(settings.address)


# StreamListener class inherits from tweepy.StreamListener and overrides on_status/on_error methods.
class StreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        
        # # if "retweeted_status" attribute exists, flag this tweet as a retweet.
        # is_retweet = hasattr(tweet, "retweeted_status")

        # check if text has been truncated
        if hasattr(tweet,"extended_tweet"):
            text = tweet.extended_tweet["full_text"]
        else:
            text = tweet.text
        ht = ['#'+t['text'].lower() for t in tweet.entities['hashtags']]
        
        for h in ht:
            try:
                i = hashtags.hashtags.index(h)
                counts[i] += 1

                for i in range(numLEDs):
                    pixels[i] = (0, (counts[i]*5)%255, 0)
                    client.put_pixels(pixels)
                print(ht)
            except:
                pass


    def on_error(self, status_code):
        if status_code == 420:
            print("Encountered streaming error (", status_code, ")")
            time.sleep(5)
        else:
            print("Encountered streaming error (", status_code, ")")
            sys.exit()

if __name__ == "__main__":
    # complete authorization and initialize API endpoint
    auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)
    auth.set_access_token(settings.access_key, settings.access_secret)
    api = tweepy.API(auth)

    for i in range(numLEDs):
        pixels[i] = (0, 0, 0)
        client.put_pixels(pixels)
    # initialize stream
    streamListener = StreamListener()
    while true:
        try:
            stream = tweepy.Stream(auth=api.auth, listener=streamListener,tweet_mode='extended')
            stream.filter(track=hashtags.hashtags)
        except:
            print("stream error")
            time.sleep(30)