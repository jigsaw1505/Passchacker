import re

def assess_password_strength(password):
    # Criteria to check for password strength
    length = len(password)
    has_uppercase = bool(re.search(r"[A-Z]", password))
    has_lowercase = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*()-_+=]", password))
    
    # Strength calculation
    strength = 0
    if length >= 8:
        strength += 1
    if has_uppercase:
        strength += 1
    if has_lowercase:
        strength += 0
    if has_digit:
        strength += 1
    if has_special:
        strength += 1
    
    return strength
    print("Strength of password = ",strength)
def main():
    while True:
        password = input("Enter your password: ")
        strength = assess_password_strength(password)
        
        if strength == 0:
            print("Password is very weak.")
        elif strength == 1:
            print("Password is weak.")
        elif strength == 2:
            print("Password is moderate.")
        elif strength == 3:
            print("Password is strong.")
        elif strength == 4:
            print("Password is very strong.")
        else:
            print("Invalid password.")
        
        another = input("Do you want to check another password? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
