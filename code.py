import googlesearch

def chatbot():
    print("Hi, I'm a chatbot. How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input == "Goodbye" or user_input == "Bye":
            print("Chatbot: Goodbye! Have a great day.")
            break
        else:
            query = user_input + " site:wikipedia.org"
            for result in googlesearch.search(query, num=1, stop=1):
                response = result
            print("Chatbot: According to my search, " + response)

chatbot()
