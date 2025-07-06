import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    digit_criteria = re.search(r"\d", password) is not None
    special_char_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    score = sum([length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_char_criteria])

    if score == 5:
        strength = "Very Strong 💪"
    elif score == 4:
        strength = "Strong 🔐"
    elif score == 3:
        strength = "Medium ⚠️"
    else:
        strength = "Weak ❌"

    print("\nPassword Strength Report:")
    print(f"- Length >= 8: {'✔️' if length_criteria else '❌'}")
    print(f"- Contains lowercase: {'✔️' if lowercase_criteria else '❌'}")
    print(f"- Contains uppercase: {'✔️' if uppercase_criteria else '❌'}")
    print(f"- Contains number: {'✔️' if digit_criteria else '❌'}")
    print(f"- Contains special character: {'✔️' if special_char_criteria else '❌'}")
    print(f"\n✅ Overall Strength: {strength}")

if __name__ == "__main__":
    pwd = input("Enter a password to check its strength: ")
    check_password_strength(pwd)
