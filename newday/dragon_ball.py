

magics = {}
enemy = {
    'meerim':1
}

magic_file = open('magic.txt', 'r')

# print(magic_file.read())
magic_array = magic_file.readlines()

for c_magic in magic_array:
    magic_striped = c_magic.strip()
    magic_splited = magic_striped.split(',')
    magics[magic_splited[0]] = float(magic_splited[1])


print('Ur oponent is', enemy)
# print(magics['waterfall'])

while enemy['meerim'] != 0:
    kick = input('name of power: ')
    k = magics[kick]
    enemy['meerim'] = enemy['meerim'] - k
    if enemy['meerim'] <= 0:
        enemy['meerim'] = 0
        print('HP meerim  is 0')
        print(' PLAYER  Win')
        break
    print('HP enemy:' , enemy['meerim'])




