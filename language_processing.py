```python
import nltk
from textblob import TextBlob
from googletrans import Translator

class LanguageProcessing:
    def __init__(self):
        self.translator = Translator()

    def tokenize(self, text):
        return nltk.word_tokenize(text)

    def sentiment_analysis(self, text):
        blob = TextBlob(text)
        return blob.sentiment

    def translate_text(self, text, target_language):
        return self.translator.translate(text, dest=target_language).text
```