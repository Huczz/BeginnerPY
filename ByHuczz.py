from random import choice
from time import sleep
from time import time 
from colorama import Fore, Back, Style
import colorama
colorama.init(autoreset = True)
aleatory = "abdefghijklmopkrstuvwxyzABCDEFGHIJQLMOPQRSTUV"
print(f"""{Fore.MAGENTA}
 ███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████       ▄████ ▓█████  ███▄    █ 
 ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒    ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░   ░▒▓███▀▒░▒████▒▒██░   ▓██░
░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░     ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░      ░   ░  ░ ░  ░░ ░░   ░ ▒░
   ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒     ░ ░   ░    ░      ░   ░ ░ 
         ░  ░              ░         ░ ░           ░    ░  ░         ░ 
 by Huczz""")
number = input(f"{Fore.MAGENTA}How many link ? ")

try:
    number = int(number)
except ValueError: 
        print(f"{Fore.MAGENTA}Fermeture du programme \n(caractere incorrect)")
        sleep(2)
        exit()
generator = 1
start = time()

while number >= generator:
  code = ""
  sleep(0.2)
  if generator % 50 == 0:
    print(f"{Fore.RED}Wait..")
    sleep(2)
  for x in range(12):
   code += choice(aleatory)
  print(f"{Fore.MAGENTA}https://discord.com/gifts/"+code)
  generator += 1  
end = time()
print(f"{Fore.MAGENTA}Temps total : ",round(end - start, 1), f"{Fore.MAGENTA}secondes")
sleep(10)
exit()

 

