# 🤖 FAQ Chatbot

An intelligent FAQ chatbot built using **Python, Natural Language Processing (NLP), TF-IDF, and Cosine Similarity**.

The chatbot understands user questions and finds the most relevant answer from a predefined FAQ dataset. It also provides a fallback response when no sufficiently relevant answer is found.

---

## 📌 Project Overview

This project was developed as part of the **CodeAlpha Artificial Intelligence Internship**.

The chatbot is designed for an online shopping service and can answer frequently asked questions related to:

- Orders
- Order tracking
- Delivery
- Payments
- Cash on Delivery
- Returns
- Refunds
- Address changes
- Damaged products
- Discounts
- Coupon codes
- Customer support

---

## ✨ Features

- 💬 Interactive chatbot interface
- 🧠 Natural Language Processing (NLP)
- 🔤 Text normalization
- ✂️ Tokenization
- 🚫 Stop-word removal
- 📊 TF-IDF vectorization
- 🔍 Cosine similarity matching
- 🎯 Similarity threshold for relevant answers
- ❌ Fallback response for unknown questions
- 🗑️ Clear chat functionality
- 📚 Example questions in the sidebar
- 🆓 Completely free to run
- 🔐 No paid APIs or external AI services required

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| NLTK | Natural Language Processing |
| Scikit-learn | TF-IDF and cosine similarity |
| Streamlit | Chatbot web interface |

---

## 🧠 Methodology

The chatbot follows these steps:

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
```


## 📂 Project Structure

FAQ-Chatbot/
│
├── app.py              # Streamlit chatbot interface
├── chatbot.py          # NLP preprocessing and similarity matching
├── faq_data.py         # FAQ questions and answers
├── requirements.txt    # Required Python packages
├── README.md           # Project documentation
│
├── .venv/              # Local virtual environment
└── __pycache__/        # Python cache files


## 💰 Cost

This project is completely free to run.

It does not require:

OpenAI API
Gemini API
Paid cloud services
Paid databases
API keys

All NLP processing is performed locally using Python libraries.



## 🚀 Future Improvements

Possible future enhancements include:

Adding more FAQ categories
Using semantic embeddings
Adding multilingual support
Adding voice input
Adding chatbot analytics
Connecting the chatbot to a real product database
Improving intent detection
Adding an administrator interface for managing FAQs



## 👨‍💻 Author

SATYA PRIYA

Developed as part of the CodeAlpha Artificial Intelligence Internship.