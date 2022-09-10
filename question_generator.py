import json
from os import system, name
from random import choice
from tqdm import tqdm
from rich.console import Console
from rich.table import Table

console = Console()

pass_file_names = {
    "1": "./questions/eng_econs_1.json",
    "2": "./questions/dsp_end_of_sem.json",
    "3": "./questions/eng_econs_2015.json",
    "4": "./questions/management_1.json",
    "5": "./questions/management_2005.json",
}

set_names: dict[int, str] = {
    1: "Engineering Econs 1",
    2: "Digital Signal Processing",
    3: "Entrepreneurship 2015",
    4: "Management 1",
    5: "Management 2 - 2005",
}


def print_table(data1, data2, data3, data4, data5):
    table = Table(title="Sets of Questions")

    table.add_column("Set Number", style="blue bold")
    table.add_column("Set Name", style="magenta bold")
    table.add_column("Total Number of Questions", style="bold")

    table.add_row("1", "Engineering Econs 1", str(number_of_questions(data1)))
    table.add_row(
        "2", "Digital Signal Processing ( End of Sem )", str(number_of_questions(data2))
    )
    table.add_row("3", "Entrepreneurship 2015", str(number_of_questions(data3)))
    table.add_row("4", "Management 1", str(number_of_questions(data4)))
    table.add_row("5", "Management 2 - 2005", str(number_of_questions(data5)))

    console.print(table)


def print_recent_runs(recent_runs):
    table = Table(title="History of Recent Runs")

    table.add_column("Set Number", style="blue bold")
    table.add_column("Set Name", style="magenta bold")
    table.add_column("Start Number", style="green bold")
    table.add_column("Stop Number", style="red bold")
    table.add_column("Score", style="bold")
    table.add_column("Skipped", style="bold")
    table.add_column("Undone", style="bold")

    for _, value in recent_runs.items():
        table.add_row(
            str(value["Set Number"]),
            str(set_names[int(value["Set Number"])]),
            str(value["Start Number"]),
            str(value["Stop Number"]),
            str(value["Score"]),
            str(value["Skipped"]),
            str(value["Undone"]),
        )

    console.print(table)


def clear_screen():
    system("cls" if name == "nt" else "clear")


if __name__ == "__main__":
    clear_screen()

    with open(file=pass_file_names["1"], mode="r", encoding="utf-8") as file1, open(
        file=pass_file_names["2"], mode="r", encoding="utf-8",
    ) as file2, open(file=pass_file_names["3"], mode="r", encoding="utf-8") as file3, open(
        file=pass_file_names["4"], mode="r", encoding="utf-8"
    ) as file4, open(
        file=pass_file_names["5"], mode="r", encoding="utf-8"
    ) as file5:
        data1 = json.load(file1)
        data2 = json.load(file2)
        data3 = json.load(file3)
        data4 = json.load(file4)
        data5 = json.load(file5)

    def number_of_questions(data):
        return len(data["questions"].items())

    loops = int(
        console.input(
            "[bold yellow]How many times do you want to run through the program? eg: 2: [/bold yellow]"
        )
    )
    runs = 0
    # Recent runs: Hold the history of the previous runs
    recent_runs = {}

    while runs < loops:
        console.print(
            f"\n[bold]Number of Runs Through Program : {runs + 1} out {loops}[/bold].\n"
        )

        if recent_runs:
            print_recent_runs(recent_runs)

        console.print("\n[bold yellow]Select your set of questions.[/bold yellow]")
        print_table(data1, data2, data3, data4, data5)

        try:
            passco_number = console.input("[bold blue]Your Choice, eg, 3: [/bold blue]")
        except KeyboardInterrupt as e:
            console.print("\n[bold red]Session Terminated by User !!![bold red]")
            break
        else:
            try:
                with open(pass_file_names[passco_number], "r") as file:
                    data = json.load(file)
            except KeyError as e:
                console.print("[bold red]Invalid Choice, Try Again.[/bold red]")
            else:
                start = int(console.input("[bold green]Start Number:[/bold green] "))
                stop = int(console.input("[bold red]Stop Number:[/bold red] "))

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
                skipped = 0

                clear_screen()

                try:
                    for i in tqdm(
                        range(len(possible_answers)), desc="Percentage Complete"
                    ):
                        random_question_number = choice(list(questions.keys()))
                        print(f"\n-----Question {random_question_number}-----")
                        console.print(
                            f"[bold yellow]{questions[random_question_number]}[/bold yellow]"
                        )
                        input()
                        print(possible_answers[random_question_number])

                        user_answer = str(
                            console.input("\n[bold]Your answer, eg, b: [/bold]")
                        )
                        console.print(
                            f"\n[bold]Suggested Answer:[/bold] [green bold]{answer[random_question_number]}[/green bold]"
                        )
                        input()

                        try:
                            answer_alphabet = answer[random_question_number][0]
                        except IndexError as e:
                            console.print(f"[bold red]{e}[/bold red]")
                        else:
                            if user_answer == answer_alphabet:
                                correct_answers += 1
                            elif user_answer == "":
                                skipped += 1

                        del questions[random_question_number]
                        clear_screen()

                except KeyboardInterrupt:
                    print("Closed session")
                else:
                    print("Completed session successfully")
                finally:
                    clear_screen()

                recent_runs[runs] = {
                    "Set Number": passco_number,
                    "Start Number": start,
                    "Stop Number": stop,
                    "Score": f"{correct_answers} / {len(possible_answers)}",
                    "Skipped": f"{skipped} / {len(possible_answers)}",
                    "Undone": f"{len(possible_answers) - (correct_answers + skipped)}/{len(possible_answers)}",
                }

                runs += 1

    print_recent_runs(recent_runs)
