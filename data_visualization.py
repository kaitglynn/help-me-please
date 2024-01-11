```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class DataVisualization:
    def __init__(self, data):
        self.data = data

    def plot_chat_frequency(self):
        chat_data = pd.DataFrame(self.data)
        chat_data['date'] = pd.to_datetime(chat_data['date'])
        chat_data.set_index('date', inplace=True)
        chat_data.resample('D').sum().plot()
        plt.title('Chat Frequency')
        plt.xlabel('Date')
        plt.ylabel('Number of Messages')
        plt.show()

    def plot_sentiment_over_time(self, sentiment_data):
        sentiment_df = pd.DataFrame(sentiment_data)
        sentiment_df['date'] = pd.to_datetime(sentiment_df['date'])
        sentiment_df.set_index('date', inplace=True)
        sentiment_df.resample('D').mean().plot()
        plt.title('Sentiment Over Time')
        plt.xlabel('Date')
        plt.ylabel('Sentiment Score')
        plt.show()

    def plot_word_frequency(self, word_data):
        word_df = pd.DataFrame(word_data)
        word_df.plot(kind='bar')
        plt.title('Word Frequency')
        plt.xlabel('Words')
        plt.ylabel('Frequency')
        plt.show()

    def plot_user_activity(self, activity_data):
        activity_df = pd.DataFrame(activity_data)
        activity_df.plot(kind='line')
        plt.title('User Activity Over Time')
        plt.xlabel('Time')
        plt.ylabel('Activity Level')
        plt.show()
```