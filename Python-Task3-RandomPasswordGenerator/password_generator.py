import random
import string

def generate_password():
    print("--- Random Password Generator ---")

    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("Password length must be positive.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))

        print("\nGenerated Password:", password)

    except ValueError:
        print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    generate_password()