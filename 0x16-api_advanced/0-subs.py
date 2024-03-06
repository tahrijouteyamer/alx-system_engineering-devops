#!/usr/bin/python3
"""
    Uses Reddit API to print the number of subscribers of a subreddit
"""
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'CustomUserAgent/1.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        subreddit_info = response.json()
        return subreddit_info['data']['subscribers']
    elif response.status_code == 404:
        return 0
    else:
        return 0

# Example usage:
subreddit_name = "python"
subscribers_count = number_of_subscribers(subreddit_name)

if subscribers_count > 0:
    print(f"The subreddit '{subreddit_name}' has {subscribers_count} subscribers.")
else:
    print(f"The subreddit '{subreddit_name}' is not valid or not found.")

