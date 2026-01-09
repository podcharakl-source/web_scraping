from datetime import datetime

def parse_tweet_data(tweet):
    """
    Extracts only the relevant fields from a raw Twikit tweet object.
    """
    return {
        'tweet_id': tweet.id,
        'user': tweet.user.screen_name,
        'text': tweet.full_text,
        'created_at': tweet.created_at,
        'likes': tweet.favorite_count,
        'retweets': tweet.retweet_count,
        'scraped_at': datetime.now().isoformat()
    }