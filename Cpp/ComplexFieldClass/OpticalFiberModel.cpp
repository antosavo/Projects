/*
This code simulates an optical communication fiber using the customized class of complex vectors called ComplexField.h. 
The output files are the intensity and the spectrum of the input wave.
*/

#include "ComplexField.h"     //ComplexField Module
#include <iostream>  //support  to write and read from console
#include <fstream>   //support to write and read files
#include <cmath>     //support for mathematical functions
#include <cstdlib>   //support for rand, system ....
using namespace std;

int main()
{
    //Optical Fiber parameters
    double beta2= -2.6*pow(10,-4);
    double beta3= 3.5*pow(10,-5);
    double gamma= 0.01;
    
    int i, q, m=14;   
    int nt= pow(2,m);   //2^m=16384 is the number of FFT points
    double tm= 160;     //Time window in ps
    double dt= tm/(nt-1);   //t increment
    double t, to=0;   //Time variable and initial time

    double xm= 40; //Fiber length in m
    int nx= 5*pow(10,3);  //Number of points along the fiber
    double dx= xm/(nx-1); //x increment
    
    double Z[5]; //Check points
    double step=xm/4;
    double I, f, L, x_max, x_final=0;
    
    Z[0]=0;
    Z[1]=1*step;
    Z[2]=2*step;
    Z[3]=3*step; 
    Z[4]=4*step;

    ComplexField<16384> U;  //Optical field
    ComplexField<16384> N,V,B;  //Intermediate parameters
    double Po= 1.0; //Initial power
    double Oo= -10.0;   //Initial frequency
    double To= sqrt((-beta2-beta3*Oo)/(gamma*Po));  //Initial duration
    
    char Intensity_name[50]; //Intensity file name
    char Spectrum_name[50]; //Spectrum file name

    //Initializing the optical field
    
    for(i=0; i<nt; i++)  
    {  
        t=(i-0.5*(nt-1))*dt;
        U.real[i]=(sqrt(Po)/cosh((t-to)/To))*cos(-Oo*(t-to)) ; // real part of U
        U.imag[i]=(sqrt(Po)/cosh((t-to)/To))*sin(-Oo*(t-to)) ; // imaginary part of U
    }
    
    //Linear part of the propagator V=exp(dx*L)

    for(i=0; i<nt; i++)  
    {
        if(i<(nt/2)){f=i/(dt*nt);}
        else{f= (-nt+i)/(dt*nt);}
    
        L=(beta2/2)*(2*M_PI*f)*(2*M_PI*f)+(beta3/6)*(2*M_PI*f)*(2*M_PI*f)*(2*M_PI*f);

        V.real[i]=cos(dx*L);
        V.imag[i]=sin(dx*L);
      }
    
    //Propagation in space the optical field
    
    for(q=0; q<5; q++)
    {

        x_max=Z[q];  

        cout << "x = " << x_max << "\n";
        
         while(x_final<=x_max)
         {
             x_final+=dx;
             
             //N=c|U|^2
             N=gamma*U*U.T();
             
             //FFT of U(t,x)
             FFT(U,1);
             
             //B=V*U;
             B=V*U;
             
             //IFFT of V
             FFT(B,-1);
             
             //U at position x + dx
             U=ExpI(N*dx)*B;
         }
        
        //Save  Intensity data
        
        sprintf(Intensity_name,"Intensity_%i.dat",q);
        ofstream File_Intensity(Intensity_name); //open output file
        
        for(i=0; i<nt; i++)  
        {
            t=(i-0.5*(nt-1))*dt;

            I=U.real[i]*U.real[i] + U.imag[i]*U.imag[i];

            File_Intensity << t << "\t" << I << "\n";
        }

        File_Intensity.close();
        
        //Save Spextrum data
        
        sprintf(Spectrum_name,"Spectrum_%i.dat",q);
        ofstream File_Spectrum(Spectrum_name);
        
        FFT(U,1);

        for(i=0; i<nt; i++)  
        {
            if(i<(nt/2)){f=i/(dt*nt);}
            else{f= (-nt+i)/(dt*nt);}  
    
            File_Spectrum << 2*M_PI*f << "\t" << U.real[i] << "\t" << U.imag[i] << "\n";
        }
        
        FFT(U,-1);

        File_Spectrum.close();
        
    }
    
    system("python Plot_Intensity.py"); //Intensity plot script
    system("python Plot_Spectrum.py");  //Spectrum plott script

    return 0;
}
