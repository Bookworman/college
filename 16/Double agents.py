
print('You will have to input surnames of agents in FBI, MI-6, GRU, and program will sor out on they are in first two and not in third')

# Bond Smith Hunt Armstrong Quill - first input for test
# Bond Power Hunt Armstrong Quill - second input for test
# Petrov Hunt Ivanov - third input for test

agents_fbi = set(input('please enter surnames of agents in FBI: ').split())
agents_mi = set(input('please enter surnames of agents in MI-6: ').split())
agents_gru = set(input('please enter surnames of agents in GRU: ').split())

print(f'founded surnames: {' '.join(sorted(agents_fbi & agents_mi - agents_gru, reverse=True))}')