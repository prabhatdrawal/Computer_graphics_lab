import matplotlib.pyplot as plt


print("enter the co-ordinates of A in the form of x,y")
x1 , y1 = int(input('enter the x cordinate : ')), int(input('enter the y - cordinate : '))

print("enter the co-ordinates of B in the form of x,y")
x2 , y2 = int(input('enter the x cordinate : ')), int(input('enter the y - cordinate : '))

print("enter the co-ordinates of C in the form of x,y")
x3 , y3 = int(input('enter the x cordinate : ')), int(input('enter the y - cordinate : '))




# translation of triangle above mentioned using the parameter (tx,ty)

tx , ty = int(input('enter the translation in x direction :')), int(input('enter the translation in y direction :'))
xt1 = x1 + tx
xt2 = x2 + tx
xt3 = x3 + tx

yt1 = y1 + tx
yt2 = y2 + tx
yt3 = y3 + tx

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('translation of the triangle')
plt.plot([x1,x2,x3,x1],[y1,y2,y3,y1],'b',label = 'original triangle')
plt.plot([xt1,xt2,xt3,xt1],[yt1,yt2,yt3,yt1],'r',label = 'translated triangle')
plt.show()


