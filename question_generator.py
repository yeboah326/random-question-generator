import json
from os import system, name
from random import choice
from tqdm import tqdm

pass_file_names = {
    "1": "./questions/eng_econs_1.json",
    "2": "./questions/dsp_end_of_sem.json",
    "3": "./questions/eng_econs_2015.json",
    "4": "./questions/management_1.json",
    "5": "./questions/management_2005.json",
}


def clear_screen():
    system("cls" if name == "nt" else "clear")


if __name__ == "__main__":
    clear_screen()

    print("Select a set of questions")

    with open(pass_file_names["1"], "r") as file1, open(
        pass_file_names["2"], "r"
    ) as file2, open(pass_file_names["3"], "r") as file3, open(
        pass_file_names["4"], "r"
    ) as file4, open(
        pass_file_names["5"], "r"
    ) as file5:
        data1 = json.load(file1)
        data2 = json.load(file2)
        data3 = json.load(file3)
        data4 = json.load(file4)
        data5 = json.load(file5)

    def number_of_questions(data):
        return len(data["questions"].items())

    print(
        f"""
    1. Engineering Econs 1. \n\tNumber of Questions: {number_of_questions(data1)}
    2. Digital Signal Processing (End of Semester). \n\tNumber of Questions: {number_of_questions(data2)}
    3. Entrepreneurship 2015. \n\tNumber of Questions: {number_of_questions(data3)}
    4. Management 1. \n\tNumber of Questions: {number_of_questions(data4)}
    5. Management 2 - 2005. \n\tNumber of Questions: {number_of_questions(data5)}
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
