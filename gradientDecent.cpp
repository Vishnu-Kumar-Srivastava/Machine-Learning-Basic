//This code is made by Vishnu Kumar Srivastava
#include<bits/stdc++.h>
#include<vector>
using namespace std;
int main()
{
   vector<int>x={2,3,5,13,8,16,11,1,9};
   vector<int>y ={15000,28000,42000,64000,50000,90000,58000,8000,54000};
   float b0=0;
   float b1=0;
   float tempo=0;
   float tempi=0;
   float tempPrev=500; //initially to run the while loop.
   int count=0;
   cout<<"Enter  0 if you want to enter the amount of iterations otherwise for most efficient cost enter 1: "<<endl;
   int t;
   cin>>t;
   if(t)
   {
       while((abs(tempo-tempPrev)>0.01))
      {
         count++;
         float sigmaO=0;
         float sigmai=0;
         for(int i=0;i<x.size();i++)
         {
            sigmaO=sigmaO+b0+b1*x[i]-y[i];
         }
         tempPrev=tempo; //here the value gets over written. 
         tempo=b0-(0.01/x.size())*sigmaO;

         for(int i=0;i<x.size();i++)
         {
            sigmai=sigmai+(b0+b1*x[i]-y[i])*x[i];
         }
         tempi=b1-(0.01/x.size())*sigmai;
         cout<<"temp0: "<<tempo<<endl;
         cout<<"tempi: "<<tempi<<endl;
         // cout<<"temp prev: "<<tempPrev<<endl;
         if(abs(tempo-tempPrev)<=0.01)
         {
            cout<<"Convergence achieved at iteration: "<<count<<endl;
            break;
         }
         b0=tempo;
         b1=tempi;
      }
   }
   else
   {
      cout<<"enter the amount of iterations you want to perform: "<<endl;
      int a;
      cin>>a;
       while(a--)
      {
         count++;
         float sigmaO=0;
         float sigmai=0;
         for(int i=0;i<x.size();i++)
         {
            sigmaO=sigmaO+b0+b1*x[i]-y[i];
         }
         tempPrev=tempo;
         tempo=b0-(0.01/x.size())*sigmaO;

         for(int i=0;i<x.size();i++)
         {
            sigmai=sigmai+(b0+b1*x[i]-y[i])*x[i];
         }
         tempi=b1-(0.01/x.size())*sigmai;
         cout<<"temp0: "<<tempo<<endl;
         cout<<"tempi: "<<tempi<<endl;
         // cout<<"temp prev: "<<tempPrev<<endl;
         if(abs(tempo-tempPrev)<=0.01)
         {
            cout<<"Convergence achieved at iteration: "<<count<<endl;
            break;
         }
         
         b0=tempo;
         b1=tempi;
      }
   }
    
    cout<<"b0 is : "<<b0<<endl;
    cout<<"b1 is : "<<b1<<endl;
    float costsum=0;
    float costsum1=0;
    for(int i=0;i<x.size();i++)
    {
      costsum=y[i]-b0-b1*x[i];
      // cout<<"costsum is : "<<costsum<<endl;
      costsum1=costsum1+pow(costsum,2);
      // cout<<"costsum1 is : "<<costsum1<<endl;
    }
    float cost=costsum1/x.size();
    cout<<"Minimized cost is : "<<cost<<endl;
}
