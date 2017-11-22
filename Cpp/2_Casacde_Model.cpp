#include <iostream>  //support writing
#include <cstdlib>   //support for rand, system ....
#include <ctime>     //support for time(0)
#include <cmath>     //support for mathematical functions
#include <string>    //support for strings
#include <fstream>   //support to write and read files
#include <sstream>   //to convert number to string
using namespace std;

/* Function for the periodic boundary condictions */

double pbc(double pos, double L) {
  
  double z;
  int n;
  
     n=pos/L;
  
     if(pos < 0.0){ z = pos + (1-n)*L;}
       
     else if(pos > L){z = pos-n*L;}
     
     else z = pos;
  
  return z;
  
}

/* Soliton real part */

double Ur(double t, double Po, double fi_0, double t_0, double To, double Op)
{
        double y;
  
        y= (sqrt(Po)/cosh((t-t_0)/To))*cos((fi_0 -Op*(t-t_0))*M_PI/180);
  
        return y;
}

/* Soliton imaginary  part */

double Ui(double t, double Po, double fi_0, double t_0, double To, double Op)
{
        double y;
  
        y= (sqrt(Po)/cosh((t-t_0)/To))*sin((fi_0-Op*(t-t_0))*M_PI/180);
  
        return y;
}


/* Speed */

double V(double beta2, double beta3,double Op, double Tp)
{
        double y;
	
         y= 1.0/(beta2*Op+0.5*beta3*Op*Op+(beta3/(6*Tp*Tp)));
  
        return y;
}


/* Percentage of Power absorbed Q=DE/E*/

double Qgain(double beta3, double phi,double Po1, double Opo1, double Po2, double Opo2, double Epsilon, double r)
{
        double y,Emax;
	double Tpo1,Tpo2,delta1,delta2;
	double beta2,gamma;
	
	beta2 = -2.6*pow(10,-4); // ps^2/m
        //beta3 = 0.6*4.4*pow(10,-6); // ps^3/m
        gamma = 0.01; // 1/Wm
        
        //Epsilon= 0.001;
	
	Tpo1= sqrt((-beta2-beta3*Opo1)/(gamma*Po1)); 
	
	delta1 = beta2*Opo1 + 0.5*beta3*Opo1*Opo1 + beta3/(6*Tpo1*Tpo1);

	
	Tpo2= sqrt((-beta2-beta3*Opo2)/(gamma*Po2));
	
	delta2 = beta2*Opo2 + 0.5*beta3*Opo2*Opo2 + beta3/(6*Tpo2*Tpo2);
	
	Emax = Epsilon/fabs(delta1-delta2);
	
	
	if( Emax < 1.0/(1.0+r) ){ y = Emax*pow(sin(phi*M_PI/360),2 ) ; }
	else{ y = (1.0/(1.0+r))*pow(sin(phi*M_PI/360),2 ) ;}
	
        return y;
}

/* Percentage of Power radiated Q=DE/E*/

double Qrad(double beta3, double phi,double Po1, double Opo1, double Po2, double Opo2, double Epsilon, double r)
{
        double y,Emax;
	double Tpo1,Tpo2,delta1,delta2;
	double beta2,gamma;
	
	beta2 = -2.6*pow(10,-4); // ps^2/m
        //beta3 = 0.6*4.4*pow(10,-6); // ps^3/m
        gamma = 0.01; // 1/Wm
        
        //Epsilon= 0.001;
	
	Tpo1= sqrt((-beta2-beta3*Opo1)/(gamma*Po1)); 
	
	delta1 = beta2*Opo1 + 0.5*beta3*Opo1*Opo1 + beta3/(6*Tpo1*Tpo1);

	
	Tpo2= sqrt((-beta2-beta3*Opo2)/(gamma*Po2));
	
	delta2 = beta2*Opo2 + 0.5*beta3*Opo2*Opo2 + beta3/(6*Tpo2*Tpo2);
	
	Emax = Epsilon/fabs(delta1-delta2);
	
	
	if( Emax < 1.0/(1.0+r) ){ y = r*Emax*pow(sin(phi*M_PI/360),2 ) ; }
	else{ y = (r/(1.0+r))*pow(sin(phi*M_PI/360),2 ) ;}
	
        return y;
}

/*F */

double F_Shift(double P, double gamma, double beta2, double beta3 )
{
        double w_0, dw, y;
	
	dw = pow(5*gamma*P/beta3, 1.0/3.0);
	
	w_0 = -beta2/beta3;
	
	if( dw < w_0 ){ y = 0; }
	else{ y = w_0 - dw;}
	
        return y;
}

/* Time of meeting */

double T(double t1_0, double t2_0, double v1, double v2)
{
        double y;
  
        y= (v1*t1_0 -v2*t2_0)/(v1 -v2);
  
        return y;
}

/* Position of meeting */

double X(double t1_0, double t2_0, double v1, double v2)
{
        double y;
  
        y= v1*v2*(t1_0 -t2_0)/(v1 -v2);
  
        return y;
}

/*Rand exp function*/

double rand_exp(double Po)
{
        double y,x;
	
        y= ((double)rand()/RAND_MAX)*(1/Po);
	
	if(y!=0){x = -Po*log(Po*y);}
        else {x=0;}
  
        return x;
}

double rand_P(double Po)
{
        double y,x;
	double a,b;
	
	a=31.4;
	b=1.687;
	
	Restart:
	
        y= ((double)rand()/RAND_MAX);
	
	if(y!=0){x = a*pow(-log(y),1/b);}
        else {goto Restart;}
  
        return x;
}



/* Main program */

int main(void)
{
	
        double t,dt,seed,T1,T2;
	double x,t_0[10000],v[10000],fi[10000];
        double Dx,Dt,Dxmin,Dxmax,phi,xfinal, Percentage_Epsilon, Epsilon;
        int i,j,j_min,j_max,k,l,m,q,k1,k2,nt,N_run;
        double x_max,Z[6],x_offset,tm,tmi,a,b,density,v_avarage;
	double P1,P2,E1,E2,E,Eo,EI,P[10000],G,Prad,Pmax;
	double Ur_tot[1000000],Ui_tot[1000000],Norm,Erad,I_background;
	double IntensityW[1000000],y,dP,Prob,Prob_PDF[6][10000];
	int c_i,I_N,PDF[6][10000],N_S;
	double beta2,beta3,gamma,To,TI,Op[10000],Tp,OI,Op1,Op2,Tp1,Tp2;
	double r;
	char file_name[15];
	
/* Initial conditions */

//dU/dx = -i(a/2)d^2U/dt^2 + (b/6)d^3U/dt^3 + ic|U|^2 U 

	//srand(time(NULL));
	
	ifstream read_file("Input.dat");

	read_file >> Percentage_Epsilon;
	
	read_file.close();
	
	seed=2;      //seed chosen for random number
	srand(seed);

	Epsilon = 0.0001*Percentage_Epsilon;
	r =0.00;//Percentage radiation
        beta2 = -2.6*pow(10,-4); // ps^2/m
        beta3 = 0.6*4.4*pow(10,-6); // ps^3/m
        gamma = 0.01; // 1/Wm
	
	N_S=1000;//1000; //Number of Solitons
	N_run=1;//250;
	density=5.88; // solitons per ps
	
	//I_N=300; //interval number for PDF
	I_N=6000;
	
	x_offset=100;  //offset due to modulation instability

	Z[0]=100;          //various fiber lengths in meters
	Z[1]=200;
	Z[2]=300;
	Z[3]=500;
	Z[4]=1000;  
        Z[5]=1500;   // maximum fiber length in meters
	
	tmi= N_S/density; //initial time window 
	
	nt=(int)(N_S/100)*10000; //number of time points
        //nt=(int)(N_S/100)*100000; //number of time points

	dt=tmi/(nt-1); //t increment	
	
/* Maximum Power */

        Pmax=1500;
        dP = Pmax/I_N; 

	
/*Initialization*/


for(q=0;q<6;q++)
{
for(c_i = 0; c_i<=I_N; c_i++){PDF[q][c_i] = 0;Prob_PDF[q][c_i]=0;} 
}


/***************************************************/
/******************** N run ************************/
/***************************************************/


for(l=0;l<N_run;l++)
{
       //printf("run=%i\n",l);
       
/*Initial conditions for the N_S solitons*/


        x=0; // Initial position
        I_background=0;
        
        //fprintf(pFile1, "%lf\t",x);

	for(i=0;i<N_S;i++)
	{
	  
	t_0[i]=(i+1)*tmi/(N_S+1);
	
	P[i]= rand_P(0.0);
	
        Op[i] = -0.1*sqrt(-gamma*P[i]/beta2);
	
	Tp=sqrt((-beta2-beta3*Op[i])/(gamma*P[i]));

	v[i]=V(beta2,beta3,Op[i],Tp);
	
	fi[i]=360*((double)rand()/RAND_MAX); //phase
	
	}
	
	//printf("OK\n");

/* MaxPower distribution function (PmaxDF) */
	
  

        
/*************************************************************************/	
/*              Repeated N soliton scattering for x=x_max                */
/*************************************************************************/
     
        j=0;
	xfinal=x_offset;
	
for(q=0;q<6;q++){
  
        x_max=Z[q]; 
	
	
     while(xfinal<=x_max)
{
  
        
	
/* Minimum position of meeting */
        
        Dxmin=1500;
	
	for(i=0; i<N_S-1; i++)
	{
	 Dx= X(t_0[i],t_0[i+1],v[i],v[i+1]);
	 
	    if(Dxmin > Dx && Dx>0) 
	    {
            Dxmin = Dx;
	    k1=i; //the two solitons that meet first
	    k2=i+1; //the two solitons that meet first
            }
        }
        //printf("k1 = %i\tk2=%i\n",k1,k2);
        //printf("OK\n");
        
/* New position and time */
        
	if(Dxmin<10.0) x=Dxmin; //New position referred to the old
	else x=10.0;
	
        xfinal+=x;
	
	//printf("OK\n");
        
        for(i=0;i<N_S;i++)
	{
	t_0[i]=t_0[i]+(x/v[i]);
	t_0[i]=pbc(t_0[i],tmi);
	}
	
/* Scattering between the two solitons */
if(Dxmin<10.0)
{
       
	phi = fi[k1] - fi[k2];
	
	
	P1=P[k1];
	P2=P[k2];
	
	Op1=Op[k1];
	Op2=Op[k2];
	
	Tp1=sqrt((-beta2-beta3*Op[k1])/(gamma*P1));
	Tp2=sqrt((-beta2-beta3*Op[k2])/(gamma*P2));
	
	T1=t_0[k1];
	T2=t_0[k2];
	
	
		
	if(P1<P2)
	{
	  
	Erad=2*P1*Tp1*Qrad(beta3, phi,P2,Op[k2],P1,Op[k1],Epsilon,r);  
	G=Qgain(beta3, phi,P2,Op[k2],P1,Op[k1],Epsilon,r);
	
	E2=2*P2*Tp2 + G*2*P1*Tp1;
	E1=2*P1*Tp1*(1.0 - G - Qrad(beta3, phi,P2,Op[k2],P1,Op[k1],Epsilon,r));
	
	P2= 0.25*gamma*E2*E2/(-beta2-beta3*Op[k2]);
	P1= 0.25*gamma*E1*E1/(-beta2-beta3*Op[k1]);
	
	}
	
	else
	{	  
	
	Erad=2*P1*Tp1*Qrad(beta3, phi,P1,Op[k1],P2,Op[k2],Epsilon,r);
	G=Qgain(beta3, phi,P1,Op[k1],P2,Op[k2],Epsilon,r);
	
	E1=2*P1*Tp1 + G*2*P2*Tp2;
	E2=2*P2*Tp2*(1.0-G -Qrad(beta3, phi,P1,Op[k1],P2,Op[k2],Epsilon,r));
	
	P1= 0.25*gamma*E1*E1/(-beta2-beta3*Op[k1]);
	P2= 0.25*gamma*E2*E2/(-beta2-beta3*Op[k2]);
	
	
	}
	
	
	t_0[k1]=T2;
	t_0[k2]=T1;
	
	P[k1]=P2; //New Power after the scattering
	P[k2]=P1; //New Power after the scattering
	
	Op[k1]=Op2;
	Op[k2]=Op1;
	
	Tp1=sqrt((-beta2-beta3*Op[k1])/(gamma*P[k1]));
	Tp2=sqrt((-beta2-beta3*Op[k2])/(gamma*P[k2]));
	
	v[k1]=V(beta2,beta3,Op[k1],Tp1);
	v[k2]=V(beta2,beta3,Op[k2],Tp2);
	
	fi[k1]=360*((double)rand()/RAND_MAX); //phase
	fi[k2]=360*((double)rand()/RAND_MAX); //phase
	
	//printf("P1=%lf\tP2=%lf\n",P1,P2);
	
	I_background += Erad/tmi;
	
	j+=1;
	
}
	
	
}



	
/* Total wave calculation */

        for(i=0;i<nt;i++)
	{
	  Ur_tot[i]=0;
	  Ui_tot[i]=0;
	  
	}


        for(k=0; k<N_S; k++)
        {
	
	Tp=sqrt((-beta2-beta3*Op[k])/(gamma*P[k]));
	  
	j_min = (int)(t_0[k] - 0.5)/dt;
	    
	if(j_min <0) j_min = 0;
	    
	j_max = (int)(t_0[k] + 0.5)/dt;
	    
	if(j_max >nt) j_max = nt-1 ;
	    
	  
	for(i=j_min; i<=j_max; i++)  
	  {
	
	   t=i*dt;
	   Ur_tot[i] +=Ur(t,P[k],fi[k],t_0[k],Tp,Op[k]);
	   Ui_tot[i] +=Ui(t,P[k],fi[k],t_0[k],Tp,Op[k]);
	
	  }
        }
        
/*Intensity Plot*/        
        
        
        for(i=0; i<nt; i++)  
	{
        t=i*dt;

	IntensityW[i] = I_background + Ur_tot[i]*Ur_tot[i]+  Ui_tot[i]*Ui_tot[i] ;
	}


	
/* Power distribution function (PDF) */
	
	for(i=0; i<nt; i++)       //canalization
 	{
 	c_i = (int)(IntensityW[i]/dP);    // Intensity coordinate with respect to the channeling choice
  	if(c_i<=I_N){PDF[q][c_i] = PDF[q][c_i] + 1;}  // increment of the PDF channel if the Intensity value is in the interval
 	}
 	
	
	
 	for(c_i = 0; c_i <=I_N; c_i++)
        {
	Prob_PDF[q][c_i]=(double)PDF[q][c_i]; //Probability to have a certain Intensity 
        }
}
        


}
        
        
/* Power distribution function (PDF) */

for(q=0;q<6;q++)
        {
	  
	sprintf(file_name,"PDF_%i.dat",(int)Z[q]);
	
	ofstream write_output(file_name);

 	Norm=0;
	
	 for(c_i = 0; c_i <=I_N; c_i++)
        {
	Norm+= dP*Prob_PDF[q][c_i];
        }
	
	
 	for(c_i = 0; c_i <=I_N; c_i++)
        {
	  
	y=(c_i+1)*dP; //Intensity 
	Prob_PDF[q][c_i]=(double)Prob_PDF[q][c_i]/Norm; //Probability to have a certain Intensity 
	write_output << y << "\t" << Prob_PDF[q][c_i] << "\n";
        }
        
	write_output.close();
	
	}

  system ("gnuplot s_PDF_Log.sh"); 
  
  return 0;


}
