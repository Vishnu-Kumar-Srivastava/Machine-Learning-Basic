//This code is made by Vishnu Kumar Srivastava
#include<bits/stdc++.h>
#include<vector>
using namespace std;
int main()
{
   vector<float> x1={2.75,2.5,2.25,2,2,2,1.75,1.75};
   vector<float> x2={5.3,5.3,5.5,5.7,5.9,6,5.9,6.1};
   vector<float> y={1464,1394,1159,1130,1075,1047,965,719};
   float b0=0;
   float b1=0;
   float b2=0;
   float tempo=0;
   float tempi=0;
   float tempv=0;
   float tempPrev=500;
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
      float sigmav=0;
      for(int i=0;i<x1.size();i++)
      {
         sigmaO=sigmaO+b0+b1*x1[i]+b2*x2[i]-y[i];
      }
      tempPrev=tempo;
      tempo=b0-(0.01/x1.size())*sigmaO;

      for(int i=0;i<x1.size();i++)
      {
         sigmai=sigmai+(b0+b1*x1[i]+ b2*x2[i]-y[i])*x1[i];
      }
      tempi=b1-(0.01/x1.size())*sigmai;

      for(int i=0;i<x1.size();i++)
      {
         sigmav=sigmav+(b0+b1*x1[i]+ b2*x2[i]-y[i])*x2[i];
      }
      tempv=b1-(0.01/x1.size())*sigmav;
      cout<<"temp0: "<<tempo<<endl;
      cout<<"tempi: "<<tempi<<endl;
      cout<<"tempv: "<<tempv<<endl;
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
      cout<<"Enter the no. of iterations you want to perform: "<<endl;
      int a;
      cin>>a;
      while(a--)
      {
         count++;
      float sigmaO=0;
      float sigmai=0;
      float sigmav=0;
      for(int i=0;i<x1.size();i++)
      {
         sigmaO=sigmaO+b0+b1*x1[i]+b2*x2[i]-y[i];
      }
      tempPrev=tempo;
      tempo=b0-(0.01/x1.size())*sigmaO;

      for(int i=0;i<x1.size();i++)
      {
         sigmai=sigmai+(b0+b1*x1[i]+ b2*x2[i]-y[i])*x1[i];
      }
      tempi=b1-(0.01/x1.size())*sigmai;

      for(int i=0;i<x1.size();i++)
      {
         sigmav=sigmav+(b0+b1*x1[i]+ b2*x2[i]-y[i])*x2[i];
      }
      tempv=b1-(0.01/x1.size())*sigmav;
      cout<<"temp0: "<<tempo<<endl;
      cout<<"tempi: "<<tempi<<endl;
      cout<<"tempv: "<<tempv<<endl;
      // cout<<"temp prev: "<<tempPrev<<endl;
      b0=tempo;
      b1=tempi;
      }
   }
    
    float costsum=0;
    float costsum1=0;
    for(int i=0;i<x1.size();i++)
    {
      costsum=y[i]-b0-b1*x1[i]-b2*x2[i];
      // cout<<"costsum is : "<<costsum<<endl;
      costsum1=costsum1+pow(costsum,2);
      // cout<<"costsum1 is : "<<costsum1<<endl;
    }
    float cost=costsum1/x1.size();
    cout<<"Minimized cost is : "<<cost<<endl;
}