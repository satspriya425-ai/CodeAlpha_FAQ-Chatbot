# FAQ Chatbot - NLP and Similarity Matching

import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from faq_data import faqs


# Download required NLTK resources
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)


def preprocess_text(text):
    """Clean and normalize text using basic NLP techniques."""

    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation and special characters
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    # Tokenize the text
    tokens = word_tokenize(text)

    # Load English stop words
    stop_words = set(stopwords.words("english"))

    # Remove stop words
    filtered_tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    return " ".join(filtered_tokens)


# Preprocess all FAQ questions
faq_questions = [
    preprocess_text(faq["question"])
    for faq in faqs
]


# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Convert FAQ questions into TF-IDF vectors
faq_vectors = vectorizer.fit_transform(faq_questions)


def get_answer(user_question, threshold=0.25):
    """
    Find the most relevant FAQ answer.

    Returns the answer if similarity is above the threshold.
    Otherwise, returns a fallback response.
    """

    # Preprocess user's question
    cleaned_question = preprocess_text(user_question)

    # Convert user question into a TF-IDF vector
    user_vector = vectorizer.transform([cleaned_question])

    # Calculate cosine similarity
    similarities = cosine_similarity(user_vector, faq_vectors)[0]

    # Find the FAQ with the highest similarity
    best_match_index = similarities.argmax()
    best_score = similarities[best_match_index]

    # Check whether the match is good enough
    if best_score >= threshold:
        return faqs[best_match_index]["answer"]

    return "Sorry, I couldn't find a relevant answer."