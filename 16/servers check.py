
print('This program will check containment of two servers')
print('First you will have to input programs on first(main) server')
print('Second you will have to input programs on second(reserve) server')

# data.db image.png log.txt - first test input
# image.png script.py data.db - second test input

server_a = set(input('please enter line of programs on first server: ').split())
server_b = set(input('please enter line of programs on second server: ').split())

print(f'shared files are: {' '.join(server_a & server_b)}')
print(f'lost files are: {' '.join(server_a - server_b)}')