
import copy

names = ['A', 'B', 'C', 'D', ['E', 'F'], 'G']
names2 = names.copy()
names3 = copy.deepcopy(names)

print(names)
print(names2)
print(names3)
print('------------------------------------------')

names[2] = 'H'

print(names)
print(names2)
print(names3)
print('------------------------------------------')


names[4][0] = 'T'

print(names)
print(names2)
print(names3)