n = int(input())
names = set(input().split())
m = int(input())
names2 = set(input().split())
print('Missed students:')
print('-', *(names.difference(names2)))
print('Not in the group:')
print('-', *(names2.difference(names)))
