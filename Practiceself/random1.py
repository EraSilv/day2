import random
s = int(input('Загадай число: '))

p = random.randint(1,s+10)
while p != s:
    p = random.randint(1,s+10)
    print('nabor chisel',p)
    

if p == s:
    print('urA VY NASHLI',p)