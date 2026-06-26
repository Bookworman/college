
def is_prime(num):
    if num == 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def is_valid_password(password):

    numbers = list(map(int,password.split(':')))
    if len(numbers) != 3:
        return False
    if str(numbers[0]) != str(numbers[0])[::-1]:
        return False
    if not is_prime(numbers[1]):
        return False
    if numbers[2] % 2 == 0:
        return True
    else:
        return False

print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))
