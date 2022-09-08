import json
from os import system, name
from random import choice
from tqdm import tqdm

pass_file_names = {
    "1": "./questions/eng_econs_1.json",
    "2": "./questions/dsp_end_of_sem.json",
    "3": "./questions/eng_econs_2015.json",
    "4": "./questions/management_1.json",
    "5": "./questions/management_2005.json"
}

def clear_screen():
    system("cls" if name == "nt" else "clear")

if __name__ == "__main__":
    clear_screen()

    print("Select a set of questions")
    print(
        """
    1. Engineering Econs 1
    2. Digital Signal Processing (End of Semester)
    3. Entrepreneurship 2015 (87)
    4. Management 1 (139)
    5. Management 2 - 2005 (80) 
        """
    )
    passco_number = input("Choice: ")

    with open(pass_file_names[passco_number], "r") as file:
        data = json.load(file)

    start = int(input("Start: "))
    stop = int(input("Stop: "))

    questions = {
        key: value
        for key, value in data["questions"].items()
        if start <= int(key) <= stop
    }  # [start:stop+1]
    possible_answers = {
        key: value
        for key, value in data["possible_answers"].items()
        if start <= int(key) <= stop
    }  # [start:stop+1]
    answer = {
        key: value
        for key, value in data["answers"].items()
        if start <= int(key) <= stop
    }  # [start:stop+1]

    correct_answers = 0

    clear_screen()

    try:
        for i in tqdm(range(len(possible_answers)), desc="Percentage Complete"):
            random_question_number = choice(list(questions.keys()))
            print(f"\n-----Question {random_question_number}-----")
            print(questions[random_question_number])
            input()
            print(possible_answers[random_question_number])
            input()
            print(f"Answer: {answer[random_question_number]}")
            answer_is_correct = input()
            if answer_is_correct == "":
                correct_answers += 1

            del questions[random_question_number]
            clear_screen()
    except KeyboardInterrupt:
        print("Closed session")
    else:
        print("Completed session successfully")
    finally:
        clear_screen()
        print(f"You scored {correct_answers}/{len(possible_answers)}")
