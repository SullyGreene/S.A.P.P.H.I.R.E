# Helper functions
# utils/helpers.py - Helper functions

import re
import webbrowser

def clean_text(text):
    """
    Cleans the input text by removing special characters and extra spaces, making it easier to process.
    
    Parameters:
        text (str): The text to clean.
    
    Returns:
        str: The cleaned text.
    """
    # Remove special characters and digits
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Remove extra spaces
    cleaned_text = " ".join(cleaned_text.split())
    
    return cleaned_text

def extract_keywords(text, num_keywords=5):
    """
    Extracts a specified number of keywords from a text using a simple frequency analysis.
    
    Parameters:
        text (str): The text from which to extract keywords.
        num_keywords (int): The number of keywords to extract.
        
    Returns:
        list: A list of the most frequent non-trivial words in the text.
    """
    # Tokenize the text into words
    words = text.lower().split()
    
    # Count the frequency of each word
    word_freq = {}
    for word in words:
        if word not in word_freq:
            word_freq[word] = 0
        word_freq[word] += 1
    
    # Sort words by frequency
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    
    # Filter out common stopwords (This list can be expanded or dynamically generated)
    stopwords = set(["the", "and", "is", "in", "to", "of"])
    keywords = [word for word, freq in sorted_words if word not in stopwords][:num_keywords]
    
    return keywords

def open_website(url):
    """
    Opens a website in the default browser.
    
    Parameters:
        url (str): The URL of the website to open.
    """
    try:
        webbrowser.open(url, new=2)  # `new=2` option opens in a new tab, if possible
        return f"Opening {url}"
    except Exception as e:
        return f"Failed to open {url}: {str(e)}"


# If you want to test the helper functions directly, you can uncomment the following lines:
# if __name__ == "__main__":
#     sample_text = "Python is an amazing programming language! It's versatile, easy to learn and has a wide range of applications."
#     print("Original text:", sample_text)
#     print("Cleaned text:", clean_text(sample_text))
#     print("Extracted keywords:", extract_keywords(clean_text(sample_text)))
