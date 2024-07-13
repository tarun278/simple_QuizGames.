def game_intro():
    print("Welcome to Quiz Trivia!")
    print("The questions will be multiple choice question answer type\nEach correct answer will worth 1 point")
    print("Lets, Begin the Game :)\n")

def alpha(n):
    return chr(ord('A')+n)


def check_answer(answer, n):
    answer_list = ["B", "C", "C", "C", "B", "D"]
    if (answer == answer_list[n]):
        print("Correct Answer ")
        return True
    else:
        print(f"Incorrect Answer, Correct Answer is option {answer_list[n]}")
        return False


def game():
    n = 0
    count = 0
    for question, options in questions.items():
        if n < len(questions):
            print(f"{question}?")
            for index, option in enumerate(options):
                alphabetical_index = alpha(index)
                print(f"{alphabetical_index}.{option}")
            answer = input("Enter Option: ")
            if (answer == "a" or answer == "b" or answer=="c" or answer == "d"):
                answer = answer.capitalize()
                chceker = check_answer(answer, n)
                if chceker:
                    count = count + 1
                else:
                    pass
                n = n + 1
            else:
                n= n+1
                print("Please Enter Valid option")
    print(f"Your score is {count}/{len(questions)}!")

questions = {
    "What is the color of sky":["Red","Blue","Green","Yellow"],
    "What is the capital city of Australia":["Sydney","Melbourne","Canberra","Brisbane"],
    "What is the chemical symbol for Gold":["Gd","Gu","Au","Ag"],
    "What is the tallest mountain in the world":["K2","Mount Abu","Mount Everest","Denalli"],
    "Which planet is known as the \"Red Planet\"":["Venus","Mars","Jupiter","Saturn"],
    "Who discovered electricity":["Issac Newton","Nikola Tesla","Michael Faraday","Benjamin Fraklin"]
}

if __name__ == '__main__':
    game_intro()
    game()














