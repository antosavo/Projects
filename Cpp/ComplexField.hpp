#include <cmath>
#include <iostream>
using namespace std;

//Defining the class of a complex vectors ComplexField
template <int N>
class ComplexField {
    public:
    double real[N]; //Real part of a complex vector (field)
    double imag[N]; //Imaginary part of a complex vector
    void print();   //Method to print a complex vector
    int length();   //Method that gives the number of components
    double modulus();   //Method that gives the modulus of a complex vector
    ComplexField<N> T(); //Method that gives the complex conjugate of a vector
    ComplexField<N> operator=(ComplexField<N> v);//Assignement = operator
    
    /*Below are defined also the following functions and operators*/
    
    //Sum operator +
    //Difference operator -
    //Multiplication by a constant operator *
    //Product operator *
    //Fast fourier transform function FFT
    //Complex exponential ExpI
};


//Method to print a complex vector
template <int N>
void ComplexField<N>::print()
{
    int i;
    for(i=0; i<N; i++) 
    {
        cout << real[i] << "\t" << imag[i] << "\n";
    }
}


//Method that gives the number of components
template <int N>
int ComplexField<N>::length() 
{ return N;}


//Method that gives the modulus of a complex vector
template <int N>
double ComplexField<N>::modulus() 
{
    double norm_val, sum = 0.0;
    for (int i=0; i<N; i++)
    {
        sum += pow(real[i], 2)+pow(imag[i], 2);
    }
    norm_val = pow(sum, 1.0/2.0);
    return norm_val;
}


//Method that gives the complex conjugate of a vector
template <int N>
ComplexField<N> ComplexField<N>::T() 
{
   int i;
   ComplexField<N> w;
   for(i=0; i<N; i++) 
   {
       w.real[i] = real[i];
       w.imag[i] = -imag[i];
   }
   return w;
}


//Assignement = operator
template <int N>
ComplexField<N> ComplexField<N>::operator=(ComplexField<N> v)
{
    int i;
    for(i=0; i<N; i++) 
    {
        real[i] = v.real[i];
        imag[i] = v.imag[i];
    }
    return *this;
}


//Sum operator +
template <int N>
ComplexField<N> operator+(ComplexField<N> v1, ComplexField<N> v2)
{
   int i;
   ComplexField<N> w;
   for(i=0; i<N; i++) 
   {
       w.real[i] = v1.real[i] + v2.real[i];
       w.imag[i] = v1.imag[i] + v2.imag[i];
   }
   return w;
}


//Difference operator -
template <int N>
ComplexField<N> operator-(ComplexField<N> v1, ComplexField<N> v2)
{
   int i;
   ComplexField<N> w;
   for(i=0; i<N; i++) 
   {
       w.real[i] = v1.real[i] - v2.real[i];
       w.imag[i] = v1.imag[i] - v2.imag[i];
   }
   return w;
}


//Multiplication by a constant operator * (1)
template <int N>
ComplexField<N> operator*(ComplexField<N> v, double a)
{
   int i;
   ComplexField<N> w;
   for(i=0; i<N; i++) 
   {
       w.real[i] = a*v.real[i];
       w.imag[i] = a*v.imag[i];
   }
   return w;
}

//Multiplication by a constant operator * (2)
template <int N>
ComplexField<N> operator*(double a, ComplexField<N> v)
{
   int i;
   ComplexField<N> w;
   for(i=0; i<N; i++) 
   {
       w.real[i] = a*v.real[i];
       w.imag[i] = a*v.imag[i];
   }
   return w;
}


//Product operator *
template <int N>
ComplexField<N> operator*(ComplexField<N> v1, ComplexField<N> v2)
{
   int i;
   ComplexField<N> w;
   for(i=0; i<N; i++) 
   {
       w.real[i] = v1.real[i]*v2.real[i] - v1.imag[i]*v2.imag[i];
       w.imag[i] = v1.real[i]*v2.imag[i] + v1.imag[i]*v2.real[i];
   }
   return w;
}


//Fast fourier transform function (FFT)
//if isign=1 the function performs the FFT
//if isign=-1 the function performs the inverse FFT
template <int N>
void FFT(ComplexField<N>& E, int isign) 
{
  
    int n,nh,k,i,j,p,q,r; 
    double w,u,v;
    double f1,f2;
    int m = log(N)/log(2.0);

    n = N;// pow(2, m) dimension of the complex vector

    nh = n/2;

    /* Rearrange the data to the bit-reversed order */
    k = 1;
    for (i=0; i<n-1; i++) {
        if (i < k-1) {
            f1 = E.real[k-1];
            f2 = E.imag[k-1];
            E.real[k-1] = E.real[i];
            E.imag[k-1] = E.imag[i];
            E.real[i] = f1;
            E.imag[i] = f2;
        }
        j = nh;
        while (j < k) {
            k -= j;
            j /= 2;
        }
        k += j;
    }
    /* Sum up the reordered data at all levels */
    k = 1;
    for (i=0; i<m; i++) {
        w = 0;
        j = k;
        k = 2*j;
        for (p=0; p<j; p++) {
            u = cos(w);
            v = sin(w);
            w += isign*M_PI/j;
  
            for (q=p; q<n; q+=k) {
                r = q+j;
                f1 = E.real[r]*u-E.imag[r]*v;
                f2 = E.real[r]*v+E.imag[r]*u;
                E.real[r] = E.real[q]-f1;
                E.real[q] += f1;
                E.imag[r] = E.imag[q]-f2;
                E.imag[q] += f2;
            }
        }
    }
    
    
    if(isign==-1)for(i=0; i<n; i++)  {
        E.real[i] /=n;
        E.imag[i] /=n;
    }

}


//Complex exponential ExpI
template <int N>
ComplexField<N> ExpI(ComplexField<N> v)
{
   int i;
   ComplexField<N> w;
   for(i=0; i<N; i++) 
   {
       w.real[i] = exp(-v.imag[i])*cos(v.real[i]);
       w.imag[i] = exp(-v.imag[i])*sin(v.real[i]);
   }
   return w;
}