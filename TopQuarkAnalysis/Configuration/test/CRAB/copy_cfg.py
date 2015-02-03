import FWCore.ParameterSet.Config as cms

process = cms.Process("COPY")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(20000) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring("")
)
process.copyAll = cms.OutputModule("PoolOutputModule",
	 fileName = cms.untracked.string("WJetsToLNu_TuneZ2_7TeV.root")	
#	 fileName = cms.untracked.string("ZZ.root")
#	 fileName = cms.untracked.string("WW.root")
 )
process.out = cms.EndPath(process.copyAll) 

