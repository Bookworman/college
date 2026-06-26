
def is_prime(number):
    if number < 2:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True

def get_next_prime(number):
    if number < 2:
        return 2
    candidate = number + 1
    if candidate % 2 == 0:
        candidate +=1
    while not is_prime(candidate):
        candidate += 2
    return candidate

print(get_next_prime(6))
print(get_next_prime(7))
print(get_next_prime(14))