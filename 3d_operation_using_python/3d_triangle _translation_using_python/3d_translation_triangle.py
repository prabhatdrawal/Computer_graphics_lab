import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


print("enter the co-ordinates of A in the form of x,y,z")
x1 , y1 , z1 = int(input('enter the x cordinate : ')), int(input('enter the y - cordinate : ')) , int(input('enter the z- cordinate : '))

print("enter the co-ordinates of B in the form of x,y,z")
x2 , y2 , z2 = int(input('enter the x cordinate : ')), int(input('enter the y - cordinate : ')) , int(input('enter the z - cordinate : '))

print("enter the co-ordinates of C in the form of x,y,z")
x3 , y3 , z3  = int(input('enter the x cordinate : ')), int(input('enter the y - cordinate : ')) , int(input('enter the z - cordinate : '))




# translation of triangle above mentioned using the parameter (tx,ty)

tx , ty , tz = int(input('enter the translation in x direction :')), int(input('enter the translation in y direction :')) , int(input('enter the translation in y direction :'))
xt1 = x1 + tx 
xt2 = x2 + tx
xt3 = x3 + tx

yt1 = y1 + tx
yt2 = y2 + tx
yt3 = y3 + tx

zt1 = z1 + tz
zt2 = z2 + tz
zt3 = z3 + tz

print("the new co-ordinates of A are :", xt1, yt1, zt1)
print("the new co-ordinates of B are :", xt2, yt2, zt2)
print("the new co-ordinates of C are :", xt3, yt3, zt3)

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis') 


plt.title('translation of the triangle')
plt.plot([x1,x2,x3,x1],[y1,y2,y3,y1],[z1,z2,z3,z1],'b',label = 'original triangle')
plt.plot([xt1,xt2,xt3,xt1],[yt1,yt2,yt3,yt1],[zt1,zt2,zt3,zt1],'r',label = 'translated triangle')
plt.show()


