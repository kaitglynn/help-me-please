```python
import random
from nltk import tokenize, FreqDist
from nltk.corpus import stopwords

class EducationalTools:
    def __init__(self):
        self.quiz_questions = []
        self.test_questions = []
        self.summarized_content = ""

    def generateQuiz(self, content, num_questions):
        sentences = tokenize.sent_tokenize(content)
        words = [word for sentence in sentences for word in tokenize.word_tokenize(sentence)]
        freq_dist = FreqDist(words)
        common_words = [word for word, freq in freq_dist.most_common(num_questions)]
        
        for word in common_words:
            self.quiz_questions.append({
                'question': f'What is the meaning of {word}?',
                'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
                'answer': 'Option 1'
            })
        return self.quiz_questions

    def generateTest(self, content, num_questions):
        sentences = tokenize.sent_tokenize(content)
        words = [word for sentence in sentences for word in tokenize.word_tokenize(sentence)]
        freq_dist = FreqDist(words)
        common_words = [word for word, freq in freq_dist.most_common(num_questions)]
        
        for word in common_words:
            self.test_questions.append({
                'question': f'What is the synonym of {word}?',
                'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
                'answer': 'Option 1'
            })
        return self.test_questions

    def summarizeContent(self, content):
        sentences = tokenize.sent_tokenize(content)
        stop_words = set(stopwords.words('english'))
        freq_table = dict()
        for sentence in sentences:
            words = tokenize.word_tokenize(sentence)
            for word in words:
                if word not in stop_words:
                    if word in freq_table:
                        freq_table[word] += 1
                    else:
                        freq_table[word] = 1
        sorted_freq_table = sorted(freq_table.items(), key=lambda item: item[1], reverse=True)
        self.summarized_content = ' '.join([word for word, freq in sorted_freq_table[:10]])
        return self.summarized_content
```