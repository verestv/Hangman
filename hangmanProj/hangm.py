import random
import os
from colorama import *
from plus import pictures
from play_loop import play_ask
from topic import choose_topic
from StartMenu import start_menu

init(autoreset=True)

def main():
    try:
        x = start_menu()
        chosen_w = random.choice(choose_topic(x))
    except:
        print(f'{Fore.RED}Invalid Input')
        main()
    display =[]
    attemts = 6
    count = 0
    used_letters = []
    word = []
    for letter in chosen_w:
        display.append('_')
    
    print(f'{Fore.LIGHTYELLOW_EX}This word contains this amount of letters: \n {display}')
    while len(word) != len(display) or attemts > 0:
        guess =  input(Fore.LIGHTCYAN_EX +"Enter a letter: ").lower()
        guess = guess.strip()
        
        if guess in used_letters:
            print(f'{Fore.LIGHTRED_EX} {Style.BRIGHT}You have already tried this letter')
        elif guess in chosen_w:
            used_letters.append(guess)

            for i,q in enumerate(chosen_w):
                if q == guess:
                    display = display[:i] + list(guess) + display[i+1:]
                    word.append('guess')
            
            print(f'{Fore.LIGHTYELLOW_EX}  {display}')
        else :
            attemts-=1
            count +=1
            pictures(count)
            used_letters.append(guess)
            print(f'{Fore.LIGHTYELLOW_EX}  {display}')
        if len(word) == len(display):
            print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Congrats you guessed the word!")
            break
        if attemts == 0:
            print(Fore.LIGHTCYAN_EX + f'You lost(\nThe word was {Style.BRIGHT}{chosen_w}')
            break
    play_ask()
    os.system('cls')
    main()
        
if __name__ == '__main__':

    main()






