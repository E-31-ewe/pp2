moves = str(input())
x1,y1 = map(int,input().split())
x2, y2 = 0, 0
for i in range(len(moves)):
    if moves[i] == 'R':
        x2 += 1
    elif moves[i] == 'L':
        x2 -= 1
    elif moves[i] == 'U':
        y2 += 1
    elif moves[i] == 'D':
        y2 -= 1 
    if x1 == x2 and y1 == y2:
     print('Passed')
     exit()
     break
    
print('Missed')
