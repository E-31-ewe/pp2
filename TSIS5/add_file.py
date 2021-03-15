def add_text(fname):
    from itertools import islice
    with open(fname,'w') as q:
        q.write('Show yourself\n')
        q.write('Tell about yourself')
    ans = open(fname)
    print(ans.read())
add_text('text.txt')