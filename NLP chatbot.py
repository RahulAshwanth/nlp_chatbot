#!/usr/bin/env python
# coding: utf-8

# In[11]:


#import nltk
from nltk.tokenize import word_tokenize
import random
import nltk



# Sample data
GREETINGS = ["hello", "hi", "greetings", "sup", "what's up"]
GREETINGS_RESPONSES = ["hi", "hey!", "*nods*", "hi there", "hello!", "I am glad you're talking to me"]

# Basic conversation pairs (can be extended)
CONVERSATION = {
    "how are you?": ["I am good, thank you!", "I am doing great!", "All good here!"],
    "what's your name?": ["I am a chatbot created by you!", "You can call me Chatbot."],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
}

# Function to check for greetings
def check_greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETINGS:
            return random.choice(GREETINGS_RESPONSES)
    return None

# Function to generate response
def respond(sentence):
    sentence = sentence.lower()
    if sentence in CONVERSATION:
        return random.choice(CONVERSATION[sentence])
    
    for key in CONVERSATION:
        if any(word in sentence for word in key.split()):
            return random.choice(CONVERSATION[key])
    return "I'm sorry! I don't understand."

# Main function to run the chatbot
def chatbot():
    print("Chatbot: Hi! How can I help you? (type 'bye' to exit)")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'bye':
            print("Chatbot: Goodbye! Have a nice day!")
            break
        greeting = check_greeting(user_input)
        if greeting:
            print(f"Chatbot: {greeting}")
        else:
            print(f"Chatbot: {respond(user_input)}")

if __name__ == "__main__":
    chatbot()


# In[ ]:




