# NLP tasks like sentiment analysis, summarization
# services/natural_language_processing/nlp.py - NLP tasks
from textblob import TextBlob
import nltk
from nltk.tokenize import word_tokenize
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def analyze_sentiment(text):
    """
    Analyzes the sentiment of a given text and returns whether it's positive, neutral, or negative.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "positive"
    elif polarity == 0:
        return "neutral"
    else:
        return "negative"

def detect_language(text):
    """
    Detects the language of a given text.
    """
    blob = TextBlob(text)
    return blob.detect_language()

def summarize_text(text, n_sentences=3):
    """
    Summarizes the given text into a specified number of sentences.
    """
    blob = TextBlob(text)
    return ' '.join(blob.sentences[:n_sentences])

def extract_entities(text):
    """
    Extracts named entities (like people, places, organizations) from the given text.
    """
    for sent in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label'):
                print(chunk.label(), ' '.join(c[0] for c in chunk))


# If you want to test the sentiment analysis functionality directly, you can uncomment the following lines:
# if __name__ == "__main__":
#     sample_text = "I love coding in Python. It's so versatile and easy to use!"
#     print(f"Analyzing sentiment for: '{sample_text}'")
#     sentiment = analyze_sentiment(sample_text)
#     print(f"The sentiment is: {sentiment}")
