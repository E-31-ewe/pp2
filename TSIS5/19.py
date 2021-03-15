import glob
empty_list = []
a = glob.glob('text.txt')
for file_elem in a:
    with open(file_elem,'r') as d:
        empty_list.append(d.read())
print(empty_list)