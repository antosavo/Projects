#include <iostream>  //support writing
#include <cstdlib>   //support for rand, system ....
#include <ctime>     //support for time(0)
#include <cmath>     //support for mathematical functions
#include <string>    //support for strings
#include <fstream>   //support to write and read files
using namespace std;


int main()
{

  int i,j,k,l,N;
  double dt,T_shell,T,DT;
  double t[100000],I[100000],t_min,t_max;
  double t_temp,I_temp, I_temp_2;
  double Io,Corr[100000];
  
  dt = 0.1;
  
  t_min=0;
  t_max=200;
  
  
  ifstream File1("Amplitude_100.dat"); //open input file
  
  ofstream File2("Autocorr.dat"); //open output file
  
  
  i=0;
  
  Io=0;
  
  while(!File1.eof())
  {
  
  File1 >> t_temp >> I_temp >> I_temp_2; //read from imput file
  
    if(t_temp>=t_min && t_temp<=t_max)
      {
      t[i]=t_temp;
      I[i]=I_temp;  
      Io +=I[i];
    
      //cout << t_temp << "\t" << I_temp <<endl;
         
      N=i;
      i++;
      }
  }
  
  Io=Io/N;
        
        
  File1.close(); 
        
  N=i;

  cout << "n_data=" << N << endl;
  
  
  for(k=0;k<N;k++)
  {
  
  T_shell = k*(t[1]-t[0]); //guscio considerato per g(r) 

  Corr[k] = 0;

  for(i=0; i<N; i++)
  {
      l = i-k;
      
      if(l<0){l=l+N;}
      if(l>=N){l=l-N;}
      
      Corr[k] += (I[i])*(I[l]);
      //if(l>=0 && l<N){Corr[k] += I[i]*I[l];}  
  }

  
  File2 << T_shell << "\t" << Corr[k]/Corr[0] << endl;// write on file

  }
  
  File2.close(); 
  
  //system ("gnuplot Plot.sh"); 
  system ("python Plot.py");
  
  return 0;
 
}
