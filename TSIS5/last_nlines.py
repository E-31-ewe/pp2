f = open('text.txt','r')
l = f.readlines()
last_l = l[:1]
print(last_l)
f.close()