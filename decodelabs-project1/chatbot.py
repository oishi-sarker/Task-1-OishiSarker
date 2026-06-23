# Rule-Based AI Chatbot
# DecodeLabs Project 1

responses = {
    "hello": "Hi there!",
    "how are you": "I am fine, thank you!",
    "what is your name": "My name is DecodeBot.",
    "who created you": "I was created by Oishi.",
    "good morning": "Good morning!",
    "good afternoon": "Good afternoon!",
    "good evening": "Good evening!",
    "good night": "Good night!",
    "thank you": "You're welcome!",
    "what can you do": "I can answer simple predefined questions."
}

print("===================================")
print("     RULE-BASED AI CHATBOT")
print("===================================")
print("Type 'bye' to exit the chatbot.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "bye":
        print("Bot: Goodbye! Have a great day!")
        break

    if user_input in responses:
        print("Bot:", responses[user_input])
    else:
        print("Bot: Sorry, I do not understand that.")