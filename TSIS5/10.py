from collections import Counter
def number_of_words(fname):
    with open(fname) as d:
        return Counter(d.read().split())
print('Number of words in the file:',number_of_words('text.txt'))
