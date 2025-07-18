from random import choice
from time import sleep
from time import time 
from colorama import Fore, Back, Style
import colorama
colorama.init(autoreset = True)
aleatory = "abdefghijklmopkrstuvwxyzABCDEFGHIJQLMOPQRSTUV"

#FUNCTION 

def crash(): # ici on cree la fonction crash , pour pouvoir la rappeler plus tard print = True SI la fonction est appeler 
    print(f"{Fore.RED}Close in 3 seconds. Reason : Incorrect Password")
    sleep(2)
    exit()

def pswrd(): # ici on cree la verification , pour ca on cree la fonction et on y mets une variable input , si il n'y a pas 1234 dans la variable on appel + appel de la def sinon ya rien 
    verification = (input(f"{Fore.MAGENTA}Password : "))
    if not "1234" in verification:
       crash()
pswrd()
    
   
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
number = input(f"{Fore.MAGENTA}How many link ? ") # variable + demande 
print(f"{number} Link created.") # on montre ce que l'user a demander

try:
    number = int(number) # ici try va voir si number = a des integer/entier , si oui on continue chill , si pas on passe par except 
except ValueError: 
        print(f"{Fore.MAGENTA}Close in 3 seconds (caractere incorrect)")
        sleep(0.2)
        exit()
generator = 1 # le generateur commence a partir de 1 

start = time() # on demarre le chrono 
while number >= generator: # On continue a refaire ce qui a en dessous tant que number est plus haut que generator
  code = "" # la remplir par l'aleatoire
  sleep(0.1) # temps de pause pour realisme et prise de conscience. 
  if generator % 50 == 0: # si 50 code on ete generer on fait .. 
    print(f"{Fore.RED}Wait..")
    sleep(2)
  for x in range(12): # pour la variable temporaire de x dans une ranger de 12
   code += choice(aleatory) # = code ( variable vide ) + choix aleatoire dans notre bibliotheque 
  print(f"{Fore.MAGENTA}https://discord.com/gifts/"+code) # On affiche le resultat 
  generator += 1  # +1 jusqu'au nombre de lien demander
end = time() # on coupe une fois que python est sortie de la boucle 
print(f"{Fore.MAGENTA}Time : ",round(end - start, 1), f"{Fore.MAGENTA}secondes") # on affiche le temps pris par la machine 
sleep(10) # 10 secondes d'attente pour "attendre"
exit()

 

