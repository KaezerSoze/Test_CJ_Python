def str_palindrome(mot):
    mot = mot.lower()
    mot = ''.join(e for e in mot if e.isalnum())
    return mot == mot[::-1]

# Salutation à l'initialisation
print("Bonjour ! Bienvenue dans le programme Palindrome.")

while True:
    str_utilisateur = input("Entrez un mot (ou 'exit' pour quitter) : ")

    if str_utilisateur.lower() == 'exit':
        print("Au revoir !")
        break

    if str_palindrome(str_utilisateur):
        print(f"{str_utilisateur} est un palindrome.")
    else:
        print(f"{str_utilisateur} n'est pas un palindrome.")
