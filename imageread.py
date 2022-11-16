import numpy as np
import cv2
import matplotlib.pyplot as plt

def show_image(sum_matrix):
 cv2.imshow("Image",sum_matrix)
 if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()

def plothist(sum_matrix,noise_matrix,original_matrix):
 a=np.array(sum_matrix.flatten())
 plt.rcParams["figure.figsize"] = [7.00, 3.50]
 plt.rcParams["figure.autolayout"] = True
 plt.subplot(6,1,1)
 plt.title("Final Image")
 y,binEdges=np.histogram(a,bins=[f for f in range(0,256)])
 plt.hist(a,bins=[f for f in range(0,256)],color='b', edgecolor='red')
 plt.subplot(6,1,2)
 bincenters = 0.5 * (binEdges[1:] + binEdges[:-1])
 plt.plot(bincenters, y, '-', c='black')

 b=np.array(noise_matrix.flatten())
 plt.rcParams["figure.figsize"] = [7.00, 3.50]
 plt.rcParams["figure.autolayout"] = True
 plt.subplot(6,1,3)
 plt.title("Noise Image")
 y,binEdges=np.histogram(b,bins=[f for f in range(0,256)])
 plt.hist(b,bins=[f for f in range(0,256)],color='b', edgecolor='red')
 plt.subplot(6,1,4)
 bincenters = 0.5 * (binEdges[1:] + binEdges[:-1])
 plt.plot(bincenters, y, '-', c='black')

 c=np.array(original_matrix.flatten())
 plt.rcParams["figure.figsize"] = [7.00, 3.50]
 plt.rcParams["figure.autolayout"] = True
 plt.subplot(6,1,5)
 plt.title("Original Image")
 y,binEdges=np.histogram(c,bins=[f for f in range(0,256)])
 plt.hist(c,bins=[f for f in range(0,256)],color='b', edgecolor='red')
 plt.subplot(6,1,6)
 bincenters = 0.5 * (binEdges[1:] + binEdges[:-1])
 plt.plot(bincenters, y, '-', c='black')

 plt.show()

def normal(grayscale):
 noise_matrix = np.random.normal(0,20, (512, 819))
 sum_matrix = grayscale + noise_matrix
 cv2.normalize(sum_matrix,sum_matrix, 0, 255, cv2.NORM_MINMAX, dtype=-1)
 sum_matrix = sum_matrix.astype(np.uint8)
 Hori = np.concatenate((grayscale, sum_matrix), axis=1)
 show_image(Hori)
 plothist(sum_matrix,noise_matrix,grayscale)


def poisson(grayscale):
 noise_matrix=np.random.poisson(lam=100,size=(512,819))
 sum_matrix = grayscale + noise_matrix
 cv2.normalize(sum_matrix,sum_matrix, 0, 255, cv2.NORM_MINMAX, dtype=-1)
 sum_matrix = sum_matrix.astype(np.uint8)
 plt.subplot(1,2,1)
#  show_image(grayscale)
 plt.imshow(grayscale)
 plt.subplot(1,2,2)
 plt.imshow(sum_matrix)
 plt.show()
 
 
 Hori = np.concatenate((grayscale, sum_matrix), axis=1)
 
 plothist(sum_matrix,noise_matrix,grayscale)
 
 
 

def binomial(grayscale):
 noise_matrix=np.random.binomial(100,0.8,size=(512,819))
 sum_matrix = grayscale + noise_matrix
 cv2.normalize(sum_matrix,sum_matrix, 0, 255, cv2.NORM_MINMAX, dtype=-1)
 sum_matrix = sum_matrix.astype(np.uint8)
 sum_matrix=sum_matrix/255
 Hori = np.concatenate((grayscale, sum_matrix), axis=1)
 show_image(Hori)
 plothist(sum_matrix,noise_matrix,grayscale)


def chisquare(grayscale):
 noise_matrix=np.random.chisquare(2,size=(512,819)) 
 sum_matrix = grayscale + noise_matrix
 cv2.normalize(sum_matrix,sum_matrix, 0, 255, cv2.NORM_MINMAX, dtype=-1)
 sum_matrix = sum_matrix.astype(np.uint8)
 sum_matrix=sum_matrix/255
 Hori = np.concatenate((grayscale, sum_matrix), axis=1)
 show_image(Hori)
 plothist(sum_matrix,noise_matrix,grayscale)

def exponential(grayscale):
 noise_matrix=np.random.exponential(5,size=(512,819)) 
 sum_matrix = grayscale + noise_matrix
 cv2.normalize(sum_matrix,sum_matrix, 0, 255, cv2.NORM_MINMAX, dtype=-1)
 sum_matrix = sum_matrix.astype(np.uint8)
 sum_matrix=sum_matrix/255
 Hori = np.concatenate((grayscale, sum_matrix), axis=1)
 show_image(Hori)
 plothist(sum_matrix,noise_matrix,grayscale)

def gamma(grayscale):
 noise_matrix=np.random.gamma(2.,2.,size=(512,819))
 sum_matrix = grayscale + noise_matrix
 cv2.normalize(sum_matrix,sum_matrix, 0, 255, cv2.NORM_MINMAX, dtype=-1)
 sum_matrix = sum_matrix.astype(np.uint8)
 sum_matrix=sum_matrix/255
 Hori = np.concatenate((grayscale, sum_matrix), axis=1)
 show_image(Hori)
 plothist(sum_matrix,noise_matrix,grayscale)
 
img = cv2.imread("emma2.jpeg")

grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image",grayscale)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
input=int(input('''Enter:
               1 -> Normal distribution
               2 -> Poisson distribution
               3 -> Binomial distribution
               4 -> Chisquare distribution
               5 -> Exponential distribution
               6 -> Gamma distribution
                              '''))
if input == 1:
    normal(grayscale)
elif input == 2:
    poisson(grayscale)
elif input ==3:
    binomial(grayscale)
elif input ==4:        
    chisquare(grayscale)
elif input ==5:
    exponential(grayscale)
elif input ==6:
    gamma(grayscale)
else:
    print("Invalid input, Kindly try again")