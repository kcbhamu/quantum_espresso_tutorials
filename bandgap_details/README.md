# Extract bandgap details from band gnu output
The script gets the band gnu output of quantum espresso and the Fermi energy and outputs the following details:

* VBM energy
* VBM kpath number and coordinate
* CBM energy
* CBM kpath number and coordinate
* Bandgap energy

Just open the  `bandgap_details.py` file and edit the first two lines. 
```python
EFermi = -0.868 # from dos, scf, or nscf outputs, in terms of [eV]
bandfile = 'espresso.band1.gnu'
```

Now run the code in a terminal

![](files/sample_run.png)
