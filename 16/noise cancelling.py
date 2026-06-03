
print('this program will tell you number of unique words in your input and sort them')
# код альфа код браво альфа - test input
words = set(input('please enter your words: ').split())
print(f'there are: {len(words)} unique words')
print(f'words are: {' '.join(sorted(words))}')

