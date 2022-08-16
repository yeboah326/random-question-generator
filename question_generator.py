import json
from os import system
from random import choice
from tqdm import tqdm


pass_file_names = {"1": "./questions/eng_econs_1.json"}

if __name__ == "__main__":
    system("cls|clear")

    print("Select a set of questions to go through: \n1. Engineering Econs 1")
    passco_number = input("Choice: ")

    with open(pass_file_names[passco_number], "r") as file:
        data = json.load(file)

    questions = data["questions"]
    possible_answers = data["possible_answers"]
    answer = data["answers"]

    system("cls|clear")

    try:
        for i in tqdm(range(len(possible_answers)), desc="Percentage Complete"):
            random_question_number = choice(list(questions.keys()))
            print(f"\n-----Question {random_question_number}-----")
            print(questions[random_question_number])
            input()
            print(possible_answers[random_question_number])
            input()
            print(f"Answer: {answer[random_question_number]}")
            input()

            del questions[random_question_number]
            system("cls|clear")
    except KeyboardInterrupt:
        print("Closed session")
    else:
        print("Completed session successfully")
    finally:
        system("cls|clear")
