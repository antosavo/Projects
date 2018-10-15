#include <cmath>
using namespace std;

template <int N>
class ComplexField {
    public:
    double real[N]; //object
    double imag[N];
    int length(); //method
    double modulus();
};


template <int N>
int ComplexField<N>::length() 
{ return N;}


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


template <int N>
double Norm(ComplexField<N> v)
{
    double norm_val, sum = 0.0;
    for (int i=0; i<N; i++)
    {
        sum += pow(v.real[i], 2)+pow(v.imag[i], 2);
    }
    norm_val = pow(sum, 1.0/2.0);
    return norm_val;
}