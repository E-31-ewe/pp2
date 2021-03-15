def removing(fname):
    a = open(fname).readlines()
    return [i.rstrip('\n') for i in a]
print(removing('text.txt'))