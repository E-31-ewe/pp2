a = list(map(str,input().split()))
word = str
maxim = 0
for i in range(len(a)):
    if len(a[i]) > maxim:
        maxim = len(a[i])
        word = a[i]
print(word, maxim)     
