import matplotlib.pyplot as plt

x1 = float(input("enter the x - co-ordinae of point 1"))
y1 = float(input("enter the y - co-ordinae of point 1"))
x2 = float(input("enter the x - co-ordinae of point 1"))
y2 = float(input("enter the x - co-ordinae of point 1"))
dx = x2 - x1
dy = y2 - y1
m = dy/dx
(x,y) = (x1,y1)
steps = int(max(abs(dx), abs(dy)))
x_inc = dx / steps
y_inc = dy / steps
x = x1
y = y1

x_points = []
y_points = []

for i in range(steps + 1):
        x_points.append(round(x))
        y_points.append(round(y))
        x += x_inc
        y += y_inc

plt.plot(x_points, y_points, marker='o', color='blue')
plt.title("DDA Line Drawing")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()