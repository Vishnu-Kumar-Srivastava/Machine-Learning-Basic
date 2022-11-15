#This code is made by Vishnu Kumar Srivastava
# Roll no. 102118066
import matplotlib.pyplot as pp
import numpy as num
import pandas as pd
import statistics as st
from sklearn.linear_model import LinearRegression

var=pd.read_csv('Salary_Data.csv')

years=list(var['YearsExperience'])
salary=list(var['Salary'])

means=st.mean(years)
meany=st.mean(salary)
salaryz=max(salary)

nr,dr=0,0
for i in range(len(salary)):
   dr+=(years[i]-means)**2
   nr+=(salary[i]-meany)*(years[i]-means)
b1=nr/dr
b0=meany- means*b1

x_array=num.array(years)   
y_line=b1*x_array+b0

def covariance():
   nr=0
   for i in range(len(salary)):
      nr+=(years[i]-means)*(salary[i]-meany)
   dr=len(salary)-1
   ans=nr/dr

   print("covariance is:",ans)
   print("\n")
   print("The result using inbuilt function is: ")
   arr=num.cov(years,salary)
   print(arr[0][1])

def Karlpearson():
   nr1,dr1=0,0
   dr2=0
   for i in range(len(salary)):
      dr1+=(years[i]-means)**2
      dr2+=(salary[i]-meany)**2
      nr1+=(years[i]-means)*(salary[i]-meany)
      
   dr=dr1*dr2
   dr=dr**0.5

   answer=nr1/dr  
   print("Karl pearson coefficient is:", answer)
   print("\n")
   
   r = num.corrcoef(years, salary)
   print("The result using inbuilt function is :")
   print(r[0][1])

def plot():
   
   pp.scatter(years,salary),
   pp.plot(x_array,y_line),
   pp.xlabel("Years of experience"),
   pp.ylabel("Salary"),
   pp.title("Without using inbuilt functions")
   pp.show()

def inbuilt_Plot():
   data= pd.read_csv('Salary_Data.csv')
   X=data.iloc[:,0].values.reshape(-1,1)
   Y=data.iloc[:,1].values.reshape(-1,1)
   num.cov(X,Y)
   lr= LinearRegression()
   lr.fit(X,Y)
   Y_pred=lr.predict(X)
   pp.scatter(X,Y)
   pp.plot(X,Y_pred,color='red')
   pp.title("Using inbuilt functions")
   pp.xlabel("Years of experience"),
   pp.ylabel("Salary"),
   pp.show()


def regression():
   a=input("Enter the value of x for which you want to find y")
   x=float(a)
   print()
   means=st.mean(years)
   meany=st.mean(salary)

   nr,dr=0,0
   for i in range(len(salary)):
      dr+=(years[i]-means)**2
      nr+=(salary[i]-meany)*(years[i]-means)
   b1=nr/dr
   b0=meany- means*b1
   
   print("b0 is ", b0,"b1 is  ",b1)
   y=b0+b1*(x)
   print("the value of y is", y)
   
def vif():
   means=st.mean(years)
   meany=st.mean(salary)

   nr,dr=0,0
   for i in range(len(salary)):
      dr+=(years[i]-means)**2
      nr+=(salary[i]-meany)*(years[i]-means)
   b1=nr/dr
   b0=0
   for i in range(len(salary)):
      b0+=salary[i]-b1*years[i]
   b0=b0/len(salary) 
   
   xxarray=num.array(years)
   yi= b1*xxarray + b0;
   
   ssr=0
   sst=0
   for i in range(len(yi)):
      ssr+=(yi[i]-meany)**2
      sst+=(salary[i]-meany)**2
      
   R2=ssr/sst

   vif=1/(1-R2)
   print("Vif= ",vif)
   if(vif>5):
      print("the data is highly correlated")
   if(vif<=5):
      print("The data is moderately correlated")
   if(vif==0):
      print("data is not correlated")
      
      
      
print('''Enter 1 if you want the covariance of data\n
Enter 2 if you want the Karl Pearson Coefficient\n

Enter 3 if you want the best fit line plot\n
Enter 4 if you want the value of y\n''')
print('Enter 5 if you want to find vif\n')
    
choice = int(input("Enter any choice given above : "))

if choice == 1:
    covariance()
elif choice == 2:
    Karlpearson()
elif choice == 3:
    plot()
    print("The result using inbuilt function is: ")
    inbuilt_Plot()
elif choice == 4:
   regression()
elif choice ==5:
   vif()
else:
    print("you entered wrong choice")



