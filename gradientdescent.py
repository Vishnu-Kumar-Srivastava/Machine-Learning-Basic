#this code is made by Vishnu Kumar Srivastava
import matplotlib.pyplot as pp
import numpy as num
x=[2,3,5,13,8,16,11,1,9]
y=[15000,28000,42000,64000,50000,90000,58000,8000,54000]

count=0
tempo=0
tempPrev=500
b0=0
b1=0
i=int(input("Enter  0 if you want to enter the amount of iterations otherwise for most efficient cost enter 1: "))
if i:
   while (abs(tempo-tempPrev)>0.01):
      
      count=count+1
      sigmaO=0
      sigmai=0
      for i in range(len(x)):
         sigmaO=sigmaO+b0+b1*x[i]-y[i]
   
      tempPrev=tempo 
      tempo=b0-(0.01/len(x))*sigmaO

      for i in range(len(x)):
         sigmai=sigmai+(b0+b1*x[i]-y[i])*x[i]
      
      tempi=b1-(0.01/len(x))*sigmai;
      print("tempo :",tempo)
      print("tempi ",tempi)
      print("temp prev: ",tempPrev)
      
      if (abs(tempo-tempPrev)<=0.01):
      
         print("Convergence achieved at iteration: ",count)
         break
      
      b0=tempo
      b1=tempi
      
   
else:
   
   print("enter the amount of iterations you want to perform: ")
   a=int(input())
   
   while a :
      a=a-1
      count=count+1
      sigmaO=0
      sigmai=0
      for i in range(len(x)):
      
         sigmaO=sigmaO+b0+b1*x[i]-y[i]
      
      tempPrev=tempo;
      tempo=b0-(0.01/len(x))*sigmaO

      for i in range(len(x)):
         sigmai=sigmai+(b0+b1*x[i]-y[i])*x[i]

      tempi=b1-(0.01/len(x))*sigmai
      print("temp0: ",tempo)
      print("tempi: ",tempi)
      
      #cout<<"temp prev: "<<tempPrev<<endl;
      if (abs(tempo-tempPrev)<=0.01):
      
         print("Convergence achieved at iteration: ",count)
         break;
      
      
      b0=tempo
      b1=tempi
      
   
    
print("b0 is : ",b0)
print("b1 is : ",b1)
costsum=0;
costsum1=0;
for i in range(len(x)):

   costsum=y[i]-b0-b1*x[i];
   #print("costsum is : ",costsum)
   costsum1=costsum1+pow(costsum,2);
   #print("costsum1 is : ",costsum1)

cost=costsum1/len(x);
print("Minimized cost is : ",cost)


x_array=num.array(y)   
y_line=b1*x_array+b0
pp.scatter(y,x),
pp.plot(x_array,y_line),
pp.xlabel("Years of experience"),
pp.ylabel("Salary"),
pp.title("Without using inbuilt functions")
pp.show()