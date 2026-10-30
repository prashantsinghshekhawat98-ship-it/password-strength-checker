import string

def check_password(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add a number.")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("Add a special character.")

    if score <= 2:
        print("\nStrength: WEAK")
    elif score <= 4:
        print("\nStrength: MEDIUM")
    else:
        print("\nStrength: STRONG")

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print("- " + suggestion)
    else:
        print("\nGreat! All basic requirements are satisfied.")


password = input("Enter your password: ")
check_password(password)
