import random

# Magic 8-Ball
# A simple Python program that generates a random response to a question.

name = input("What is your name? ")
question = input("What is your question? ")

# Generate a random number between 1 and 15
random_number = random.randint(1, 15)

# Generate a response based on the random number
if random_number == 1:
    answer = "Yes definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
elif random_number == 10:
    answer = "I'm tired, so I'll say no... sorry... not sorry :)"
elif random_number == 11:
    answer = "What sort of question is that?"
elif random_number == 12:
    answer = "NEVER! NEVER! NEVER!"
elif random_number == 13:
    answer = "Hm... 8-Ball is confused"
elif random_number == 14:
    answer = "YES! YES! YES!"
elif random_number == 15:
    answer = "All we can say is omo"
else:
    answer = "Error"

# Handle cases where the user does not provide a name or question
if question == "" and name == "":
    print("Question:", question)
    print(
        "Magic 8-Ball Answer: Uhm... you didn't ask a question. "
        "How am I supposed to give you a response???"
    )

elif name == "":
    print("Question:", question)
    print("Magic 8-Ball Answer:", answer)

elif question == "":
    print(name, "asks:", question)
    print(
        "Magic 8-Ball Answer: Uhm... you didn't ask a question. "
        "How am I supposed to give you a response???"
    )

else:
    print(name, "asks:", question)
    print("Magic 8-Ball's Answer:", answer)
