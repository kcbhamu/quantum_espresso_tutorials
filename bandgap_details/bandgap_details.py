#!/usr/bin/env python3

import pandas as pd

bandfile = 'espresso.band1.gnu'
nvbands= 13 # number of valence bands, only for insulators

kpaths=[]

for line in open(bandfile, 'r'):
    if (len(line.split()) < 2):
        break
    values = [float(s) for s in line.split()]
    kpaths.append(values[0])
    
df=pd.DataFrame(kpaths, columns=['kpaths'])

bandnumber=0
energies=[]

for line in open(bandfile, 'r'):
    if (len(line.split()) > 1):
        values = [float(s) for s in line.split()]
        energies.append(values[1])
    else:
        bandnumber+=1
        df[bandnumber]=energies
        energies=[]

print("VBM energy = ",max(df[nvbands]), " eV")
print("VBM k-point number and coordinate = ", df[nvbands].idxmax()+1, " ", df['kpaths'].iloc[df[nvbands].idxmax()])
print("CBM energy = ",min(df[nvbands+1]), " eV")
print("CBM k-point number and coordinate = ", df[nvbands+1].idxmin()+1, " ", df['kpaths'].iloc[df[nvbands+1].idxmin()])
print("bandgap=", min(df[nvbands+1])-max(df[nvbands]), 'eV')
