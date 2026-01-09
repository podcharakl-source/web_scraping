import asyncio
import yaml
import pandas as pd
from twikit import Client
from parser import parse_tweet_data
import os

async def main():
    print("🚀 Starting EV Tweet Scraper...")
    # 1. Load Config
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    client = Client('en-US')

    # 2. Use ONLY cookies to avoid Cloudflare 403
    if os.path.exists('cookies.json'):
        client.load_cookies('cookies.json')
        print("✅ Session loaded from cookies. Cloudflare bypassed.")
    else:
        print("❌ Error: 'cookies.json' not found!")
        print("Please export your X cookies from your browser and save them to 'cookies.json'.")
        return

    all_data = []
    
    # 3. Search Loop
    for query in config['search']['queries']:
        print(f"Searching for: {query}")
        try:
            # Added a slight delay to look more 'human'
            await asyncio.sleep(2) 
            tweets = await client.search_tweet(query, 'Top')
            
            for tweet in tweets:
                all_data.append(parse_tweet_data(tweet))
        except Exception as e:
            print(f"⚠️ Could not scrape {query}: {e}")

    # 4. Save Data
    if all_data:
        df = pd.DataFrame(all_data)
        df.to_csv('data/ev_comments.csv', index=False)
        print(f"🎉 Success! Saved {len(all_data)} rows.")

if __name__ == "__main__":
    asyncio.run(main())