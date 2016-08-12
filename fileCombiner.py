## This is a file that would theoretically combine multiple root files into one large output file
## I don't really know if it would actually work


from ROOT import TFile, TTree
import ROOT
import array

files = []

#as many of these as you need
file1 = TFile("output.root", "READ")
file2 = TFile("output (1).root", "READ")
file3 = TFile("output (2).root", "READ")

files.append(file1, file2, file3)

fout = TFile( 'fourlepton.root', 'recreate' )
t = TTree( 'Leptons', 'Tree' )

Lepton1_energy = array.array('f',[0])
Lepton1_charge = array.array('f',[0])
Lepton1_pt     = array.array('f',[0])
Lepton1_px     = array.array('f',[0])
Lepton1_py     = array.array('f',[0])
Lepton1_pz     = array.array('f',[0])
Lepton1_phi    = array.array('f',[0])
Lepton1_eta    = array.array('f',[0])
Lepton1_flavor = array.array('i',[0])

Lepton2_energy = array.array('f',[0])
Lepton2_charge = array.array('f',[0])
Lepton2_pt     = array.array('f',[0])
Lepton2_px     = array.array('f',[0])
Lepton2_py     = array.array('f',[0])
Lepton2_pz     = array.array('f',[0])
Lepton2_phi    = array.array('f',[0])
Lepton2_eta    = array.array('f',[0])
Lepton2_flavor = array.array('i',[0])

Lepton3_energy = array.array('f',[0])
Lepton3_charge = array.array('f',[0])
Lepton3_pt     = array.array('f',[0])
Lepton3_px     = array.array('f',[0])
Lepton3_py     = array.array('f',[0])
Lepton3_pz     = array.array('f',[0])
Lepton3_phi    = array.array('f',[0])
Lepton3_eta    = array.array('f',[0])
Lepton3_flavor = array.array('i',[0])

Lepton4_energy = array.array('f',[0])
Lepton4_charge = array.array('f',[0])
Lepton4_pt     = array.array('f',[0])
Lepton4_px     = array.array('f',[0])
Lepton4_py     = array.array('f',[0])
Lepton4_pz     = array.array('f',[0])
Lepton4_phi    = array.array('f',[0])
Lepton4_eta    = array.array('f',[0])
Lepton4_flavor = array.array('i',[0])

t.Branch('Lepton1_energy', Lepton1_energy, 'Lepton1_energy/F')
t.Branch('Lepton1_charge', Lepton1_charge, 'Lepton1_charge/F')
t.Branch('Lepton1_pt',     Lepton1_pt,     'Lepton1_pt/F')
t.Branch('Lepton1_px',     Lepton1_px,     'Lepton1_px/F')
t.Branch('Lepton1_py',     Lepton1_py,     'Lepton1_py/F')
t.Branch('Lepton1_pz',     Lepton1_pz,     'Lepton1_pz/F')
t.Branch('Lepton1_phi',    Lepton1_phi,    'Lepton1_phi/F')
t.Branch('Lepton1_eta',    Lepton1_eta,    'Lepton1_eta/F')
t.Branch('Lepton1_flavor', Lepton1_flavor, 'Lepton1_flavor/I')

t.Branch('Lepton2_energy', Lepton2_energy, 'Lepton2_energy/F')
t.Branch('Lepton2_charge', Lepton2_charge, 'Lepton2_charge/F')
t.Branch('Lepton2_pt',     Lepton2_pt,     'Lepton2_pt/F')
t.Branch('Lepton2_px',     Lepton2_px,     'Lepton2_px/F')
t.Branch('Lepton2_py',     Lepton2_py,     'Lepton2_py/F')
t.Branch('Lepton2_pz',     Lepton2_pz,     'Lepton2_pz/F')
t.Branch('Lepton2_phi',    Lepton2_phi,    'Lepton2_phi/F')
t.Branch('Lepton2_eta',    Lepton2_eta,    'Lepton2_eta/F')
t.Branch('Lepton2_flavor', Lepton2_flavor, 'Lepton2_flavor/I')

t.Branch('Lepton3_energy', Lepton3_energy, 'Lepton3_energy/F')
t.Branch('Lepton3_charge', Lepton3_charge, 'Lepton3_charge/F')
t.Branch('Lepton3_pt',     Lepton3_pt,     'Lepton3_pt/F')
t.Branch('Lepton3_px',     Lepton3_px,     'Lepton3_px/F')
t.Branch('Lepton3_py',     Lepton3_py,     'Lepton3_py/F')
t.Branch('Lepton3_pz',     Lepton3_pz,     'Lepton3_pz/F')
t.Branch('Lepton3_phi',    Lepton3_phi,    'Lepton3_phi/F')
t.Branch('Lepton3_eta',    Lepton3_eta,    'Lepton3_eta/F')
t.Branch('Lepton3_flavor', Lepton3_flavor, 'Lepton3_flavor/I')

t.Branch('Lepton4_energy', Lepton4_energy, 'Lepton4_energy/F')
t.Branch('Lepton4_charge', Lepton4_charge, 'Lepton4_charge/F')
t.Branch('Lepton4_pt',     Lepton4_pt,     'Lepton4_pt/F')
t.Branch('Lepton4_px',     Lepton4_px,     'Lepton4_px/F')
t.Branch('Lepton4_py',     Lepton4_py,     'Lepton4_py/F')
t.Branch('Lepton4_pz',     Lepton4_pz,     'Lepton4_pz/F')
t.Branch('Lepton4_phi',    Lepton4_phi,    'Lepton4_phi/F')
t.Branch('Lepton4_eta',    Lepton4_eta,    'Lepton4_eta/F')
t.Branch('Lepton4_flavor', Lepton4_flavor, 'Lepton4_flavor/I')

for f in files:

	for lept in f:

		Lepton1_energy[0] = lept.Lepton1_energy
    	Lepton1_charge[0] = lept.Lepton1_charge
    	Lepton1_pt[0]     = lept.Lepton1_pt
    	Lepton1_px[0]     = lept.Lepton1_px
    	Lepton1_py[0]     = lept.Lepton1_py
    	Lepton1_pz[0]     = lept.Lepton1_pz
    	Lepton1_phi[0]    = lept.Lepton1_phi
    	Lepton1_eta[0]    = lept.Lepton1_eta
    	Lepton1_flavor[0] = lept.Lepton1_flavor
    	
    	Lepton2_energy[0] = lept.Lepton2_energy
    	Lepton2_charge[0] = lept.Lepton2_charge
    	Lepton2_pt[0]     = lept.Lepton2_pt
    	Lepton2_px[0]     = lept.Lepton2_px
    	Lepton2_py[0]     = lept.Lepton2_py
    	Lepton2_pz[0]     = lept.Lepton2_pz
    	Lepton2_phi[0]    = lept.Lepton2_phi
    	Lepton2_eta[0]    = lept.Lepton2_eta
    	Lepton2_flavor[0] = lept.Lepton2_flavor
    	
    	Lepton3_energy[0] = lept.Lepton3_energy
    	Lepton3_charge[0] = lept.Lepton3_charge
    	Lepton3_pt[0]     = lept.Lepton3_pt
    	Lepton3_px[0]     = lept.Lepton3_px
    	Lepton3_py[0]     = lept.Lepton3_py
    	Lepton3_pz[0]     = lept.Lepton3_pz
    	Lepton3_phi[0]    = lept.Lepton3_phi
    	Lepton3_eta[0]    = lept.Lepton3_eta
    	Lepton3_flavor[0] = lept.Lepton3_flavor
    	
    	Lepton4_energy[0] = lept.Lepton4_energy
    	Lepton4_charge[0] = lept.Lepton4_charge
    	Lepton4_pt[0]     = lept.Lepton4_pt
    	Lepton4_px[0]     = lept.Lepton4_px
    	Lepton4_py[0]     = lept.Lepton4_py
    	Lepton4_pz[0]     = lept.Lepton4_pz
    	Lepton4_phi[0]    = lept.Lepton4_phi
    	Lepton4_eta[0]    = lept.Lepton4_eta
    	Lepton4_flavor[0] = lept.Lepton4_flavor
    	
    	t.Fill()


