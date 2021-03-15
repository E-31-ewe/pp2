n = int(input())
g = list(input().split())
k = int(input())
tot1 = g[:k]
tot2 = g[k:]
tot3 = [x.strip(' ') for x in tot1]
tot4 = [x.strip(' ') for x in tot2]
print(tot3*tot4)