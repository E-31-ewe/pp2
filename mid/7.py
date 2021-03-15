import re
cnt = 0
text = input()
t = (input())
s = (input())
f = (input())
x = re.sub(t, s, text)
regex = re.compile(f)
ans = re.findall(regex, x)
for i in ans:
    cnt += 1
print(cnt)