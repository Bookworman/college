
print('You will have to input three lines of IP adresses and frogram will exclude ones that occur in all three lines')

# 1.1.1.1 8.8.8.8 - first input for test
# 8.8.8.8 2.2.2.2 - second input for test
# 1.1.1.1 8.8.8.8 3.3.3.3 - third input for test

ip_1 = set(input('please enter line of first IP: ').split())
ip_2 = set(input('please enter line of second IP: ').split())
ip_3 = set(input('please enter line of third IP: ').split())

ip_final = (ip_1 | ip_2 | ip_3) - (ip_1 & ip_2 & ip_3)

print(f'valid IP: {' '.join(sorted(ip_final))}')