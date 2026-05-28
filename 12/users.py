users = ['Admin','Guest','User','Bot']
print(f'There are original list of users: {users}')
print('Whoopedy doopedy')
users[2] = 'Moderator'
users[-1] = 'SuperAdmin'
users.append('Newbie')
print(f'There are new list of users: {users}')