import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("emma2.jpg")

greyimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
chisquare=np.random.chisquare(1.4,size=greyimg.shape)
normal=np.random.normal(60,20,size=greyimg.shape)
# sum_matrix=chisquare+greyimg
sum_matrix=normal+greyimg
sum_matrix=sum_matrix.astype(np.uint8)
cv2.imshow(sum_matrix)
if cv2.waitKey(0):
    cv2.destroyAllWindows()
a=sum_matrix.flatten()
plt.subplot(4,1,1)
plt.title("Final image")
plt.hist(a,bins=[f for f in range(0,256)],edgecolor="blue",color="red")
plt.plot()
plt.subplot(4,1,2)
y,x=np.histogram(a,bins=[f for f in range(0,256)])
x_new=0.5*(x[:-1]+x[1:])
plt.plot(x_new,y,"-",color="black")
# plt.show()

b=normal.flatten()
plt.subplot(4,1,3)
plt.title("Normal Distribution")
plt.hist(b,bins=[f for f in range(0,256)],edgecolor="blue",color="red")
plt.plot()
plt.subplot(4,1,4)
y,x=np.histogram(b,bins=[f for f in range(0,256)])
x_new=0.5*(x[:-1]+x[1:])
plt.plot(x_new,y,"-",color="black")
plt.show()