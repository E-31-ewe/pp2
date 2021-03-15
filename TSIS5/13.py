with open('text.txt','r') as rf:
    with open('text_copy','w') as rw:
        for line in rf:
            rw.write(line)