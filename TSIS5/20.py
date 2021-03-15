import string,os
if not os.path.exists('words'):
    os.makedirs('words')
for word in string.ascii_uppercase:
    with open(word + 'text.txt','w') as d:
        d.writelines(word)

