from colorama import Fore, Style, init
import time
import webbrowser
import sys

ascii = r'''
 (                                                     
 )\ )                (         )                 (     
(()/((     )         )\  (  ( /(          ) (    )\ )  
 /(_))\   (    `  ) ((_)))\ )\())  (   ( /( )(  (()/(  
(_))((_)  )\  '/(/(  _ /((_|(_)\   )\  )(_)|()\  ((_)) 
/ __|(_)_((_))((_)_\| (_)) | |(_) ((_)((_)_ ((_) _| |  
\__ \| | '  \() '_ \) / -_)| '_ \/ _ \/ _` | '_/ _` |  
|___/|_|_|_|_|| .__/|_\___||_.__/\___/\__,_|_| \__,_|  
              |_|                                      
'''
print(f"{Fore.LIGHTBLUE_EX}{ascii}")
#-------------------------------------
im = input(f"{Fore.YELLOW}What do you want to search for (>): ")
default_link = f"https://disboard.org/servers/tag/{im}"
if len(default_link) <= 15:
    print(f"{Fore.RED}Over 15 Char")
    sys.exit()
else:
    print(f"{Fore.GREEN}Getting URL")
time.sleep(1.5)
webbrowser.open(default_link)
print(f"{Fore.GREEN}{default_link} Opened!")
input("enter to exit.")