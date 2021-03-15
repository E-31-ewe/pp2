f = open('text.txt','r')
f_contents = f.readlines()
c = []
for line in f_contents:
    c.append(line)
print(c)
f.close()