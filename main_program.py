class PalindromeChecker:
    @classmethod
    def is_palindrome(cls, mot):
        mot = ''.join(e.lower() for e in mot if e.isalnum() or e.isspace())
        return mot == mot[::-1]

class OHCE:
    def __init__(self):
        print("OHCE: Bonjour")

    def palindrome(self, input_str):
        reversed_str = input_str[::-1]
        print(f"OHCE: {reversed_str}")

        if PalindromeChecker.is_palindrome(input_str):
            print("OHCE: Bien dit !")

        print("OHCE: Au revoir")

def main():
    ohce = OHCE()

    while True:
        user_input = input("Entrez une chaîne (ou 'exit' pour quitter) : ")

        if user_input.lower() == 'exit':
            print("OHCE: Au revoir !")
            break

        ohce.palindrome(user_input)

if __name__ == "__main__":
    main()
