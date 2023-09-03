import re
#pre-defined rules
rules=[
    (r"hello|hi", "Hello! How can I help you?"),
    (r"who are you?", "I am Alex, your virtual assistant. What can I do for you today?"),
    (r"what is a chatbot?", " A chatbot is a computer program that simulates and processes human conversation either written or spoken, allowing humans to interact with digital devices as if they were communicating with a real person."),
    (r"how are you?", "I am doing well, thank you for asking"),
    (r"bye", "Goodbye! Have a great day!")

]
#ai's responses
def alex_response(user_input):
    user_input=user_input.lower()
    for rule, response in rules :
        if re.search(rule, user_input):
            return response
        
    return "I am sorry, I don't think I understand that."
    
while True:
    user_input=input("You:")
    if user_input.lower()=="exit":
        print("Goodbye!")
        break
    elif user_input.lower()=="bye":
        response= alex_response(user_input)
        print("Alex:",response)
        break
    else:
        response= alex_response(user_input)
        print("Alex:",response)
