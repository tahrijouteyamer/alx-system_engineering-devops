#!/usr/bin/python3
"""
Uses Reddit API to print the number of subscribers of a subreddit
"""
import requests
import ssl  # Import the ssl module

def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json().get("data")
    if data:
        num_subs = data.get("subscribers")
        # Use repr() to get a string representation of OPENSSL_VERSION
        ssl_version = repr(ssl.OPENSSL_VERSION)
        print("the 'ssl' module is compiled with {}.".format(ssl_version))  # Print the message
        return num_subs
    else:
        return 0

# Example usage:
if __name__ == "__main__":
    subreddit_name = "python"  # Replace with the desired subreddit name
    subscribers_count = number_of_subscribers(subreddit_name)
    print("Subscribers in r/{}: {}".format(subreddit_name, subscribers_count))

