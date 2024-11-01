import random
import string

def generate_password(length):
    # Define the character sets to use
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    # Combine all characters
    all_characters = lowercase + uppercase + digits + symbols
    
    # Ensure the password includes at least one character from each category
    if length < 4:
        print("Length should be at least 4 to include all character types.")
        return None

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    
    # User input for password length
    try:
        length = int(input("Enter the desired password length (minimum 4): "))
    except ValueError:
        print("Please enter a valid number.")
        return

    # Generate and display the password
    password = generate_password(length)
    if password:
        print(f"Generated password: {password}")

# Run the password generator
if __name__ == "__main__":
    main()
