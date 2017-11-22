/*FFT*/

#include <iostream>  //support writing
#include <cstdlib>   //support for rand, system ....
#include <ctime>     //support for time(0)
#include <cmath>     //support for mathematical functions
#include <string>    //support for strings
#include <fstream>   //support to write and read files
using namespace std;

/* Definition of a function that substituting the function with its
   Fast Fourier Transform (FFT) */


void FFT(double fr[], double fi[], int m, int isign) 
{
  
  int n,nh,np,k,i,j,p,q,r; 
  double w,u,v;
  double f1,f2;
  
  // fr[] function real part
  // fi[] function imaginary part

  np = pow(2, m); //number of complex numbers

  n=np;

  nh = n/2;

/* Rearrange the data to the bit-reversed order */
  k = 1;
  for (i=0; i<n-1; i++) {
  if (i < k-1) {
  f1 = fr[k-1];
  f2 = fi[k-1];
  fr[k-1] = fr[i];
  fi[k-1] = fi[i];
  fr[i] = f1;
  fi[i] = f2;
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
  f1 = fr[r]*u-fi[r]*v;
  f2 = fr[r]*v+fi[r]*u;
  fr[r] = fr[q]-f1;
  fr[q] += f1;
  fi[r] = fi[q]-f2;
  fi[q] += f2;
  }
  }
  }
}
