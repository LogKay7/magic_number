"""
Le nombre magique :
	-> Faire deviner un nombre aléatoire à l'utilisateur en 4 vies maximum.
"""

import random

# Déclarations :

def ask_number(NBR_MIN, NBR_MAX):
	print(f"Quel est le nombre magique ? (Compris entre {NBR_MIN} et {NBR_MAX})")
	nbr_int = NBR_MAX + 1
	while (nbr_int > NBR_MAX):
		nbr = input("Votre réponse : ")
		try:
			nbr_int = int(nbr)
		except:
			print("Erreur : veuillez entrer un nombre.")
		else:
			if nbr_int < NBR_MIN or nbr_int > NBR_MAX:
				print(f"Erreur : veuillez entrer un nombre compris entre {NBR_MIN} et {NBR_MAX}.")
				nbr_int = NBR_MAX + 1
	return nbr_int


NBR_MIN = 0
NBR_MAX = 10
nbr = random.randint(NBR_MIN, NBR_MAX)
nbr_user = NBR_MAX + 1
nb_vies = 4
while nbr_user != nbr and nb_vies > 0:
	print(f"{nb_vies} vies restantes.")
	nbr_user = ask_number(NBR_MIN, NBR_MAX)
	if (nbr == nbr_user):
		print()
		print(f"Bien joué ! Le nombre était {nbr}")
		break
	elif nbr_user > nbr:
		print()
		print("C'est moins.")
	else:
		print()
		print("C'est plus !")
	nb_vies -= 1
	print()

if (nb_vies == 0):
	print()
	print("Dommage... Retentez votre chance !")
