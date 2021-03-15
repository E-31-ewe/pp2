items = ['leg','arm','shoulder']
with open('text.txt','w') as f:
    for i in items:
        f.write("%s\n" % i)
ans = open('text.txt')
print(ans.read())