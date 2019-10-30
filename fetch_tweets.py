import tweepy




ckey = "nYKSjSpE5IrO9y7qECVk4jMMu"
csecret = "YdCeEYJSGHVscthswLnNiDHmM7N24hSM82hslTVsRpgmn9evD3"
atoken = "282101457-b7VzdJJnzNYzHrS6VwC7OCOzHOIKjedYI9NBP3ts"
asecret = "MRSCxDqpIxdkGHj6SDAdh693tYxkTyyKPFS9TaKBI8fHq"

OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret,
'access_token_key':atoken, 'access_token_secret':asecret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api =tweepy.API(auth)

tweets = tweepy.Cursor(api.search, q='Australia', rpp='100').items(100)
tweet_list = []
for tweet in tweets:
   print(tweet.text, tweet.lang)
   # we append a new line for when we save to a file

   tweet_list.append(tweet.text.strip() + "\n")

f=open('tweet_data.txt','w', encoding="utf-8")
f.writelines(tweet_list)
print("fetched " + str(len(tweet_list)) + " tweets")

