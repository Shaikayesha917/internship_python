# Function to get bot's reply
def chatbot_reply(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi!"
    elif "how are you" in user_input:
        return "I am fine, thanks!"
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "I don't understand 😅"

# Main loop
def chat():
    print("Welcome to Simple Chatbot! (Type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        reply = chatbot_reply(user_input)
        print("Bot:", reply)
        if "bye" in user_input.lower():
            break

chat()