import streamlit as st
from chatbot import get_answer


# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="FAQ Chatbot",
    page_icon="🤖",
    layout="centered"
)


# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #666666;
    font-size: 17px;
    margin-bottom: 25px;
}

.info-box {
    padding: 15px;
    border-radius: 10px;
    background-color: #f0f4ff;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.markdown(
    '<div class="main-title">🤖 FAQ Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your AI-powered online shopping assistant</div>',
    unsafe_allow_html=True
)


st.markdown("""
<div class="info-box">
💡 Ask questions about orders, delivery, payments, returns, refunds and more.
</div>
""", unsafe_allow_html=True)


# ---------------- CHAT HISTORY ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.header("About the Chatbot")

    st.write(
        "This chatbot uses Natural Language Processing "
        "(NLP), TF-IDF and cosine similarity to find "
        "the most relevant FAQ answer."
    )

    st.divider()

    st.subheader("Example Questions")

    st.write("• How can I track my order?")
    st.write("• Do you accept UPI?")
    st.write("• How long does delivery take?")
    st.write("• Can I return a product?")
    st.write("• How can I get a refund?")

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# ---------------- DISPLAY CHAT HISTORY ----------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# ---------------- USER INPUT ----------------

user_question = st.chat_input(
    "Ask your question..."
)


# ---------------- CHATBOT RESPONSE ----------------

if user_question:

    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    with st.chat_message("user"):
        st.write(user_question)


    # Generate response
    answer = get_answer(user_question)


    # Add chatbot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant"):
        st.write(answer)