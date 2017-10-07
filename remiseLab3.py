# -*- coding: utf-8 -*-
"""
Created on Sat Oct 07 14:47:43 2017

@author: Benoit Brizard (1849948) 
"""

import math
import numpy as np
import pylab as pl
from matplotlib import collections  as mc
def integration(f, a, b, N):
    x = np.linspace(a+(b-a)/(2*N), b-(b-a)/(2*N), N)
    fx = f(x)
    area = np.sum(fx)*(b-a)/N
    return area
    
print 'Question 1 : Voir graphiques '
#PV
#Ligne 1
q=float(273)/373
w=float(0.0009)**0.4
vfinal=(q*w)**(1/0.4)
v1= np.linspace(0.00025, vfinal, 1000)
p1=20*8.31*(100+273)/v1
#Ligne  adiab 1
pstart=p1[999]
vstart=v1[999]
cste1=pstart*vstart**1.4
v2=np.linspace(vstart, 0.0009, 1000)
v2_cal=v2**1.4
p2=cste1/v2_cal

#Ligne  isoth 2
q2=float(373)/273
w2=float(0.00025)**0.4
v4=(q2*w2)**(1/0.4)
v3=np.linspace(0.0009, v4, 1000)
p3=20*8.31*(273)/v3

#Last adiab

v5=np.linspace(0.00025, v4, 1000)
v5_cal=v5**1.4
cste2=p1[0]*0.00025**1.4
p4=cste2/v5_cal


fig, ax = pl.subplots()
fig.suptitle('Diagramme P-V')
fig.text(0.5, 0.04, 'Volume ($m^3$)', ha='center')
fig.text(0.04, 0.5, 'Pression (Pa)', va='center', rotation='vertical')
ax.autoscale()

ax.plot(v1,p1)
ax.plot(v2,p2)
ax.plot(v3,p3)
ax.plot(v5,p4)

#TS

I=2*10**-46
pi=math.pi
e=math.e
h=6.62607004*10**-34
N=20*6.02214179*10**23
m=float(0.0280134)/(6.02214179*10**23)
k=1.3806504*10**-23

interieur1=4*pi*e*0.5*k*373
diviseur=(N*h**5)
interieur1_1=float(e*0.00025*4*(pi**2)*I*(m**1.5))/diviseur
part1=2.5*N*math.log(interieur1)
part2=N*math.log(interieur1_1)
S1=k*(part1+part2)


interieur2=4*pi*e*0.5*k*373
interieur2_2=float(e*v1[999]*4*(pi**2)*I*(m**1.5))/(N*h**5)
part3=2.5*N*math.log(interieur2)
part4=N*math.log(interieur2_2)
S2=k*(part3+part4)
deltaS=S2-S1

#segments
lignes = [[(S1, 273), (S1, 373)], [(S1, 373), (S2, 373)], [(S2, 373), (S2, 273)],[(S1, 273), (S2, 273)]]
cmap =(['c', 'b', 'g','r'])
fig1, ax2 = pl.subplots()
fig1.suptitle('Diagramme T-S')
fig1.text(0.5, 0.04, 'Entropie (J/K)', ha='center')
fig1.text(0.04, 0.5, 'Temperature (K)', va='center', rotation='vertical')

lc = mc.LineCollection(lignes,colors=cmap,  linewidths=2)
ax2.add_collection(lc)
ax2.autoscale()
print 'Question 2 '
f1 = lambda x: 20*8.31*(100+273)/x
i1= integration(f1,0.00025,vfinal,100)

f2 = lambda x: cste1/(x**1.4)
i2= integration(f2,vfinal,0.0009,100)

f3 = lambda x: 20*8.31*(273)/x
i3= integration(f3,v4,0.0009,100)

f4 = lambda x: cste2/(x**1.4)
i4= integration(f4,0.00025,v4,100)

wnet=i1+i2-i3-i4
efficiency=wnet/i1
eff_carnot=1-float(273)/373
print 'Rendement théorique de Carnot : ' , eff_carnot
print 'Rendement de la machine selon les diagrammes de phase : ' , efficiency
print "Il est clair que les deux résultats sont les mêmes, puisque le cycle étudié est un cycle de Carnot, les deux rendements concordent forcément."