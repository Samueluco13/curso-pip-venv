import random

options = ["Rock", "Paper", "Cissors"]

def computer_choice():
    return random.choice(options)

def menu():
    print("Welcome to Rock, Paper, Cissors Game")
    return int(input("Elige el numero de tu opcion:\n1. Rock\n2. Paper\n3. Cissors\n---------------------------"))

def user_choice():
    choice = menu()
    return options[choice - 1]


def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Empate"

    if user_choice == "Rock":
        match computer_choice:
            case "Cissors":
                return "Usuario gana"
            case "Paper":
                return "Computador gana"

    if user_choice == "Paper":
        match computer_choice:
            case "Cissors":
                return "Computador gana"
            case "Rock":
                return "Usuario gana"

    if user_choice == "Cissors":
        match computer_choice:
            case "Rock":
                return "Computador gana"
            case "Paper":
                return "Usuario gana"

