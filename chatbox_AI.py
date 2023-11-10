import random

responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm just a bot, but I'm doing well. How can I help you?", "I'm fine, thanks. What can I do for you?"],
    "goodbye": ["Goodbye!", "See you later!", "Have a great day!"],
    "default": ["I'm not sure what you mean. Can you please rephrase your question?", "I don't understand. Could you ask another way?"]
}

def get_response(user_input):
    user_input = user_input.lower()  

    for key, value in responses.items():
        if key in user_input:
            return random.choice(value)

    return random.choice(responses["default"])

print("Chatbot: Hi, I'm your chatbot. How can I assist you today?")
while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    
    response = get_response(user_input)
    print("Chatbot:", response)
