# a dictionary that stores questions and answers
# have a variable that tracks the scor of the player
# loop through the dictionary using the key values pairs
#display each question to the user and allow them to answer
#tell them if they are right or wrong
#show the final resut when quiz is completed

quiz = {
    "question1": {
        "question": "what is the capital of france?",
        "answer": "paris"
    },
    "question2": {
        "question": "what is the capitol of India",
        "answer": "new delhi"
    },
    "question3": {
        "question": "what is the capitol of China",
        "answer": "bejing"
    },
    "question4": {
        "question": "what is the capitol of USA",
        "answer": "washington D.C"
    },
    "question5": {
        "question": "what is the capitol of italy",
        "answer": "rome"
    },
    "question6": {
        "question": "what is the capitol of portugal",
        "answer": "lisbon"
    },
    "question7": {
        "question": "what is the capitol of austria",
        "answer": "vienna"
    },
    "question8": {
        "question": " what is the capitol of spain",
        "answer": "madrid"
    },
    "question9": {
        "question": " what is the question of germany",
        "answer": "berlin"
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("answer: ")

    if answer.lower() == value["answer"].lower():
        print('correct')
        score = score + 2
        print("your score is: " + str(score))

    else:
        print("wrong!")
        print("the answer is : " + value['answer'])
        print("your score is: " + str(score))