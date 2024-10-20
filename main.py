import random
import string

def generate_password(length):
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + special_characters

    # Ensure the password has at least one character from each category for complexity
    if length < 4:
        print("Password length should be at least 4 to include all character types.")
        return None

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 4): "))
            if length < 4:
                print("Please enter a length of at least 4.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    generated_password = generate_password(length)
    if generated_password:
        print(f"Generated Password: {generated_password}")

if __name__ == "__main__":
    main()
