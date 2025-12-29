# Password Strength Checker 🔐

import re

def check_password_strength(password):
    strength = 0

    # Length check
    if len(password) >= 8:
        strength += 1

    # Uppercase letter check
    if re.search(r"[A-Z]", password):
        strength += 1

    # Lowercase letter check
    if re.search(r"[a-z]", password):
        strength += 1

    # Digit check
    if re.search(r"[0-9]", password):
        strength += 1

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    # Strength result
    if strength <= 2:
        return "Weak Password ❌"
    elif strength == 3 or strength == 4:
        return "Medium Password ⚠️"
    else:
        return "Strong Password ✅"


# ---- Main Program ----
password = input("Enter your password: ")
result = check_password_strength(password)
print("Password Strength:", result)

