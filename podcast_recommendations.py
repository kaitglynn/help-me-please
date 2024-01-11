```python
import requests
import json

def recommendPodcast(userProfile):
    # Fetch user interests from the profile
    user_interests = userProfile['interests']

    # API endpoint for podcast recommendations
    api_url = "https://api.podcast.com/recommendations"

    # Prepare the payload with user interests
    payload = {
        "interests": user_interests
    }

    # Make a POST request to the API
    response = requests.post(api_url, data=json.dumps(payload))

    # If the request was successful, parse the response
    if response.status_code == 200:
        recommendations = response.json()

        # Prepare a message with the recommended podcasts
        message = "Here are some podcast recommendations based on your interests:\n"
        for podcast in recommendations:
            message += f"- {podcast['title']} by {podcast['author']}\n"

        # Return the message
        return message

    else:
        # If the request was not successful, return an error message
        return "Sorry, I couldn't fetch podcast recommendations at the moment."
```