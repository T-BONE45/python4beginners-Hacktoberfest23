import random

def basic_ai_response(user_input):
    greetings = ["hello", "hi", "hey", "howdy"]
    responses = ["Hello!", "Hi there!", "Hey!", "How can I assist you today?"]

    user_input = user_input.lower()

    for greeting in greetings:
        if greeting in user_input:
            return random.choice(responses)

    return "I'm sorry, I don't understand that."

def main():
    print("Basic AI: Hello, how can I assist you today?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Basic AI: Goodbye!")
            break

        response = basic_ai_response(user_input)
        print("Basic AI:", response)

if __name__ == "__main__":
    main()
