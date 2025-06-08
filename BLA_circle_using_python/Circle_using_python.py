# making circle using bresenhams circle algorithm

import matplotlib.pyplot as plt


x0 = int(input("enter the x-cordinate of  centre of the circle"))
y0 = int(input("enter the y-cordinate of centre of the circle"))
r = int(input("enter the radius of the circle"))


def midpoint_circle_draw(x0,y0,r):

    d = 3 - 2*r

    (x,y) = (0,r)
    x_points = []
    y_points = []

    while x<=y:
      x_points.extend([
    x0 + x, x0 - x, x0 + x, x0 - x,
    x0 + y, x0 - y, x0 + y, x0 - y
    ])
      y_points.extend([
     y0 + y, y0 + y, y0 - y, y0 - y,
     y0 + x, y0 + x, y0 - x, y0 - x
     ])

      if d < 0:
               d = d + 4*x + 6
      else:
               d = d + 4*(x - y) + 10
               y -= 1
      x+=1

    return x_points,y_points
    

(x_points,y_points) = midpoint_circle_draw(x0,y0,r)

plt.scatter(x_points,y_points,marker = 'o',color = 'blue')
plt.title("midpoint circle drawing")
plt.grid(True)
plt.gca().set_aspect('equal',adjustable = 'box')
plt.xlabel('x_axis')
plt.ylabel('y_axis')
plt.show()
