import numpy as np
import scipy as sc
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy
from scipy import special, optimize, integrate, stats
from scipy.optimize import curve_fit


# 0 Parameters for the Nonlinear schrodinger equation that governs my system
# dU/dx = -i(beat2/2)d^2U/dt^2 + (beta3/6)d^3U/dt^3 + i*gamma|U|^2 U 

beta2= -2.6*10**-4
beta3= 3.5*10**-5
gamma= 0.01


Gain = np.zeros(31) #Percentage of energy transferred during the scattering between the two solitons
phase_difference = np.zeros(31) 

for j in range(31): #Iterating over the phase difference between the two solitons 

# 1 Finding the initial power and energy for two solitons

    phase_difference[j]=j*12

    folder = 'phi_%d/'%phase_difference[j]
    
    file_to_read = 'Intensity_10_0.dat'

    #path = 'phi_0/Intensity_10_0.dat'#This is the file for the intensity at 0 meters

    path = folder + file_to_read #This is the file for the intensity at 0 meters

    print 'phase_difference =',phase_difference[j]

    file = open( path , 'r' )

    Time = np.zeros(16384)
    Intensity = np.zeros(16384)

    i=0

    for columns in ( raw.strip().split() for raw in file ):  
        Time[i] = columns[0]
        Intensity[i]= columns[1]
        #print Time[i], Intensity[i]
        i+=1

    file.close()

    dt=Time[1]-Time[0]
    nt =i # Number of points

    #print 'dt=', dt, 'nt =', nt

    #Energy = sum(Intensity)
    #Energy = scipy.integrate.simps(Intensity, Time, axis=-1, even='avg')
    Energy_I = scipy.integrate.simps(Intensity, x=None, dx=dt, axis=-1, even='avg')
    print 'Total Initial Energy =', Energy_I

    Max_Intensity = np.amax(Intensity)
    i_max = np.argmax(Intensity)

    P1_I = Max_Intensity # Initial power first soliton
    t1=(i_max-0.5*(nt-1))*dt # Initial position first soliton

    i_I=i_max-200
    i_F=i_max+200

    Intensity_1 = Intensity[i_I : i_F] # intensity first soliton

    Energy_1_I = scipy.integrate.simps(Intensity_1, x=None, dx=dt, axis=-1, even='avg') # Initial energy first soliton (integral around the first pulse)

    print 'Initial power soliton 1 =', P1_I, 'Initial energy soliton 1 =', Energy_1_I


    Intensity_2 = Intensity[i_F : np.size(Intensity)] # intensity second soliton

    Max_Intensity_2 = np.amax(Intensity_2)

    P2_I = Max_Intensity_2 # Initial power second soliton

    Energy_2_I = Energy_I - Energy_1_I # Initial energy second soliton

    print 'Initial power soliton 2 =', P2_I, 'Initial energy soliton 2 =', Energy_2_I



# 2 Finding the final power and energy for two solitons


    file_to_read = 'Intensity_10_1000.dat'

    path = folder + file_to_read #This is the file for the intensity at 1000 meters

    #path = 'phi_0/Intensity_10_1000.dat' #This is the file for the intensity at 1000 meters

    file = open( path , 'r' )

    i=0

    for columns in ( raw.strip().split() for raw in file ):  
        Time[i] = columns[0]
        Intensity[i]= columns[1]
        i+=1

    file.close()

    Energy_F = scipy.integrate.simps(Intensity, x=None, dx=dt, axis=-1, even='avg')
    print 'Total final Energy =', Energy_F

    Max_Intensity = np.amax(Intensity)
    i_max = np.argmax(Intensity)

    P1_F = Max_Intensity # Final power first soliton
    t1=(i_max-0.5*(nt-1))*dt # Final position first soliton

    i_I=i_max-200
    i_F=i_max+200

    Intensity_1 = Intensity[i_I : i_F] # intensity first soliton

    Energy_1_F = scipy.integrate.simps(Intensity_1, x=None, dx=dt, axis=-1, even='avg') # Final energy first soliton (integral around the first pulse)

    print 'Final power soliton 1 =', P1_F, 'Final energy soliton 1 =', Energy_1_F


    Intensity_2 = Intensity[0 : i_I] # intensity second soliton

    Max_Intensity_2 = np.amax(Intensity_2)

    P2_F = Max_Intensity_2 # Final power second soliton

    Energy_2_F = Energy_F - Energy_1_F # Final energy second soliton

    print 'Final power soliton 2 =', P2_F, 'Final energy soliton 2 =', Energy_2_F


# 3 Finding the energy transferred

    Energy_transfered = Energy_1_F - Energy_1_I 

    Gain[j] = Energy_transfered/Energy_2_I

    print 'Energy transfered =', Energy_transfered, 'Gain =', Gain[j], '\n'


# 4 Finding the the inverse of the group velocities

O_1= -math.sqrt(-gamma*P1_I/beta2) # Main frequency for the soliton 1

T_1= math.sqrt((-beta2-beta3*O_1)/(gamma*P1_I)) # Width for the soliton 1

delta_1 = beta2*O_1 + 0.5*beta3*O_1*O_1 + beta3/(6*T_1*T_1) # Inverse of the group velocity for the soliton 1


O_2= -math.sqrt(-gamma*P2_I/beta2) # Main frequency for the soliton 2

T_2= math.sqrt((-beta2-beta3*O_2)/(gamma*P2_I)) # Width for the soliton 2

delta_2 = beta2*O_2 + 0.5*beta3*O_2*O_2 + beta3/(6*T_2*T_2) # Inverse of the group velocity for the soliton 2

delta_12 = math.fabs(delta_1-delta_2) # difference for the inverse of the group velocity, It is important to calculate the coupling constant between the two solitons

print '\n|delat_1 - delta_2| =', delta_12,'\n'

# 5 Save the the gain calculated in a file

file_2 = open( 'Gain.dat' , 'w' )

for j in range(31): 
    print >> file_2, phase_difference[j], Gain[j]

file_2.close()


# 6 Fitting the energy transferred and finding the coupling constant


def f(x, a, b, c):
    return a + b* np.sin((x-c)*math.pi/360)**2

params, pcov = curve_fit(f, phase_difference, Gain)

print '\n', 'a=', params[0], 'b=', params[1],  'c=', params[2]

plt.clf() # Clear the figure
plt.title('Plot Fit Gain',fontsize=20)
plt.xlabel('$\Delta$$\phi$',fontsize=20)
plt.ylabel('$\Delta$$E_1$/$E_2$',fontsize=20)
plt.xlim([0,360])
plt.plot(phase_difference, Gain, label = 'Data',linestyle='', marker='o', color='g')
plt.plot(phase_difference, f(phase_difference, *params),label = 'Fit',linestyle='--', color='b')
plt.legend()
plt.savefig('Fit.png')

coupling_constant = params[1]*delta_12

file_3 = open( 'Fitting_parameters.dat' , 'w' )

print >> file_3, 'a=', params[0], 'b=', params[1],  'c=', params[2],'\n', 'coupling constant =',coupling_constant

file_3.close()



