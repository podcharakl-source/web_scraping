import json

# Load the messy browser export
with open('cookies.json', 'r') as f:
    bad_cookies = json.load(f)

# Convert to simple key-value pairs
# This handles both list format and object format
clean_cookies = {}
if isinstance(bad_cookies, list):
    for c in bad_cookies:
        clean_cookies[c['name']] = c['value']
else:
    clean_cookies = bad_cookies

# Save the clean version back
with open('cookies.json', 'w') as f:
    json.dump(clean_cookies, f, indent=4)

print("✅ cookies.json has been flattened and is ready for use!")