import random
def randomno(fname):
    stroki = open(fname).read().splitlines()
    return random.choice(stroki)
print(randomno('text.txt'))