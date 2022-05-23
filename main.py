from termcolor import colored
import os
import colorama
import webbrowser

colorama.init()


url = 'https://github.com/xoxocjm111/History-Project'
#windows path
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


os.system('cls')
print(colored("""  _______ _             _____ _       _ _   _____  _       _     _         __  __                                     _   
 |__   __| |           / ____(_)     (_) | |  __ \(_)     | |   | |       |  \/  |                                   | |  
    | |  | |__   ___  | |     ___   ___| | | |__) |_  __ _| |__ | |_ ___  | \  / | _____   _____ _ __ ___   ___ _ __ | |_ 
    | |  | '_ \ / _ \ | |    | \ \ / / | | |  _  /| |/ _` | '_ \| __/ __| | |\/| |/ _ \ \ / / _ \ '_ ` _ \ / _ \ '_ \| __|
    | |  | | | |  __/ | |____| |\ V /| | | | | \ \| | (_| | | | | |_\__ \ | |  | | (_) \ V /  __/ | | | | |  __/ | | | |_ 
    |_|  |_| |_|\___|  \_____|_| \_/ |_|_| |_|  \_\_|\__, |_| |_|\__|___/ |_|  |_|\___/ \_/ \___|_| |_| |_|\___|_| |_|\__|
                                                      __/ |                                                               
                                                     |___/                                                                """, 'blue'))


print('')
print(colored('[1] Information', 'blue'))
print('')
user_input = print(input(colored('[] Type Here: ', 'blue')))

if user_input == '1':
   #webbrowser.get(chrome_path).open(url)
   print('hello')