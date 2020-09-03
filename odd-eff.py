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


def help():
    print("HELP")
    


def main_page():
    #help()
    print("\nSelect from the given options")
    print("1 for batting")
    print("2 for bowling")

    print("\nYour choice ",end='')
    n=int(input())
    if n==1:
        player_runs=batting()
        computer_runs=bowling()
    
    if n==2:
        computer_runs=bowling()
        player_runs=batting()
    
    if player_runs>computer_runs:
        print(f'\n\nYou Win by {player_runs-computer_runs} runs :)')
    elif player_runs<computer_runs:
        print(f'\n\nYou Lose by {computer_runs-player_runs} runs :(')
    else:
        print("Game draw :|")


main_page()