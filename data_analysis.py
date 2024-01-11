```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class DataAnalysis:
    def __init__(self, chatHistory):
        self.chatHistory = chatHistory

    def load_data(self):
        self.data = pd.DataFrame(self.chatHistory)

    def analyze_chat_frequency(self):
        chat_frequency = self.data['user'].value_counts()
        return chat_frequency

    def analyze_chat_length(self):
        self.data['message_length'] = self.data['message'].apply(len)
        chat_length = self.data.groupby('user')['message_length'].mean()
        return chat_length

    def visualize_chat_frequency(self):
        chat_frequency = self.analyze_chat_frequency()
        plt.figure(figsize=(10,6))
        sns.barplot(chat_frequency.index, chat_frequency.values, alpha=0.8)
        plt.title('Chat Frequency')
        plt.ylabel('Number of Chats', fontsize=12)
        plt.xlabel('User', fontsize=12)
        plt.show()

    def visualize_chat_length(self):
        chat_length = self.analyze_chat_length()
        plt.figure(figsize=(10,6))
        sns.barplot(chat_length.index, chat_length.values, alpha=0.8)
        plt.title('Average Chat Length')
        plt.ylabel('Average Length', fontsize=12)
        plt.xlabel('User', fontsize=12)
        plt.show()
```