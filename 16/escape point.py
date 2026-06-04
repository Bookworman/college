agent = (2,2)
points = {(1,1), (5,5), (0,3)}
nearest = points.pop()

print(f'you are a secret agent, currently standing at {agent} coordinates')

for item in points:
    if abs(nearest[0] - agent[0]) + abs(nearest[1] - agent[1]) > abs(item[0] - agent[0]) + abs(item[1] - agent[1]):
        nearest = item
print('the nearest exit is:',nearest)
