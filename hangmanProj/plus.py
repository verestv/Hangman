from colorama import *
import time
init()
def pictures(count):
    time.sleep(0.2)
    if count == 1:
        print((Fore.LIGHTCYAN_EX + "       \n"
                                    "  |      \n"
                                    "  |      \n"
                                    "  |      \n"
                                    "  |      \n"
                                    "  |      \n"
                                    "  |      \n"
                                    "__|__\n"))
        print(Fore.LIGHTMAGENTA_EX + f'Wrong letter\nYou have {5} attemts')
    
    
    if count == 2:
        time.sleep(0.2)
        print((Fore.LIGHTCYAN_EX  +"   _____ \n"
                                   "  |      \n"
                                   "  |      \n"
                                   "  |      \n"
                                   "  |      \n"
                                   "  |      \n"
                                   "  |      \n"
                                   "__|__\n"))
        print(f'{Fore.LIGHTMAGENTA_EX}Wrong letter\nYou have {4} attemts')
    elif count == 3:
            time.sleep(0.2)
            print(Fore.LIGHTCYAN_EX  + "   _____ \n"
                                       "  |     | \n"
                                       "  |     |\n"
                                       "  |      \n"
                                       "  |      \n"
                                       "  |      \n"
                                       "  |      \n"
                                       "__|__\n")
            print(f'{Fore.LIGHTMAGENTA_EX}Wrong letter\nYou have {3} attemts')

    elif count == 4:
           time.sleep(0.2)
           print(Fore.LIGHTCYAN_EX  +"   _____ \n"
                                     "  |     | \n"
                                     "  |     |\n"
                                     "  |     | \n"
                                     "  |      \n"
                                     "  |      \n"
                                     "  |      \n"
                                     "__|__\n")
           print(f'{Fore.LIGHTMAGENTA_EX}Wrong letter\nYou have {2} attemts')

    elif count == 5:
            time.sleep(0.2)
            print(Fore.LIGHTCYAN_EX  +"   _____ \n"
                                      "  |     | \n"
                                      "  |     |\n"
                                      "  |     | \n"
                                      "  |     O \n"
                                      "  |      \n"
                                      "  |      \n"
                                      "__|__\n")
            print(f'{Fore.LIGHTMAGENTA_EX}Wrong letter\nYou have {1} attemt')

    elif count == 6:
        time.sleep(0.2)
        print(Fore.LIGHTCYAN_EX  +"   _____ \n"
                                  "  |     | \n"
                                  "  |     |\n"
                                  "  |     | \n"
                                  "  |     O \n"
                                  "  |    /|\ \n"
                                  "  |    / \ \n"
                                  "__|__\n")
        
        

        
    