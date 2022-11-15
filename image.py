
#This code is made by Vishnu Kumar Srivastava
# Roll no. 102118066
import numpy as np
import cv2
import matplotlib.pyplot as plt



def normal(grayscale):
 noise_matrix = np.random.normal(0,20, grayscale.shape)
 sum_matrix = grayscale + noise_matrix
 cv2.normalize(sum_matrix,sum_matrix, 0, 255, cv2.NORM_MINMAX, dtype=-1)
 sum_matrix = sum_matrix.astype(np.uint8)#jo matrix print hota hai best hota hai
 show_image(sum_matrix)
 plothist(sum_matrix,noise_matrix,grayscale)


def poisson(grayscale):
 noise_matrix=np.random.poisson(lam=100,size= grayscale.shape)
 sum_matrix = grayscale + noise_matrix
 cv2.normalize(sum_matrix,sum_matrix, 0, 255, cv2.NORM_MINMAX, dtype=-1)
 sum_matrix = sum_matrix.astype(np.uint8)
 plothist(sum_matrix,noise_matrix,grayscale)
 show_image(sum_matrix/255)


def binomial(grayscale):
 noise_matrix=np.random.binomial(100,0.8,size=grayscale.size)
 sum_matrix = grayscale + noise_matrix
 cv2.normalize(sum_matrix,sum_matrix, 0, 255, cv2.NORM_MINMAX, dtype=-1)
 sum_matrix = sum_matrix.astype(np.uint8)
 plothist(sum_matrix,noise_matrix,grayscale)
 show_image(sum_matrix/255)


def chisquare(grayscale):   
 noise_matrix=np.random.chisquare(2,size=grayscale.size) 
 sum_matrix = grayscale + noise_matrix
 cv2.normalize(sum_matrix,sum_matrix, 0, 255, cv2.NORM_MINMAX, dtype=-1)
 sum_matrix = sum_matrix.astype(np.uint8)
 show_image(sum_matrix)
 plothist(sum_matrix,noise_matrix,grayscale)


def exponential(grayscale):
 noise_matrix=np.random.exponential(5,size=(512,819)) 
 sum_matrix = grayscale + noise_matrix
 cv2.normalize(sum_matrix,sum_matrix, 0, 255, cv2.NORM_MINMAX, dtype=-1)
 sum_matrix = sum_matrix.astype(np.uint8)
 show_image(sum_matrix)
 plothist(sum_matrix,noise_matrix,grayscale)


def gamma(grayscale):
 noise_matrix=np.random.gamma(2.,2.,size=(512,819))
 sum_matrix = grayscale + noise_matrix
 cv2.normalize(sum_matrix,sum_matrix, 0, 255, cv2.NORM_MINMAX, dtype=-1)
 sum_matrix = sum_matrix.astype(np.uint8)
 show_image(sum_matrix)
 plothist(sum_matrix,noise_matrix,grayscale)


img = cv2.imread("emma2.jpeg")
# print(img)
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