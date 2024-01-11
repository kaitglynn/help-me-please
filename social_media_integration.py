```python
import requests
from requests_oauthlib import OAuth1

class SocialMediaIntegration:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)

    def post_to_twitter(self, message):
        url = 'https://api.twitter.com/1.1/statuses/update.json'
        data = {'status': message}
        response = requests.post(url, auth=self.auth, data=data)
        return response.status_code == 200

    def post_to_facebook(self, message, page_id, access_token):
        url = f"https://graph.facebook.com/{page_id}/feed"
        payload = {
            'message': message,
            'access_token': access_token
        }
        response = requests.post(url, params=payload)
        return response.status_code == 200

    def post_to_linkedin(self, message, access_token):
        url = "https://api.linkedin.com/v2/ugcPosts"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0"
        }
        payload = {
            "author": f"urn:li:person:{access_token}",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": message
                    },
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.status_code == 201
```