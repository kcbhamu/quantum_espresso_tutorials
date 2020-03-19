EFermi = -0.868 # from dos, scf, or nscf outputs, in terms of [eV]
bandfile = 'espresso.band1.gnu'

kpaths=[]
energies=[]
for line in open(bandfile, 'r'):
    if (len(line.split()) < 2):
        continue
    values = [float(s) for s in line.split()]
    kpaths.append(values[0])
    energies.append(values[1])

VBMenergies=[]
VBMkpaths=[]
CBMenergies=[]
CBMkpaths=[]
for i in range(len(energies)):
    if (energies[i] <= EFermi):
        VBMenergies.append(energies[i])
        VBMkpaths.append(kpaths[i])
    else:
        CBMenergies.append(energies[i])
        CBMkpaths.append(kpaths[i])

print("VBM energy = ",max(VBMenergies), " eV")
print("VBM k-point number and coordinate = ", kpaths.index(VBMkpaths[VBMenergies.index(max(VBMenergies))])+1, " ", VBMkpaths[VBMenergies.index(max(VBMenergies))])
print("CBM energy = ",min(CBMenergies), " eV")
print("CBM k-point number and coordinate = ", kpaths.index(CBMkpaths[CBMenergies.index(min(CBMenergies))])+1, " ", CBMkpaths[CBMenergies.index(min(CBMenergies))])
print("Bandgap energy = ",min(CBMenergies)-max(VBMenergies), " eV")

