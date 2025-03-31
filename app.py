import streamlit as st
import requests
import json

# Set up API key
API_KEY = "AIzaSyA1nkzJxllp9rZVLbwwOIwA71cli9n9hmI"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

# Streamlit UI
st.title("Gemini 2.0 Flash Chatbot")
st.write("Ask me anything!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input("Type your message...")
if user_input:
    # Append user input to chat history
    st.session_state["messages"].append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.write(user_input)

    # Prepare API request
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {
                "parts": [{"text": user_input}]
            }
        ]
    }

    # Call Gemini API
    response = requests.post(API_URL, headers=headers, json=data)
    response_data = response.json()

    # Extract response text
    bot_response = response_data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "Sorry, I couldn't generate a response.")

    with st.chat_message("assistant"):
        st.write(bot_response)

    # Append bot response to chat history
    st.session_state["messages"].append({"role": "assistant", "content": bot_response})
