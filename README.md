# 🤖 FAQ Chatbot

An intelligent FAQ chatbot built using **Python, Natural Language Processing (NLP), TF-IDF, Cosine Similarity, and Streamlit**.

The chatbot accepts questions from users, compares them with a predefined FAQ dataset, and returns the most relevant answer.

---

## 📌 Project Overview

This project was developed as part of the **CodeAlpha Artificial Intelligence Internship**.

The chatbot is designed for an online shopping service and answers frequently asked questions about orders, delivery, payments, returns, refunds, and customer support.

---

## ✨ Features

- 💬 Interactive chatbot interface
- 🧠 Natural Language Processing (NLP)
- 🔤 Text normalization
- ✂️ Tokenization
- 🚫 Stop-word removal
- 📊 TF-IDF vectorization
- 🔍 Cosine similarity matching
- 🎯 Similarity threshold
- ❌ Fallback response for unknown questions
- 🗑️ Clear chat functionality
- 📚 Example questions
- 🆓 Completely free to run
- 🔐 No paid APIs required

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main programming language |
| NLTK | NLP preprocessing |
| Scikit-learn | TF-IDF and cosine similarity |
| Streamlit | Web-based chatbot interface |

---

## 🧠 How It Works

The chatbot follows this workflow:

```text
User Question
      ↓
Text Normalization
      ↓
Tokenization
      ↓
Stop-word Removal
      ↓
TF-IDF Vectorization
      ↓
Cosine Similarity
      ↓
Find Best Matching FAQ
      ↓
Similarity Threshold Check
      ↓
Chatbot Response