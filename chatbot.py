import random

def simple_chatbot(user_input):
    greetings = ["hello", "hi", "hey", "greetings", "howdy"]
    farewells = ["bye", "goodbye", "see you", "farewell"]

    # Convert user input to lowercase for case-insensitive matching
    user_input_lower = user_input.lower()

    # Check for greetings
    if any(word in user_input_lower for word in greetings):
        return "Hello! How can I help you today?"

    # Check for farewells
    elif any(word in user_input_lower for word in farewells):
        return "Goodbye! Have a great day."

    # Default response if no keyword is matched
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Simple chat loop
while True:
    user_input = input("You: ")

    # Break the loop if the user types 'exit'
    if user_input.lower() == 'exit':
        break

    # Get the chatbot's response
    response = simple_chatbot(user_input)
    
    print(f"Bot: {response}")
