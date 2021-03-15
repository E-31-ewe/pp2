def store_var(fname):
    with open (fname,'r') as tot:
        dt = tot.readlines()
        print(dt)
store_var('text.txt')