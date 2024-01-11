```python
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def summarize_web_page(url):
    # Fetching the content from the URL
    fetched_data = requests.get(url)
    article_content = fetched_data.text

    # Parsing the URL content and storing in a variable
    soup = BeautifulSoup(article_content, 'html.parser')

    # Returning <p> tags
    paragraphs = soup.find_all('p')

    article_content = ""

    # Looping through the paragraphs and adding them to the variable
    for p in paragraphs:  
        article_content += p.text

    # Removing Square Brackets and Extra Spaces
    article_content = re.sub(r'\[[0-9]*\]', ' ', article_content)
    article_content = re.sub(r'\s+', ' ', article_content)

    # Removing special characters and digits
    formatted_article_content = re.sub('[^a-zA-Z]', ' ', article_content )
    formatted_article_content = re.sub(r'\s+', ' ', formatted_article_content)

    # Converting Text To Sentences
    sentence_list = sent_tokenize(article_content)

    # Find Weighted Frequency of Occurrence
    stopwords = set(stopwords.words('english'))
    word_frequencies = {}
    for word in word_tokenize(formatted_article_content):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    maximum_frequency = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequency)

    # Calculating Sentence Scores
    sentence_scores = {}
    for sent in sentence_list:
        for word in word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    # Getting the Summary
    import heapq
    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)
    return summary
```