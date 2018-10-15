/* Split step Fourier Method */

/* This code solves the NLS equation with the split-step method
   
dU/dx = -i(a/2)d^2U/dt^2 + (b/6)d^3U/dt^3 + ic|U|^2 U  */

#include "FFT.h"     //FFT Module
#include <iostream>  //support  to write and read from console
#include <fstream>   //support to write and read files
#include <cmath>     //support for mathematical functions
#include <cstdlib>   //support for rand, system ....
using namespace std;

   
 /* Solving dU/dx = -i(a/2)d^2U/dt^2 + (b/6)d^3U/dt^3 + ic|U|^2 U  */

int main()
{
        
double x,t,f;
double dx,dt;
int i,j,nx,nt,m,q,r,kmax1;
double beta2,beta3,gamma,U0,I,Imax1,Z[5],step;
double Ur[100000],Ui[100000],Vr[100000],Vi[100000];
double N[100000],L,Br,Bi,Ar,Ai,Percentage_beta3;
double xm,tm,xfinal,x_max,delta;
double Po1,Tpo1,Opo1,to1,E,H,t_avarage1,Smax,fmax,Opmax;
double P1,Tp1,Op1,Ep1;

char Intensity_name[50];
char Spectrum_name[50];

/* dU/dx = -i(a/2)d^2U/dt^2 + (b/6)d^3U/dt^3 + ic|U|^2 U  */

       

ifstream File_Input("Input.dat"); //open input file

File_Input >> Po1; //Reading parameters from input file

Percentage_beta3=1.0;

beta2= -2.6*pow(10,-4);
beta3= Percentage_beta3*3.5*pow(10,-5);
gamma= 0.01;


tm= 160;  // time window in ps
m = 14; 
nt= pow(2,m); //number of time points for the FFT
dt= tm/(nt-1); //t increment
to1=0;

xm= 40; //40.0/delta;    // fiber length in m
nx= pow(10,3);  // number of points along the fiber
dx= xm/(nx-1); //x increment
xfinal=0;
step=xm/4;

Z[0]=0;
Z[1]=1*step;
Z[2]=2*step;
Z[3]=3*step; 
Z[4]=4*step;

Opo1= 0;

Tpo1= sqrt((-beta2-beta3*Opo1)/(gamma*Po1)); 

ofstream File_Quasisoliton("Quasisoliton.dat"); //open output file


/*Initializing Wave values on position x=0 */


for(i=0; i<nt; i++)  
  {  
  t=(i-0.5*(nt-1))*dt;

  Ur[i]=(sqrt(Po1)/cosh((t-to1)/Tpo1))*cos(-Opo1*(t-to1)) ; // real part of U
  Ui[i]=(sqrt(Po1)/cosh((t-to1)/Tpo1))*sin(-Opo1*(t-to1)) ;  // imaginary part of U
  }

/* Calculation of the wave for each positions */

for(q=0;q<5;q++)
  {
  
  x_max=Z[q];  

  cout << "x = " << x_max << "\n";


  while(xfinal<=x_max)
    {

    xfinal+=dx;

 
 /* N=ic|U|^2 */

    for(i=0; i<nt; i++)  
      {
      N[i]=gamma*Ur[i]*Ur[i]+gamma*Ui[i]*Ui[i];
      }
  
/* FFT of U(t,x) */
  
    FFT(Ur,Ui,m,1);

/* V=exp(dx*L)*FFT(U)=B*FFT(U) */

    for(i=0; i<nt; i++)  
      {
      //f=i/(dt*nt);
      if(i<(nt/2)){f=i/(dt*nt);}
      else{f= (-nt+i)/(dt*nt);}
    
      L=(beta2/2)*(2*M_PI*f)*(2*M_PI*f)+(beta3/6)*(2*M_PI*f)*(2*M_PI*f)*(2*M_PI*f);

      Br=cos(dx*L);
      Bi=sin(dx*L);
    
      Vr[i]=Ur[i]*Br-Ui[i]*Bi;
      Vi[i]=Ui[i]*Br+Ur[i]*Bi;
      }

/* IFFT of V */

    FFT(Vr,Vi,m,-1);

    for(i=0; i<nt; i++)  
      {
      //t=i*dt;
      Vr[i] /=nt;
      Vi[i] /=nt;
      }


/* U(x+dx)=exp(dx*N)*IFFT(V)=A*IFFT(V) */

    for(i=0; i<nt; i++)  
      {
      Ar=cos(dx*N[i]);
      Ai=sin(dx*N[i]);
      
      Ur[i]=Vr[i]*Ar-Vi[i]*Ai;
      Ui[i]=Vi[i]*Ar+Vr[i]*Ai;
      }

    }


/* Intensity and Amplitude */

  r=250*q;


  sprintf(Intensity_name,"Intensity_%i.dat",q);

  ofstream File_Intensity(Intensity_name); //open output file

  E=0;
  H=0;

//First soliton P1, T1, to1

  t_avarage1=0;
  Imax1=0;

  for(i=0; i<nt; i++)  
    {
    t=(i-0.5*(nt-1))*dt;

    I=Ur[i]*Ur[i]+Ui[i]*Ui[i];

    E+=I*dt;

    if(I>=Imax1){Imax1=I;kmax1=i;}

    File_Intensity << t << "\t" << I << "\n";
    }

  File_Intensity.close();

  t_avarage1=(kmax1-0.5*(nt-1))*dt;

  P1=Imax1;

  Ep1=0;

  for(i=0; i<nt; i++)  
    {
    t=(i-0.5*(nt-1))*dt;
    if(t>=(t_avarage1-1) && t<=(t_avarage1+1)){I=Ur[i]*Ur[i]+Ui[i]*Ui[i]; Ep1+=I*dt;}
    }

  Tp1=Ep1/(2*P1);

  Op1= -(beta2+gamma*P1*Tp1*Tp1)/beta3;

/*Spextrum*/

/* FFT of U(t,x) */
  
  FFT(Ur,Ui,m,1);

  sprintf(Spectrum_name,"Spectrum_%i.dat",q);

  ofstream File_Spectrum(Spectrum_name);

  Smax=0;

  for(i=0; i<nt; i++)  
    {
    if(i<(nt/2)){f=i/(dt*nt);}
    else{f= (-nt+i)/(dt*nt);}  
    
    I=Ur[i]*Ur[i]+Ui[i]*Ui[i];
    
    if(I>=Smax){Smax=I;kmax1=i;}
    
    File_Spectrum << 2*M_PI*f << "\t" << Ur[i] << "\t" << Ui[i] << "\n";
    }

  if(kmax1<(nt/2)){fmax=kmax1/(dt*nt);}
  else{fmax= (-nt+kmax1)/(dt*nt);}  

  Opmax=fmax*2*M_PI;

  File_Spectrum.close();


/*Quasisoliton Parameters*/

  File_Quasisoliton << q*step << "\t " << t_avarage1 << "\t " << E << "\t " << P1 << "\t " << Ep1 << "\t " << Tp1 << "\t " << Op1 << "\n";


/*Inverse FFT*/

  FFT(Ur,Ui,m,-1);


  for(i=0; i<nt; i++)  
    {
    Ur[i] /=nt;
    Ui[i] /=nt;
    }


  }


File_Quasisoliton.close();

system ("gnuplot s_Intensity.sh"); //gnuplot script
system ("gnuplot s_Spectrum.sh"); //gnuplot script

return 0;

}
