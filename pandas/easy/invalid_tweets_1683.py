import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    result = tweets[tweets.content.str.len() > 15].get(["tweet_id"])

    return result

tweets = [
    {'tweet_id': 1, 'content': 'Let us Code'},
    {'tweet_id': 2, 'content': 'More than fifteen chars are here!'}
]

df = pd.DataFrame(tweets)

df = invalid_tweets(df)

print(df)