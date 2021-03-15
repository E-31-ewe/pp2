def longest(fname):
    with open(fname,'r') as got:
        words = got.read().split()
        maxim_len = len(max(words, key=len))
        return[word for word in words if len(word)==maxim_len]
print (longest('text.txt'))