import string

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = any(c.isupper() for c in password)
    lowercase_criteria = any(c.islower() for c in password)
    digit_criteria = any(c.isdigit() for c in password)
    special_criteria = any(c in string.punctuation for c in password)

    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_criteria:
        return "Strong"
    elif length_criteria and (uppercase_criteria or lowercase_criteria) and digit_criteria:
        return "Moderate"
    else:
        return "Weak"

if __name__ == '__main__':
    while True:
        password = input("\nEnter a password to assess its strength (or type 'quit' to exit): ")
        
        if password.lower() == 'quit':
            break
        
        strength = check_password_strength(password)
        print(f"The strength of your password '{password}' is: {strength}")