import asyncio
import yaml
import pandas as pd
from twikit import Client
from parser import parse_tweet_data

async def main():
    # 1. Load Configuration
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    # 2. Initialize Client
    client = Client('en-US')
    
    # login (Uses cookies if available to avoid blocks)
    try:
        client.load_cookies('cookies.json')
    except:
        await client.login(
            auth_info_1=config['auth']['username'],
            auth_info_2=config['auth']['email'],
            password=config['auth']['password']
        )
        client.save_cookies('cookies.json')

    all_data = []

    # 3. Loop through EV keywords
    for query in config['search']['queries']:
        print(f"Searching for: {query}")
        tweets = await client.search_tweet(query, 'Top')
        
        for tweet in tweets:
            clean_tweet = parse_tweet_data(tweet)
            all_data.append(clean_tweet)
        
        # Respectful delay to avoid bans
        await asyncio.sleep(5) 

    # 4. Save to CSV
    df = pd.DataFrame(all_data)
    df.to_csv('data/ev_comments.csv', index=False)
    print(f"Saved {len(all_data)} comments to data/ev_comments.csv")

if __name__ == "__main__":
    asyncio.run(main())