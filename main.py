from termcolor import colored
import os
import colorama
import webbrowser
import signal

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
print(colored('[2] Rosa Parks and the Bus Boycotts', 'red'))
print('')
while True:

   user_input = int(input(colored('[] Type Here: ', 'blue')))

   if user_input == 1:
      webbrowser.get(chrome_path).open(url)
      os.system('cls')
      os.system('python main.py')
      
   elif user_input == 2:
      os.system('cls')
      print(colored("""The Montgomery Bus Boycott was a civil rights protest in which African-Americans refused to ride city buses in Montgomery, Alabama to protest segregation of seats.
               The boycott took place from December 5, 1955 to December 20, 1956 and is considered the first large-scale American protest against apartheid. 
               Four days before the boycott began, Rosa Parks, an African-American woman, was arrested and fined for refusing to give up her bus seat to a white man. 
               The U.S. Supreme Court eventually ordered Montgomery to integrate its bus system, and one of the boycott's leaders named Martin Luther King Jr, 
               became a preacher. Prominent leader of the American civil rights movement.""", 'blue'))
      u_i = colored(input('[Y, N] Continue?: ')).lower()
      if u_i == 'Y':
         os.system('cls')
         os.system('python main.py')
      else:
         os.system('cls')
         exit()
