from src.parser import parse_tweet_data

# 1. Create a "Fake" tweet object that mimics what Twikit sends
class MockTweet:
    def __init__(self):
        self.id = "12345"
        self.user = type('User', (), {'screen_name': 'EV_Fan_99'})()
        self.full_text = "Thinking of buying an EV, but I'm worried about range."
        self.created_at = "2026-01-09"
        self.favorite_count = 10
        self.retweet_count = 2

# 2. Run the parser
test_tweet = MockTweet()
result = parse_tweet_data(test_tweet)

# 3. Verify it works
print("Parsed Result:", result)
assert result['user'] == 'EV_Fan_99'
print("✅ Parser Test Passed!")