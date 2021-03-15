def count(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i+1
print('Number of lines in the file:', count('text.txt'))