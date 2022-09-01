import json
from os import system
from random import choice
from statistics import correlation
from tqdm import tqdm
from itertools import islice

pass_file_names = {"1": "./questions/management_1.json"}

if __name__ == "__main__":
    system("cls|clear")

    print("Select a set of questions to go through: \n1. Management & Entrepreneurship")
    passco_number = input("Choice: ")

    with open(pass_file_names[passco_number], "r") as file:
        data = json.load(file)
    
    start = int(input("Start: "))
    stop = int(input("Stop: "))

    questions = {key:value for key, value in  data["questions"].items() if start <= int(key) <= stop}  #[start:stop+1]
    answer = {key:value for key, value in  data["answers"].items() if start <= int(key) <= stop} #[start:stop+1]

    correct_answers = 0

    system("cls|clear")

    try:
        for i in tqdm(range(len(questions)), desc="Percentage Complete"):
            random_question_number = choice(list(questions.keys()))
            print(f"\n-----Question {random_question_number}-----")
            print(questions[random_question_number])
            input()
            print(f"Answer: {answer[random_question_number]}")
            answer_is_correct = input()
            if answer_is_correct == "":
                correct_answers += 1

            del questions[random_question_number]
            system("cls|clear")
    except KeyboardInterrupt:
        print("Closed session")
    else:
        print("Completed session successfully")
    finally:
        system("cls|clear")
        print(f"You scored {correct_answers}/{len(answer)}")
