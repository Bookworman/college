import random

answer = ['100%','5%','10%','15%','20%','25%','30%','35%','40%','45%','50%','55%','60%','65%','70%','75%','80%','85%','90%','95%']
print('hello world i am magic ball, ask me a question and i will tell you probability of it')
name = input('what is your name? ')
print(f'hello {name}')

while True:
    question = input('whats your question? ')
    print(f'probability of this:{random.choice(answer)}')
    while True:
        resolve = input('Do you have any more questions?')
        if resolve.lower() == 'yes':
            break
        elif resolve.lower() == 'no':
            print('bye,see you next time')
            exit()
        else:
            print('sorry, i understand only yes or no')