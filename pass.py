import random
import string

def generate_password(length, complexity):
    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity. Please choose 1, 2, or 3.")
        return None

    generated_password = ''.join(random.choice(characters) for _ in range(length))
    return generated_password

def main():
    length = int(input("Enter the required length of your password: "))
    complexity = int(input("Enter the choice  (1 - Letters only, \n"
                           " 2 - Letters and digits, \n"
                           "3 - Letters, digits, and punctuation): "))

    password = generate_password(length, complexity)
    if password:
        print("Your password is ready!:", password)

if __name__ == "__main__":
    main()
