import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}  # Set a custom User-Agent to avoid potential issues
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0
    else:
        return 0

# Example usage:
subreddit_name = 'python'
print(f"Number of subscribers in r/{subreddit_name}: {number_of_subscribers(subreddit_name)}")