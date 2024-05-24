import re

def check_password_strength(password):
    # Initialize a score variable
    score = 0
    
    # Length check
    length = len(password)
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1

    # Pattern checks
    patterns = [
        r'[a-z]',         # Lowercase letter
        r'[A-Z]',         # Uppercase letter
        r'[0-9]',         # Digit
        r'[!@#$%^&*(),.?":{}|<>]',  # Special character
    ]

    # Check for the presence of each pattern and add to the score
    for pattern in patterns:
        if re.search(pattern, password):
            score += 1

    # Check for sequences of the same character
    if re.search(r'(.)\1{2,}', password):
        score -= 1  # Penalty for repeated sequences
    
    # Check for common patterns
    common_patterns = [
        '123456', 'password', 'qwerty', 'abc123', 'letmein', 'welcome', 'iloveyou', 'admin', 'user'
    ]
    for common_pattern in common_patterns:
        if common_pattern in password.lower():
            score -= 1  # Penalty for common patterns

    # Score interpretation
    if score <= 2:
        strength = "Very Weak"
    elif score == 3:
        strength = "Weak"
    elif score == 4:
        strength = "Moderate"
    elif score == 5:
        strength = "Strong"
    elif score >= 6:
        strength = "Very Strong"

    return {
        "score": score,
        "strength": strength
    }

# Example usage
passwords = [
    "password",
    "12345678",
    "Passw0rd!",
    "Str0ngP@ssw0rd!",
    "abcABC123!@#",
    "aaaAAA111!!!",
    "A1b2C3d4E5F6G7",
    "P@$$w0rd",
    "letmein123"
]

for pwd in passwords:
    result = check_password_strength(pwd)
    print(f"Password: {pwd}, Strength: {result['strength']}, Score: {result['score']}")
