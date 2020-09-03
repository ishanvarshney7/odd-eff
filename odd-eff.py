import random


def batting():
    print("\n\nIt's your batting now")
    player_runs=0
    while(True):
        n=random.randint(1,6)
        print("Enter a Number ", end='')
        num=int(input())
        if num>6 or num<0:
            print("Invalid number\n")
            continue

        print("Number given by Computer is",n)
        if n==num:
            print("\n\n\nYou are out!!!")
            print(f'Your total score is {player_runs}')
            break
        player_runs+=num
        print(f'Your total run till now {player_runs}\n')
    return player_runs


def bowling():
    print("\n\nIt's your bowling now")
    computer_runs=0
    while(True):
        n=random.randint(1,6)
        print("Enter a Number ",end='')
        num=int(input())
        if num>6 or num<0:
            print("Invalid number\n")
            continue

        print("Number given by Computer is",n)
        if n==num:
            print("\n\n\nIt's a wicket")
            print(f"computer's total score is {computer_runs}")
            break
        computer_runs+=n
        print(f'Computer total runs till now {computer_runs}\n')    
    return computer_runs

def main_page():

    print("\nSelect from the given options")
    print("1 for Batting")
    print("2 for Bowling")

    print("\nYour choice ",end='')
    n=int(input())
    if n==1:
        player_runs=batting()
        computer_runs=bowling()
    
    if n==2:
        computer_runs=bowling()
        player_runs=batting()
    if n!=1 or n!=2:
        print("Invalid input!!!")
        main_page() 
    
    if player_runs>computer_runs:
        print(f'\n\nYou Win by {player_runs-computer_runs} runs :)')
    elif player_runs<computer_runs:
        print(f'\n\nYou Lose by {computer_runs-player_runs} runs :(')
    else:
        print("Game draw :|")

def main_page1():

    print("\nSelect from the given options")
    print("1 for Batting")
    print("2 for Bowling")
    print("3 for Help")

    print("\nYour choice ",end='')
    n=int(input())

    if n==3:
        help()
    else:
        
        if n==1:
           player_runs=batting()
           computer_runs=bowling()
    
        elif n==2:
          computer_runs=bowling()
          player_runs=batting()
        
        else:
            print("Invalid input")
            main_page1()

    
    
        if player_runs>computer_runs:
            print(f'\n\nYou Win by {player_runs-computer_runs} runs :)')
        elif player_runs<computer_runs:
            print(f'\n\nYou Lose by {computer_runs-player_runs} runs :(')
        else:
            print("Game draw :|")


def help():
    print("                                                 HELP")
    print("\n\n\n                                               Instructions \n\n")
    print("You have to opt a number from 1 to 6 (inluding both of them), similarly the computer will chose a number randomly.")
    print("You have to do batting and bowling accordingly to your choice and your scores will be recored on each turn then the \nplayer with most runs at the end will win the game")


    print("\n\n     For Batting")
    print("\nIf the number chosen by both are same then you are out else the number selected by you is added to your total score.")

    print("\n\n     For Bowling")
    print("\nIf the number chosen by both are same then the computer is out else the number selected by the computer is added to \ncomputer's total score.")

    print("\n\n\nPress any key to exit")
    hold=input()
    main_page()

main_page1()
