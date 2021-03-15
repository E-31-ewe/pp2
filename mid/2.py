import re
text = input()
word = input()
s = re.compile(word)
match = re.search(s, text)
if match:
     print('First time {} occured in position: {}'.format(word, match.start()))
else:
     print('Not found')
     