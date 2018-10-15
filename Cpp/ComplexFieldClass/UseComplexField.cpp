#include "ComplexField.h"     //ComplexField Module
#include <iostream>  //support  to write and read from console
#include <fstream>   //support to write and read files
#include <cmath>     //support for mathematical functions
#include <cstdlib>   //support for rand, system ....
using namespace std;

int main()
{
    ComplexField<2> a;
    ComplexField<2> b={{2.0,3.0},{2.5,4.5}};
    
    a.real[0]=2.0;
    a.real[1]=3.0;
    a.imag[0]=2.5;
    a.imag[1]=4.5;

    
    cout << a.real[0] << "\n";
    cout << a.real[1] << "\n";
    cout << a.imag[0] << "\n";
    cout << a.imag[1] << "\n";
    cout << Norm(a+b) <<"\n";
    cout << Norm(a) <<"\n";
    cout << a.modulus() <<"\n";
    cout << a.length() <<"\n";
}