def validate_password(password):
    # Check minimum length
    if len(password) < 8:
        return False

    # Check for the presence of letters (uppercase and lowercase) and a digit
    has_lowercase = any(char.islower() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)

    # Check for the absence of spaces
    has_no_spaces = ' ' not in password

    # Return True if all conditions are met, otherwise False
    return has_lowercase and has_uppercase and has_digit and has_no_spaces

# Example usage:
password_to_check = "Passw0rd"
if validate_password(password_to_check):
    print("Password is valid.")
else:
    print("Password is not valid.")
