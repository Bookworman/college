
print('this program will check is your word is polyndrome or not')
word = list(input('what is your word? '))
second_word= word[::-1]
if second_word == word:
    print('it is a polyndrome')
else:
    print('it is NOT a polyndrome')