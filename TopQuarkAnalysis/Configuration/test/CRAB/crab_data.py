[CMSSW]
lumi_mask=Cert_132440-144114_7TeV_StreamExpress_Collisions10_JSON_v3.txt
output_file=JetAll_DATA_DPhi.root
total_number_of_lumis=-1
pset=jet_dphianalyze_cfg.py
lumis_per_job=100
datasetpath=/MinimumBias/Run2010A-Jun14thReReco_v2/RECO

[USER]
ui_working_dir=MyFirstDataRun_20Oct10
check_user_remote_dir = 1
copy_data=1
user_remote_dir=/user/m/mashah/Data20Oct10
storage_element=srm-cms.cern.ch
return_data=0
email=mashah@cern.ch
storage_path=/srm/managerv2?SFN=/castor/cern.ch

[CRAB]
cfg=crabData.crab
scheduler=glite
jobtype=cmssw
use_server=1

~

