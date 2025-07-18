from random import choice
from time import sleep, time
from colorama import Fore, Style
import colorama
colorama.init(autoreset=True)

characters = "abdefghijklmopkrstuvwxyzABCDEFGHIJQLMOPQRSTUV"

# FUNCTIONS

def crash():
    # If the function is called, print a message then exit
    print(f"{Fore.RED}Closing in 3 seconds. Reason: Incorrect Password")
    sleep(2)
    exit()

def password_check():
    # Ask for a password and validate it
    entered = input(f"{Fore.MAGENTA}Password: ")
    if "1234" not in entered:
        crash()

password_check()

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
 by Huczz
""")

amount = input(f"{Fore.MAGENTA}How many links? ")
print(f"{amount} links will be generated.")

try:
    amount = int(amount)  # Convert input to int or crash
except ValueError:
    print(f"{Fore.MAGENTA}Closing in 3 seconds (invalid character)")
    sleep(0.2)
    exit()

count = 1  # Start counter at 1
start = time()  # Start timer

while amount >= count:
    code = ""  # Empty string for new code
    sleep(0.1)  # Realistic delay

    if count % 50 == 0:
        print(f"{Fore.RED}Wait...")
        sleep(2)

    for _ in range(12):  # Generate 12-character code
        code += choice(characters)

    print(f"{Fore.MAGENTA}https://discord.com/gifts/" + code)
    count += 1

end = time()  # End timer
print(f"{Fore.MAGENTA}Time: ", round(end - start, 1), f"{Fore.MAGENTA}seconds")
sleep(10)
exit()
