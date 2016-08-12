# Fork of CMS Outreach exercise from 2011

See the original readme [here](https://github.com/katilp/OutreachExercise2011)

This repository is a modified version of the original that creates an "output.root" file with data from four lepton events that have been selected as Z candidates based on CMS criteria.  The output.root file contains one TTree, called "t1", which has the following branches:


Lepton1_energy | Lepton1_charge | Lepton1_pt | Lepton1_px | Lepton1_py | Lepton1_pz | Lepton1_phi | Lepton1_eta | Lepton1_flavor | Lepton2_energy | Lepton2_charge | Lepton2_pt | Lepton2_px | Lepton2_py | Lepton2_pz | Lepton2_phi | Lepton2_eta | Lepton2_flavor | Lepton3_energy | Lepton3_charge | Lepton3_pt | Lepton3_px | Lepton3_py | Lepton3_pz | Lepton3_phi | Lepton3_eta | Lepton3_flavor | Lepton4_energy | Lepton4_charge  | Lepton4_ | Lepton4_px | Lepton4_py | Lepton4_pz | Lepton4_phi | Lepton4_eta | Lepton4_flavor
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- 

The "Lepton#_flavor" attribute is an integer that is either 1 or 2. A lepton with flavor value = 1 represents a Muon, and a value of 2 represents an electron.

To create the CMSSW environment on an lxplus server, use the following commands:

```
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh

scramv1 list CMSSW
scramv1 project CMSSW CMSSW_5_3_32
```

On all CMSSW devices, before running this program you must run the following commands:

```
cd CMSSW_5_3_32
cmsenv
```

After you've successfully created the environment, to run the analyzer:

```
git clone https://github.com/alkaplan/OutreachExercise2011
scram b
cd src/OutreachExercise2011/DecaysToLeptons/run/
ipython run.py
```

Currently the `sources.py` file includes sources from [data set 231](http://opendata.cern.ch/record/231), however you can also add files from [data set 230](http://opendata.cern.ch/record/230) and simply add them to the file in the same format. 

Hopefully this will be useful in extracting data from future four lepton files and making them usable documents for Jupyter notebooks and other projects.