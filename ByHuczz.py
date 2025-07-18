from random import choice
from time import sleep
from time import time 
from colorama import Fore, Back, Style
import colorama
colorama.init(autoreset = True)
password = input(f"Password : ")
if not "1985" in password:
   print("Wrong Password. 2 seconds before exit ")
   sleep(2)
   exit()
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
        print(f"{Fore.MAGENTA}Close in 3 seconds \n(caractere incorrect)")
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
print(f"{Fore.MAGENTA}Time : ",round(end - start, 1), f"{Fore.MAGENTA}secondes")
sleep(10)
exit()

 

