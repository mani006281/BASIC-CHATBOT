# A simple rule-based chatbot using if-elif-else

def chatbot():
    print("🤖 Chatbot: Hello! I'm your simple chatbot. Type something or type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("🤖 Chatbot: Hi!")
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("🤖 Chatbot: Sorry, I didn't understand that.")

# Run the chatbot
chatbot()
