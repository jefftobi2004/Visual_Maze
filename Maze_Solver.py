import sys
from tabulate import tabulate
v = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]
n = int(input("Enter number of lines: "))
m = int(input("Enter number of columns: "))

#print(f'You entered {n} and its type is {type(n)}')
#print(f'You entered {m} and its type is {type(m)}')

x = [1]*(m+2)
v.append(x)

for i in range(1,n+1):   
    line = list(tuple([1]) + tuple([int(j) for j in input().split()]) + tuple([1]))
    v.append(line)
v.append(x)

iS,js=[int(x) for x in input("Enter the coordinates of the start point: ").split()]
iF,jf=[int(x) for x in input("Enter the coordinates of the finish point: ").split()]


def bk(i,j,poz):
    global iS, js, iF, jf, v

    if v[i][j] == 0:
        v[i][j]=poz
        if i == iF and j == jf:
            print(tabulate(v,tablefmt="fancy_grid")) 
            sys.exit(0)
        else:
            for k in range (0,4):
                bk(i+dx[k], j+dy[k], poz+1)
        v[i][j]=0 

bk(iS, js, 2)       
