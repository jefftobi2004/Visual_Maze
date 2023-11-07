import sys
import turtle
import tabulate
from tabulate import tabulate

v2 = []
v = []
dx = [0,1,0,-1] # Un vector de directie pentru coordonata x
dy = [1,0,-1,0] # Un vector de directie pentru coordonata y
n = int( input ("Enter number of lines: ") ) # Citim numarul de linii
m = int( input ("Enter number of columns: ") ) # Citim numarul de coloane

print("Please enter the matrix:")

x = [1]*(m+2)
v.append(x)
for i in range (1, n+1):
    line = list( tuple([1]) + tuple([int(j) for j in input().split()[:m]]) + tuple([1]) )
    v.append(line)
v.append(x)

iS, jS = [ int(x) for x in input("Enter the coordinates of the start point:").split() ]
iF, jF = [ int(x) for x in input("Enter the coordinates of the finish point:").split() ]

screen = turtle.Screen()
pen = turtle.Turtle()
pen.speed(0)
pen.up()

pen.shape("square")
pen.color("black")
pen.shapesize(2)

for i in range (0, n+2):
    for j in range (0, m+2):
        if v[i][j] == 1:
            pen.goto(48 * (j-1), 48 * (1-i))
            pen.stamp()

turtle.done()

