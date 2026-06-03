

print('this program will form a maze from your input')
print('''
0 - passway
1 - wall
t - trap
c - coin
e - exit
z - enemy
s - start
''')
# 1e111t000cz11011100111s11 - тестовый ввод
maze = list(input('please enter line of 25 symbols:'))

for i in range(5):
    print(''.join(maze[i*5:i*5+5])
          .replace('0', '⬜')
          .replace('1', '⬛')
          .replace('t', '🔷')
          .replace('c', '🟡')
          .replace('e', '🟫')
          .replace('z', '🐷')
          .replace('s', '⭐'))

exit_index = maze.index('e')
exit_x_pos = exit_index % 5
exit_y_pos = exit_index // 5
print('exit coordinates:',exit_x_pos, exit_y_pos)
start_index = maze.index('s')
start_x_pos = start_index % 5
start_y_pos = start_index // 5
print('start coordinates:',start_x_pos, start_y_pos)
manhattan_distance = abs(start_x_pos - exit_x_pos) + abs(start_y_pos - exit_y_pos)
print('manhattan distance:',manhattan_distance)

coin_count = maze.count('c')
print(f'🟡x{coin_count}')

enemy_count = maze.count('e')
trap_count = maze.count('t')
player_health = (100 - enemy_count * 50 - trap_count * 10) // 10
if player_health < 0:
    player_health = 0
print('player health:',end='')
for i in range(player_health):
    print('♥',end='')
for i in range(10-player_health):
    print('♡',end='')

