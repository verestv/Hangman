from colorama import *
init(autoreset=True)
def play_ask():
    global play_game
    play_game = input(f"{Fore.CYAN}Do You want to play again?{Fore.LIGHTGREEN_EX} y = yes{Fore.LIGHTCYAN_EX},{Fore.LIGHTRED_EX} n = no {Fore.LIGHTCYAN_EX}\n")
    while play_game not in ["y", "n"]:
        play_game = input(f"{Fore.CYAN}Do You want to play again?{Fore.LIGHTGREEN_EX} y = yes{Fore.LIGHTCYAN_EX},{Fore.LIGHTRED_EX} n = no {Fore.LIGHTCYAN_EX}\n")
    if play_game == "y":
        return 
    elif play_game == "n":
        print(f"{Fore.BLUE}{Style.BRIGHT}Thanks For Playing! We expect you back again!")
        exit()
