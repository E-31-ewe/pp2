def countr(filepath):
    with open(filepath) as a:
        ans = a.read()
        ans.replace(',',' ')
        return len(ans.split(' '))
print (countr('text.txt'))