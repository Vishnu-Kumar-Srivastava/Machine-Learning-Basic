import numpy as np
import pandas
from sklearn import linear_model
def inbuilt(a,b):
    df = pandas.read_csv("python\wook1.csv")
    inbuilt_X = df[['buyer','holiday']]
    inbuilt_Y = df['sales']
    regr = linear_model.LinearRegression()
    regr.fit(inbuilt_X, inbuilt_Y)
    output_Y = regr.predict([[a,b]])
    print(f"Predicted value of Y for given x1 & x2 using inbuilt function is {output_Y}")

X1=[4,5,5,5,3]
X2=[7,6,7,2,2]
Y=[-2.7,4.5,2.5,10.5,6.7]
X1_init=[4,5,5,5,3]
X2_init=[7,6,7,2,2]
Y_init=[-2.7,4.5,2.5,10.5,6.7]
mean_X1=sum(X1)/len(X2)
mean_X2=sum(X2)/len(X2)
mean_Y=sum(Y)/len(X2)
summation_X1=sum(X1)
summation_X2=sum(X2)
summation_Y=sum(Y)
summation_X1_whole_squared=summation_X1**2
summation_X2_whole_squared=summation_X2**2
summation_X1_squared= sum([f*f for f in X1])
summation_X2_squared= sum([f*f for f in X2])
summation_X1_into_X2=sum([f*y for f,y in zip(X1,X2)])
summation_X1_into_Y=sum([f*y for f,y in zip(X1,Y)])
summation_X2_into_Y=sum([f*y for f,y in zip(X2,Y)])
summation_small_x1_squared=(summation_X1_squared)-(summation_X1_whole_squared)/len(X1)
summation_small_x2_squared=(summation_X2_squared)-(summation_X2_whole_squared)/len(X1)
summation_small_x1_into_y=(summation_X1_into_Y)-(summation_X1*summation_Y)/len(X1)
summation_small_x2_into_y=(summation_X2_into_Y)-(summation_X2*summation_Y)/len(X1)
summation_small_x1_into_x2=(summation_X1_into_X2)-(summation_X1*summation_X2)/len(X1)
b1=(summation_small_x2_squared*summation_small_x1_into_y-summation_small_x1_into_x2*summation_small_x2_into_y)/(summation_small_x1_squared*summation_small_x2_squared-(summation_small_x1_into_x2**2))
b2=(summation_small_x1_squared*summation_small_x2_into_y-summation_small_x1_into_x2*summation_small_x1_into_y)/(summation_small_x1_squared*summation_small_x2_squared-(summation_small_x1_into_x2**2))
b0=mean_Y-b1*mean_X1-b2*mean_X2
input_X1=int(input("Enter the value of X1 : "))
input_X2=int(input("Enter the value of X2 : "))
output_Y = b0+b1*input_X1+b2*input_X2
print(output_Y)
inbuilt(input_X1,input_X2)