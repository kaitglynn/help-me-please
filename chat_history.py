```python
import json

chatHistory = []

class ChatSchema:
    def __init__(self, sender, message, timestamp):
        self.sender = sender
        self.message = message
        self.timestamp = timestamp

def add_to_chat_history(sender, message, timestamp):
    new_chat = ChatSchema(sender, message, timestamp)
    chatHistory.append(new_chat.__dict__)

def save_chat_history():
    with open('chat_history.json', 'w') as file:
        json.dump(chatHistory, file)

def load_chat_history():
    global chatHistory
    try:
        with open('chat_history.json', 'r') as file:
            chatHistory = json.load(file)
    except FileNotFoundError:
        chatHistory = []

def search_chat(keyword):
    load_chat_history()
    results = [chat for chat in chatHistory if keyword in chat['message']]
    return results
```