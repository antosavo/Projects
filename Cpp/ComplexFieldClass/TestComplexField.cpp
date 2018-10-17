#include "ComplexField.hpp"     //ComplexField Module
#include <iostream>  //support  to write and read from console
#include <fstream>   //support to write and read files
#include <cmath>     //support for mathematical functions
#include <cstdlib>   //support for rand, system ....
using namespace std;

int main()
{
    ComplexField<2> a,d;
    ComplexField<2> b={{3.0,3.0},{2.5,4.5}};
    double c=4.0;
    
    a.real[0]=2.0;
    a.real[1]=3.0;
    a.imag[0]=2.5;
    a.imag[1]=4.5;

    
    cout << "a=\n"; 
    a.print();
    
    cout << "a.modulus=" << a.modulus() <<"\n";
    cout << "a.length=" << a.length() <<"\n";
    
    cout << "b=\n"; 
    b.print();
    
    a.real[0]=5.0;
    cout << "a=\n";
    a.print();
    
    d=a;
    
    cout << "d=\n";
    d.print();
    
    d.real[0]=15.0;
    cout << "d=\n";
    d.print();
    
    cout << "a=\n";
    a.print();
    
    FFT(a,1);
    cout << "FFT(a)=\n";
    a.print();
    
    FFT(a,-1);
    cout << "IFFT(a)=\n";
    a.print();
    
    cout << "a+b=\n";
    (a+b).print();
    
    cout << "a-b=\n";
    (a-b).print();

    cout << "a*=\n";
    a.T().print();
    
    cout << "a*b=\n";
    (a*b).print();
    
    cout << "a*c=\n";
    (a*c).print();
    
    cout << "c*a=\n";
    (c*a).print();
    
    cout << "ExpI(a)=\n";
    ExpI(a).print(); 
    
}