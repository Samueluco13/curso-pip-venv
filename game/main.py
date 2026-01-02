import random

options = ["Rock", "Paper", "Cissors"]

def computer_choice():
    return random.choice(options)

def menu():
    print("Welcome to Rock, Paper, Cissors Game")
    return int(input("Elige el numero de tu opcion:\n1. Rock\n2. Paper\n3. Cissors\n"))

def user_choice():
    choice = menu()
    return options[choice - 1]

def winner():
    user = user_choice()
    computer = computer_choice()
    if user == computer:
        return print("Empate")

    if user == "Rock":
        match computer:
            case "Cissors":
                return print("Usuario gana")
            case "Paper":
                return print("Computador gana")

    if user == "Paper":
        match computer:
            case "Cissors":
                return print("Computador gana")
            case "Rock":
                return print("Usuario gana")

    if user == "Cissors":
        match computer:
            case "Rock":
                return print("Computador gana")
            case "Paper":
                return print("Usuario gana")
winner()