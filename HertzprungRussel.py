# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 21:09:52 2023

@author: Gabriele
"""

import numpy as np
import matplotlib.pyplot as plt
import statistics as stat
import sys

def single_histogram(num,num1,string):
    nb=200
    mask = (age>=num) & (age<num1)    
    counts, xc = np.histogram(MsuH[mask], bins=nb, range=(0.0,5.0))
    counts = counts/sum(counts)
    xbin = xc[:-1]
    for i in range(len(xbin)):
        xbin[i] = (xc[i+1]+xc[i])*0.5
    ax2.hist(xbin, bins=nb, weights=counts, histtype='step', density=True, lw=3, label=string)

#path = input('inserisci path: ')
filename = str(sys.argv[1])
data = np.loadtxt(filename, delimiter=' ', usecols=(0, 1, 4, 8, 12), unpack=True)
MsuH0 = data[0]
m_ini0 = data[1]
mabs0 = data[2]
mb_y0 = data[3]
age0 = data[4]

#Trasforma le liste in arrays
MsuH = np.array(MsuH0)
m_ini = np.array(m_ini0)
mabs = np.array(mabs0)
mb_y = np.array(mb_y0)
age = np.array(age0)

#seleziono le stelle contenute nel file in base all'età
mask = (age>=0.00)&(age<0.50)
mask1 = (age>=0.50)&(age<1.00)
mask2 = (age>=1.00)&(age<1.50)
mask3 = (age>=1.50)&(age<2.00)
mask4 = (age>=2.00)&(age<2.50)
mask5 = (age>=2.50)&(age<3.00)
mask6 = (age>=3.00)&(age<3.50)
mask7 = (age>=3.50)&(age<4.00)
mask8 = (age>=4.00)&(age<4.50)
mask9 = (age>=4.50)&(age<5.00)
mask10 = (age>=5.00)&(age<5.50)
mask11 = (age>=5.50)&(age<6.00)
mask12 = (age>=6.00)&(age<6.50)
mask13 = (age>=6.50)&(age<7.00)
mask14 = (age>=7.00)&(age<7.50)
mask15 = (age>=7.50)&(age<8.00)
mask16 = (age>=8.00)&(age<8.50)
mask17 = (age>=8.50)&(age<9.00)
mask18 = (age>=9.00)&(age<9.50)
mask19 = (age>=9.50)&(age<10.00)
mask20 = (age>=10.00)&(age<10.50)
mask21 = (age>=10.50)&(age<11.00)
mask22 = (age>=11.00)&(age<11.50)
mask23 = (age>=11.50)&(age<12.00)
mask24 = (age>=12.00)&(age<12.50)
mask25 = (age>=12.50)&(age<13.00)
mask26 = (age>=13.00)&(age<13.50)
mask27 = (age>=13.50)&(age<14.00)

mask28 = (age>=0.00) & (age<1.00)
mask29 = (age>=1.00) & (age<5.00)
mask30 = (age>=5.00) & (age<14.00)

fig1, (ax1) = plt.subplots()
fig2, (ax2) = plt.subplots()
fig2, (ax3) = plt.subplots()
ax1.plot(mb_y[mask], mabs[mask], '.', markersize=3, label='0.00 Gyr - 0.50 Gyr')
ax1.plot(mb_y[mask1], mabs[mask1], '.', markersize=3, label='0.50 Gyr - 1.00 Gyr')
ax1.plot(mb_y[mask2], mabs[mask2], '.', markersize=3, label='1.00 Gyr - 1.50 Gyr')
ax1.plot(mb_y[mask3], mabs[mask3], '.', markersize=3, label='1.50 Gyr - 2.00 Gyr')
ax1.plot(mb_y[mask4], mabs[mask4], '.', markersize=3, label='2.00 Gyr - 2.50 Gyr')
ax1.plot(mb_y[mask5], mabs[mask5], '.', markersize=3, label='2.50 Gyr - 3.00 Gyr')
ax1.plot(mb_y[mask6], mabs[mask6], '.', markersize=3, label='3.00 Gyr - 3.50 Gyr')
ax1.plot(mb_y[mask7], mabs[mask7], '.', markersize=3, label='3.50 Gyr - 4.00 Gyr')
ax1.plot(mb_y[mask8], mabs[mask8], '.', markersize=3, label='4.00 Gyr - 4.50 Gyr')
ax1.plot(mb_y[mask9], mabs[mask9], '.', markersize=3, label='4.50 Gyr - 5.00 Gyr')
ax1.plot(mb_y[mask10], mabs[mask10], '.', markersize=3, label='5.00 Gyr - 5.50 Gyr')
ax1.plot(mb_y[mask11], mabs[mask11], '.', markersize=3, label='5.50 Gyr - 6.00 Gyr')
ax1.plot(mb_y[mask12], mabs[mask12], '.', markersize=3, label='6.00 Gyr - 6.50 Gyr')
ax1.plot(mb_y[mask13], mabs[mask13], '.', markersize=3, label='6.50 Gyr - 7.00 Gyr')
ax1.plot(mb_y[mask14], mabs[mask14], '.', markersize=3, label='7.00 Gyr - 7.50 Gyr')
ax1.plot(mb_y[mask15], mabs[mask15], '.', markersize=3, label='7.50 Gyr - 8.00 Gyr')
ax1.plot(mb_y[mask16], mabs[mask16], '.', markersize=3, label='8.00 Gyr - 8.50 Gyr')
ax1.plot(mb_y[mask17], mabs[mask17], '.', markersize=3, label='8.50 Gyr - 9.00 Gyr')
ax1.plot(mb_y[mask18], mabs[mask18], '.', markersize=3, label='9.00 Gyr - 9.50 Gyr')
ax1.plot(mb_y[mask19], mabs[mask19], '.', markersize=3, label='9.50 Gyr - 10.00 Gyr')
ax1.plot(mb_y[mask20], mabs[mask20], '.', markersize=3, label='10.00 Gyr - 10.50 Gyr')
ax1.plot(mb_y[mask21], mabs[mask21], '.', markersize=3, label='10.50 Gyr - 11.00 Gyr')
ax1.plot(mb_y[mask22], mabs[mask22], '.', markersize=3, label='11.00 Gyr - 11.50 Gyr')
ax1.plot(mb_y[mask23], mabs[mask23], '.', markersize=3, label='11.50 Gyr - 12.00 Gyr')
ax1.plot(mb_y[mask24], mabs[mask24], '.', markersize=3, label='12.00 Gyr - 12.50 Gyr')
ax1.plot(mb_y[mask25], mabs[mask25], '.', markersize=3, label='12.50 Gyr - 13.00 Gyr')
ax1.plot(mb_y[mask26], mabs[mask26], '.', markersize=3, label='13.00 Gyr - 13.50 Gyr')
ax1.plot(mb_y[mask27], mabs[mask27], '.', markersize=3, label='13.50 Gyr - 14.00 Gyr')
ax1.set_xlim(-0.1, 1.2)
ax1.set_ylim(8.5, -3.6)
ax1.set_xlabel('b-y')
ax1.set_ylabel('Mv')
ax1.legend(fontsize='xx-small', loc='center right')
ax1.set_title('Hertzprung-Russel diagram')

single_histogram(0.00,1.00,'age under 1 Gyr')
single_histogram(1.00,5.00,'age between 1 Gyr and 5 Gyr')
single_histogram(5.00,14.00,'age over 5 Gyr')
ax2.axvline(x = np.mean(MsuH[mask28]), linestyle='--', label='mean for pop with age under 1 Gyr', alpha=0.5)
ax2.axvline(x = np.mean(MsuH[mask29]), linestyle='--', label='mean for pop with age between 1 Gyr and 5 Gyr', alpha=0.5)
ax2.axvline(x = np.mean(MsuH[mask30]), linestyle='--', label='mean for pop with age over 5 Gyr', alpha=0.5)
ax2.axvline(x = np.median(MsuH[mask28]), linestyle='solid', label='mean for pop with age under 1 Gyr', alpha=0.5)
ax2.axvline(x = np.median(MsuH[mask29]), linestyle='solid', label='mean for pop with age between 1 Gyr and 5 Gyr', alpha=0.5)
ax2.axvline(x = np.median(MsuH[mask30]), linestyle='solid', label='mean for pop with age over 5 Gyr', alpha=0.5)
ax2.set_xlim(0.0, 1.0)
ax2.set_ylim(0.0, 12.0)
ax2.set_xlabel('MsuH')
ax2.set_ylabel('Counts')
ax2.legend(fontsize='small', loc='best')
ax2.set_title('Distribution of MsuH at different ages')
ax2.grid()

ax3.plot(m_ini[mask28], MsuH[mask28], '.', markersize=1.5, label='age under 1 Gyr')
ax3.plot(m_ini[mask29], MsuH[mask29], '.', markersize=1.5, label='age between 1 Gyr and 5 Gyr')
ax3.plot(m_ini[mask30], MsuH[mask30], '.', markersize=1.5, label='age over 5 Gyr')
ax3.set_xlim(0.6, 5.5)
ax3.set_ylim(-0.75, 0.75)
ax3.set_xlabel('m_ini')
ax3.set_ylabel('MsuH')
ax3.legend(loc='best')
ax3.set_title('Distributions per age of MsuH as function of m_ini')
ax3.grid()
plt.show()
