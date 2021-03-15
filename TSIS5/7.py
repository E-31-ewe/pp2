def ar(fname):
    ar = []
    with open(fname) as g:
        for line in g:
            ar.append(line)
        print(ar)
ar('text.txt')
