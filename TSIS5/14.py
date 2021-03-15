with open('text.txt') as a:
    with open('text_copy.txt') as b:
        for line1, line2 in zip(a,b):
            print(line1+line2)