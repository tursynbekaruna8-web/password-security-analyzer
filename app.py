import string

def check_password_strength(password: str):
    score = 0
    x = 0

    if any(c.isupper() for c in password):
        score += 1
        x += 1
    if any(c.islower() for c in password):
        score += 1
        x += 1
    if any(c.isdigit() for c in password):
        score += 1
        x += 1
    if any(c in string.punctuation for c in password):
        score += 1
        x += 1

    if x < 4:
        return score, x

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1
    if len(password) >= 20:
        score += 1

    return score, x


def check_password(password: str):
    with open("common.txt", "r", encoding="utf-8") as f:
        common_passwords = set(f.read().splitlines())

    if password in common_passwords:
        return "Password is too common ❌"

    score, x = check_password_strength(password)

    extra = ""
    if x < 4:
        extra = " (Add uppercase, lowercase, digit and symbol)"

    if score <= 1:
        return "Weak ❌" + extra
    elif score <= 3:
        return "Medium ⚠️" + extra
    else:
        return "Strong ✅"