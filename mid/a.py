import re
x = input()
match = re.search('[A-Z]{1}[a-z]{1}', x)
if match:
    print("Found a match!")
else:
    print("Not match!")