import random

a=input('deseja jogar o dado? ')
a=a.lower()
while (a=='sim'):
    b=random.randint(1,6)
    print(b)
    a=input('deseja jogar o dado? ')
    a=a.lower()

