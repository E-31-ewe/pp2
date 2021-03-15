n = int(input())
arr = list(map(int,input().split()))
myset = set()
for i in arr:
    myset.add(i)
if len(arr) == len(myset):
    print('Yes')
else:
    print('No')