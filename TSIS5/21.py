import string
def func(n):
    with open('dop_file.txt','w') as d:
        alp = string.ascii_uppercase
        bukv = [alp[i:i + n] + '\n' for i in range(0, len(alp), n)]
        d.writelines(bukv)
func(4)