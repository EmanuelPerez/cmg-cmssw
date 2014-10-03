import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('analysis')

options.register ('skipEvents',
                  0,
                  VarParsing.multiplicity.singleton,
                  VarParsing.varType.int,
                  "events to skip")

options.parseArguments()

procName="DMtest"

eMax = 100
if options.maxEvents:
    eMax = options.maxEvents


sEvents=0
if options.skipEvents:
    sEvents=options.skipEvents

#discName2='LooseCombinedIsolationDBSumPtCorr3Hits'
discName2='DecayModeFindingNewDMs'
discriminator2="hpsPFTauDiscriminationBy"+discName2

#discName='LooseCombinedIsolationDBSumPtCorr3Hits'
discName='DecayModeFindingNewDMs'
discriminator="hpsPFTauDiscriminationBy"+discName

decayMode = 0

DMname=""
if decayMode == 0:
    DMname="DMall"
elif decayMode == 1:
    DMname="DM1p"
elif decayMode == 2:
    DMname="DM1pX"
elif decayMode == 3:
    DMname="DM3p"

#process definition'
procName=procName+DMname
process = cms.Process(procName)

## MessageLogger
process.load("FWCore.MessageLogger.MessageLogger_cfi")


## Options and Output Report
process.options = cms.untracked.PSet( 
    SkipEvent = cms.untracked.vstring('ProductNotFound'),
    wantSummary = cms.untracked.bool(False) 
    )


## Source
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_1.root'
#        '/store/relval/CMSSW_7_1_0_pre4_AK4/RelValZTT_13/GEN-SIM-RECO/POSTLS171_V1-v2/00000/E8DA9320-52B5-E311-AB3B-0025905A6088.root'

        
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_1.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_10.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_101.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_102.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_103.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_104.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_105.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_106.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_107.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_108.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_109.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_11.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_110.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_111.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_112.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_113.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_114.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_115.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_116.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_117.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_118.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_119.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_12.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_120.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_121.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_122.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_123.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_124.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_125.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_126.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_127.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_128.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_129.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_13.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_130.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_131.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_132.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_133.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_134.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_135.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_136.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_137.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_138.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_139.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_14.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_140.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_141.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_142.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_143.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_144.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_145.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_146.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_147.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_148.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_149.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_15.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_150.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_151.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_152.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_153.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_154.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_155.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_156.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_157.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_158.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_159.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_16.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_160.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_161.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_162.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_163.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_164.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_165.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_166.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_167.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_168.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_169.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_17.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_170.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_171.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_172.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_173.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_174.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_175.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_176.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_177.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_178.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_179.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_18.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_180.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_181.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_182.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_183.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_184.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_185.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_186.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_187.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_188.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_189.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_19.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_190.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_191.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_192.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_193.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_194.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_195.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_196.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_197.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_198.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_199.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_2.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_20.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_200.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_201.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_202.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_203.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_204.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_205.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_206.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_207.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_208.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_209.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_21.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_210.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_211.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_212.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_213.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_214.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_215.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_216.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_217.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_218.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_219.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_22.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_220.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_221.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_222.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_223.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_224.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_225.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_226.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_227.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_228.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_229.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_23.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_230.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_231.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_232.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_233.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_234.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_235.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_236.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_237.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_238.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_239.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_24.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_240.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_241.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_242.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_243.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_244.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_245.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_246.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_247.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_248.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_249.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_25.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_250.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_251.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_252.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_253.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_254.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_255.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_256.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_257.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_258.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_259.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_26.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_260.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_261.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_262.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_263.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_264.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_265.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_266.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_267.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_268.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_269.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_27.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_270.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_271.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_272.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_273.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_274.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_275.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_276.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_277.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_278.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_279.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_28.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_280.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_281.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_282.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_283.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_284.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_285.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_286.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_29.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_3.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_30.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_31.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_32.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_33.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_34.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_35.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_36.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_37.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_38.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_39.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_4.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_40.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_41.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_42.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_43.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_44.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_45.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_46.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_47.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_48.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_49.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_5.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_50.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_51.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_52.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_53.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_54.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_55.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_56.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_57.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_58.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_59.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_6.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_60.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_61.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_62.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_63.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_64.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_65.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_66.root',
        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_67.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_68.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_69.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_7.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_70.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_71.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_72.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_73.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_74.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_75.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_76.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_77.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_78.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_79.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_8.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_80.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_81.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_82.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_83.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_84.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_85.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_86.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_87.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_88.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_89.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_9.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_90.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_91.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_92.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_93.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_94.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_95.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_96.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_97.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_98.root',
#        '/store/cmst3/group/htautau/CMG/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/GEN-SIM-RAW/VBF_Tau_Timing_20140507/aod_99.root'


        ),
                            skipEvents = cms.untracked.uint32(sEvents)
)

## Maximal Number of Events
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(eMax) )
#process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(10))

#### included from standard pat template
## Geometry and Detector Conditions (needed for a few patTuple production steps)
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.autoCond import autoCond
process.GlobalTag.globaltag = cms.string( autoCond[ 'startup' ] )
process.load("Configuration.StandardSequences.MagneticField_cff")



process.options.allowUnscheduled = cms.untracked.bool(False)

process.load("RecoTauTag.Configuration.RecoPFTauTag_cff")
process.load("PhysicsTools.JetMCAlgos.TauGenJets_cfi")
process.load("RecoJets.JetProducers.ak5GenJets_cfi")
process.load("RecoJets.Configuration.GenJetParticles_cff")

#process.load("PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff")
#from PhysicsTools.PatAlgos.tools.tauTools import *
#switchToPFTauHPS(process)

#process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
from TrackingTools.TransientTrack.TransientTrackBuilder_cfi import TransientTrackBuilderESProducer
process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")

from RecoTauTag.RecoTau.PFRecoTauQualityCuts_cfi import PFTauQualityCuts

process.tauDifferenceAnalyzer = cms.EDFilter("RecoTauDifferenceAnalyzer",
                                             src1 = cms.InputTag("hpsPFTauProducer","",procName),
                                             src2 = cms.InputTag("hpsPFTauProducer","","RECO"),
                                             disc1 = cms.InputTag(discriminator, "", procName),
                                             disc2 = cms.InputTag(discriminator2, "", "RECO"),
                                             chIso1 = cms.InputTag("hpsPFTauMVA3IsolationChargedIsoPtSum","",procName),
                                             chIso2 = cms.InputTag("hpsPFTauMVA3IsolationChargedIsoPtSum","","RECO"),
                                             nIso1 = cms.InputTag("hpsPFTauMVA3IsolationNeutralIsoPtSum","",procName),
                                             nIso2 = cms.InputTag("hpsPFTauMVA3IsolationNeutralIsoPtSum","","RECO"),
                                             PUIso1 = cms.InputTag("hpsPFTauMVA3IsolationPUcorrPtSum","",procName),
                                             PUIso2 = cms.InputTag("hpsPFTauMVA3IsolationPUcorrPtSum","","RECO"),
                                             cmbIso1 = cms.InputTag("hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits","",procName),
                                             cmbIso2 = cms.InputTag("hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits","","RECO"),
                                             genSrc = cms.InputTag("genParticles"),
                                             genTauSrc = cms.InputTag("tauGenJets"),
                                             jetSrc = cms.InputTag("ak5PFJets"),
                                             jetSrcCHS = cms.InputTag("ak5PFJetsCHS"),
                                             primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
                                             matchingDistance = cms.double(0.1),
#                                             checkMother = cms.bool(False),
                                             qualityCuts=PFTauQualityCuts)

process.tauDifferenceAnalyzer.qualityCuts.isolationQualityCuts.minTrackHits = cms.uint32(3)
process.tauDifferenceAnalyzer.qualityCuts.isolationQualityCuts.minTrackPt = cms.double(0.5)
process.tauDifferenceAnalyzer.qualityCuts.isolationQualityCuts.minGammaEt = cms.double(0.5)

## let it run
process.load("CommonTools.ParticleFlow.pfParticleSelection_cff")
process.load("RecoParticleFlow.PFProducer.pfLinker_cff")

process.pfPileUp.PFCandidates = 'particleFlowPtrs'
process.pfNoPileUp.bottomCollection = 'particleFlowPtrs'
process.pfPileUpIso.PFCandidates = 'particleFlowPtrs'
process.pfNoPileUpIso.bottomCollection='particleFlowPtrs'
process.pfPileUpJME.PFCandidates = 'particleFlowPtrs'
process.pfNoPileUpJME.bottomCollection='particleFlowPtrs'


process.p = cms.Path(
        process.tauGenJets*
        process.particleFlowPtrs*
        process.pfParticleSelectionSequence*
        process.PFTau*
        process.tauDifferenceAnalyzer
#        process.patDefaultSequence
            )


#process.TFileService = cms.Service("TFileService", fileName = cms.string("output.root"))

## Output Module Configuration (expects a path 'p')
from PhysicsTools.PatAlgos.patEventContent_cff import patEventContentNoCleaning
process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('patTuple.root'),
                               ## save only events passing the full path
                               #SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
                               ## save PAT output; you need a '*' to unpack the list of commands
                               ## 'patEventContent'
                               outputCommands = cms.untracked.vstring('drop *', *patEventContentNoCleaning )
                               )

#process.outpath = cms.EndPath(process.out)

process.options.wantSummary = False
