import matplotlib.pyplot as plt


print("enter the co-ordinates of A in the form of x,y")
x1 , y1 = int(input('enter the x cordinate : ')), int(input('enter the y - cordinate : '))

print("enter the co-ordinates of B in the form of x,y")
x2 , y2 = int(input('enter the x cordinate : ')), int(input('enter the y - cordinate : '))

print("enter the co-ordinates of C in the form of x,y")
x3 , y3 = int(input('enter the x cordinate : ')), int(input('enter the y - cordinate : '))


# reflection on x axis of triangle above mentioned
'''''
reflection_matrix = [{1,0,0},{0,-1,0},{0,0,1}]
original_matrix = [{x1,x2,x3},{y1,y2,y3},{1,1,1}]


# first row of the matrix 
x1_ref = x1*1 + x2*0+x3*0
x2_ref = x1*0 + x2*(-1) + x3*0
x3_ref = x1*0 + x2*(0) + x3*1

# second row of the matrix 
y1_ref = y1*1 + y2*0+y3*0
y2_ref = y1*0 + y2*(-1) + y3*0
y3_ref = y1*0 + y2*(0) + y3*1
'''

x_orig = [x1, x2, x3, x1]
y_orig = [y1, y2, y3, y1]

# Reflected coordinates (about x-axis)
x_ref = x_orig.copy()
y_ref = [-y for y in y_orig]

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Reflection of Triangle about X-axis')
plt.axhline(0, color='black', linewidth=0.5) 
plt.grid(True)
plt.axis('equal')

plt.plot(x_orig, y_orig, 'b-o', label='Original Triangle')
plt.plot(x_ref, y_ref, 'r--o', label='Reflected Triangle')

plt.text(x1, y1, ' A', fontsize=10)
plt.text(x2, y2, ' B', fontsize=10)
plt.text(x3, y3, ' C', fontsize=10)
plt.text(x1, -y1, " A'", fontsize=10)
plt.text(x2, -y2, " B'", fontsize=10)
plt.text(x3, -y3, " C'", fontsize=10)

plt.legend()
plt.show()
