from colorama import *
init(autoreset=True)
def start_menu():
    x = input(f"""{Style.BRIGHT}{Fore.LIGHTCYAN_EX}Available topics:
        {Fore.YELLOW}Food - f
        {Fore.LIGHTBLUE_EX}Geography - g
        {Fore.LIGHTBLACK_EX}Cars - c
        {Fore.LIGHTGREEN_EX}Animals - a
        {Fore.MAGENTA}Clothes - cl
        {Fore.LIGHTRED_EX}Random - r
        {Fore.RESET}{Style.BRIGHT}{Fore.LIGHTCYAN_EX}Choose topic{Fore.YELLOW}(f,{Fore.LIGHTBLUE_EX}g,{Fore.LIGHTBLACK_EX}c,{Fore.LIGHTGREEN_EX}a,{Fore.MAGENTA}cl,{Fore.LIGHTRED_EX}r):{Style.BRIGHT}{Fore.LIGHTCYAN_EX} """).lower()
    return x