
def is_password_good(password):
    if len(password) >= 8 and any(c.isupper() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password):
        return True
    else:
        return False

print(is_password_good('aabbCC11OP'))
print(is_password_good('abC1pu'))
