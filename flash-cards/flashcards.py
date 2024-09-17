# imports
import json


#functions
def read_data(file, type):
    with open(file, type) as f:
        data = json.load(f)
        return data
    
def response1(score, total):
    return f"Correct! Current score: {score}/{total}"
def response2(score, total):
    return f"Current score: {score}/{total}"
def check_score(score):
    if score == 5:
        print('Perfect')
    elif score >=3:
        print('almost')
    else:
        print('needs improvement')

def display_questions(dictionary):
    score = 0
    total = len(dictionary)
    for i in dictionary:
        guess = input(i["q"] + " > ")

        if guess.lower() == i["a"].lower():
            # increment score up one
            score += 1
            # interpolate score and total into the response
            print(response1(score, total))
        else:
            print("Incorrect! The correct answer was", i["a"])
            print(response2(score, total))
    check_score(score)

dictionary = read_data('./flash-cards/me-capitals.json', 'r')['cards']
display_questions(dictionary)