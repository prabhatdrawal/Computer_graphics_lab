import matplotlib.pyplot as plt 
import mpl_toolkits.mplot3d as mplot3d

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

print("enter the co-ordinates of A in the form of x,y,z")
x1 , y1 , z1 = int(input('enter the x cordinate : ')), int(input('enter the y - cordinate : ')) , int(input('enter the z- cordinate : '))

print("enter the co-ordinates of B in the form of x,y,z")
x2 , y2 , z2 = int(input('enter the x cordinate : ')), int(input('enter the y - cordinate : ')) , int(input('enter the z - cordinate : '))

print("enter the co-ordinates of C in the form of x,y,z")
x3 , y3 , z3  = int(input('enter the x cordinate : ')), int(input('enter the y - cordinate : ')) , int(input('enter the z - cordinate : '))

# scaling of the triangel
sx = float(input('enter the scaling factor in x direction : '))
sy = float(input('enter the scaling factor in y direction : '))
sz = float(input('enter the scaling factor in z direction : '))

x1_scaled = x1 * sx
x2_scaled = x2 * sx
x3_scaled = x3 * sx

y1_scaled = y1 * sx
y2_scaled = y2 * sx
y3_scaled = y3 * sx

z1_scaled = z1 * sx
z2_scaled = z2 * sx
z3_scaled = z3 * sx



print("the new co-ordinates of A are :", x1_scaled, y1_scaled, z1_scaled)
print("the new co-ordinates of B are :", x2_scaled, y2_scaled, z2_scaled)
print("the new co-ordinates of C are :", x3_scaled, y3_scaled, z3_scaled)

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis') 


plt.title('scaling of the triangle')
plt.plot([x1_scaled,x2_scaled,x3_scaled,x1_scaled],[y1_scaled,y2_scaled,y3_scaled,y1_scaled],[z1_scaled,z2_scaled,z3_scaled,z1_scaled],'r',label = 'scaled trianngle')
plt.plot([x1,x2,x3,x1],[y1,y2,y3,y1],[z1,z2,z3,z1],'b',label = 'original triangle')
plt.show()




