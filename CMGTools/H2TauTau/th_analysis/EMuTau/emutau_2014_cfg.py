import copy, os
import shelve
import CMGTools.RootTools.fwlite.Config as cfg
from CMGTools.RootTools.fwlite.Config import printComps

from CMGTools.H2TauTau.triggerMap import pathsAndFilters
from CMGTools.H2TauTau.proto.weights.weighttable import mu_id_taumu_2012, mu_iso_taumu_2012
from CMGTools.RootTools.RootTools import * 

# set True when you want to throw the jobs
#jobmode = True
jobmode = False
selector = False

if jobmode:
    selector = False



# Andrew Summer 13 (MC is identical to the previous one)
puFileMC = '/afs/cern.ch/user/a/agilbert/public/HTT_Pileup/13-09-13/MC_Summer12_PU_S10-600bins.root'
puFileData = '/afs/cern.ch/user/a/agilbert/public/HTT_Pileup/13-09-13/Data_Pileup_2012_ReRecoPixel-600bins.root'

mc_vertexWeight = None

# mc_tauEffWeight_mc = 'effTau2012MC53X'
# mc_muEffWeight_mc = 'eff_2012_Rebecca_TauMu_IsoMu1753XMC'
# mc_tauEffWeight = 'effTau2012ABC'
# mc_muEffWeight = 'effMu2012_Rebecca_TauMu_ABC'

mc_tauEffWeight_mc = 'effTau_muTau_MC_2012ABCDSummer13'
mc_muEffWeight_mc = 'effMu_muTau_MC_2012ABCD'
mc_tauEffWeight = 'effTau_muTau_Data_2012ABCDSummer13'
mc_muEffWeight = 'effMu_muTau_Data_2012ABCDSummer13'

elist = []

#for line in open('f3_data_list'):
#for line in open('yuta'):
#    evt = line.rstrip().split(':')[2]
#    print evt
#    elist.append(int(evt))

print 'eventSelector = ', len(elist)

eventSelector = cfg.Analyzer(
    'EventSelector',
#    toSelect = [2300255]
#    toSelect = [340638739]
    toSelect = elist
#    toSelect = [1547113]
#    toSelect = [2536837]
#    toSelect = [1017082]
#    toSelect = [2274154]
#    toSelect = [2655724]
#    toSelect = [1321707]
#    toSelect = [4326570] # MuonTight
#    toSelect = [1901037]
#    toSelect = [726881]
#    toSelect = [3078777]
    )


jsonAna = cfg.Analyzer(
    'JSONAnalyzer',
    )

#triggerAna = cfg.Analyzer(
#    'TriggerAnalyzer'
#    )

triggerAna = cfg.Analyzer(
    'DiTriggerAnalyzer'    
    )

vertexAna = cfg.Analyzer(
    'VertexAnalyzer',
    goodVertices = 'goodPVFilter',
    vertexWeight = mc_vertexWeight,
    fixedWeight = 1,
    verbose = False,
    )

embedWeighter = cfg.Analyzer(
    'EmbedWeighter',
    isRecHit = False,
    verbose = False
    )

pileUpAna = cfg.Analyzer(
    'PileUpAnalyzer',
    true = True
    )

genErsatzAna = cfg.Analyzer(
    'GenErsatzAnalyzer',
    verbose = False
    )

genTopAna = cfg.Analyzer(
    'GenTopAnalyzer',
    src = 'genParticlesPruned',
    verbose = False
    )

EMuTauAna = cfg.Analyzer(
    'WHEMTAnalyzer',
#    scaleShift1 = tauScaleShift,
#    pt1 = 20,
#    eta1 = 2.3,
#    iso1 = None,
#    pt2 = 20,
#    eta2 = 2.1,
#    iso2 = 0.1,
#    m_min = 10,
#    m_max = 99999,
#    dR_min = 0.5,
    triggerMap = pathsAndFilters,
#    mvametsigs = 'mvaMETTauMu',
#    verbose = False
    )

dyJetsFakeAna = cfg.Analyzer(
    'DYJetsFakeAnalyzer',
    leptonType = 13,
    src = 'genParticlesPruned',
    )

WNJetsAna = cfg.Analyzer(
    'WNJetsAnalyzer',
    verbose = False
    )

NJetsAna = cfg.Analyzer(
    'NJetsAnalyzer',
    fillTree = True,
    verbose = False
    )

WNJetsTreeAna = cfg.Analyzer(
    'WNJetsTreeAnalyzer'
    )

higgsWeighter = cfg.Analyzer(
    'HiggsPtWeighter',
    src = 'genParticlesPruned',
    )

tauDecayModeWeighter = cfg.Analyzer(
    'TauDecayModeWeighter',
    )

tauFakeRateWeighter = cfg.Analyzer(
    'TauFakeRateWeighter'
    )

tauWeighter = cfg.Analyzer(
    'LeptonWeighter_tau',
    effWeight = mc_tauEffWeight,
    effWeightMC = mc_tauEffWeight_mc,
    lepton = 'leg1',
    verbose = False,
    disable = False,
    )

muonWeighter = cfg.Analyzer(
    'LeptonWeighter_mu',
    effWeight = mc_muEffWeight,
    effWeightMC = mc_muEffWeight_mc,
    lepton = 'leg2',
    verbose = False,
    disable = False,
    idWeight = mu_id_taumu_2012,
    isoWeight = mu_iso_taumu_2012    
    )



# defined for vbfAna and eventSorter
vbfKwargs = dict( Mjj = 500,
                  deltaEta = 3.5    
                  )


jetAna = cfg.Analyzer(
    'JetAnalyzerEMT',
    jetCol = 'cmgPFJetSel',
    jetPt = 20.,
#    jetPt = 10.,
    jetEta = 4.7,
    btagSFseed = 123456,
    relaxJetId = False, 
    jerCorr = False,
    #jesCorr = 1.,
    )

vbfSimpleAna = cfg.Analyzer(
    'VBFSimpleAnalyzer',
    vbfMvaWeights = '',
    cjvPtCut = 30.,
    **vbfKwargs    
    )


treeProducer = cfg.Analyzer(
    'H2TauTauTreeProducerEMT2'
    )


#########################################################################################
# sample definition
#from CMGTools.H2TauTau.proto.samples.run2012.emuTau_YutaOct15 import *
#from CMGTools.H2TauTau.proto.samples.run2012.emuTau_YutaOct18 import *
#from CMGTools.H2TauTau.proto.samples.run2012.emuTau_YutaNov15 import *
#from CMGTools.H2TauTau.proto.samples.run2012.emuTau_YutaDec24 import *
#from CMGTools.H2TauTau.proto.samples.run2012.emuTau_YutaFeb11 import *
from CMGTools.H2TauTau.proto.samples.run2012.emuTau_YutaFeb12 import * 
#########################################################################################
diboson_list = [   # WWJetsTo2L2Nu,
                   # WZJetsTo2L2Q,
                    WZJetsTo3LNu,
                   # ZZJetsTo2L2Nu,
                   # ZZJetsTo2L2Q,
#                    ZZJetsTo4L,
                   # T_tW,
                   # Tbar_tW
                    ]

for mc in diboson_list:
    mc.puFileMC = puFileMC
    mc.puFileData = puFileData

#for mc in [TTJetsFullLept]:

for mc in MC_list:
    mc.puFileMC = puFileMC
    mc.puFileData = puFileData


#WNJetsAna.nevents = [ WJets.nGenEvents,
#                      W1Jets.nGenEvents,
#                      W2Jets.nGenEvents,
#                      W3Jets.nGenEvents,
#                      W4Jets.nGenEvents
#                      ]

# Fractions temporarily taken from Jose (29 May 2013):
#WNJetsAna.fractions = [0.74392452, 0.175999, 0.0562617, 0.0168926, 0.00692218]


#WJetsSoup = copy.copy(WJets)
#WJetsSoup.name = 'WJetsSoup'

#DYJetsSoup = copy.copy(DYJets)
#DYJetsSoup.name = 'DYJetsSoup'

#VVgroup = [comp.name for comp in diboson_list]

selectedComponents = []
####selectedComponents = [TTJetsFullLept,
####    TTJetsSemiLept,
####    TTJetsHadronic, 
####    DYJets, WJets,
####    W1Jets, W2Jets, W3Jets, W4Jets,
####    W1Jets_ext, W2Jets_ext, W3Jets_ext,
####    DY1Jets, DY2Jets, DY3Jets, DY4Jets,
####    ]
####
##### FOR PLOTTING:
####TTgroup = None
####if doThePlot:
####    selectedComponents = [TTJetsFullLept,
####    TTJetsSemiLept,
####    TTJetsHadronic, #DYJets, #WJets,
####        WJetsSoup,
####        DYJetsSoup
####        ]
####    TTgroup = [TTJetsFullLept.name,
####    TTJetsSemiLept.name,
####    TTJetsHadronic.name]
####
####if not doThePlot:
####    selectedComponents.extend( higgs )
####    selectedComponents.extend( mc_higgs_susy )
####else:
####    # pass
####    selectedComponents.extend( higgs )
####    selectedComponents.extend( mc_higgs_susy )
####
####selectedComponents.extend( diboson_list )
####
####if not simulatedOnly:
####    selectedComponents.extend( data_list )
#    selectedComponents.extend( embed_list )


#sequence = cfg.Sequence( [
#    # eventSelector,
#    jsonAna, 
#    triggerAna,
#    vertexAna, 
#    EMuTauAna,
##    dyJetsFakeAna,
#    # WNJetsAna,
#    # WNJetsTreeAna,
##    NJetsAna,
##    higgsWeighter, 
#    jetAna,
#    vbfSimpleAna,
#    pileUpAna,
##    embedWeighter,
#    tauDecayModeWeighter,
##    tauFakeRateWeighter,
#    tauWeighter, 
#    muonWeighter, 
#    treeProducer,
#    # treeProducerXCheck
#   ] )


seq_list = [
            jsonAna, 
            triggerAna,
            vertexAna,
            EMuTauAna,
            jetAna,
            pileUpAna,
            genTopAna,
            treeProducer,
            ]

if jobmode==False and selector:
    seq_list.insert(0, eventSelector)

if jobmode:
    seq_list = [
        jsonAna, 
        triggerAna,
        vertexAna,
        EMuTauAna,
        jetAna,
        pileUpAna,
        genTopAna,
        treeProducer,
        ]

print 'sequence = ', seq_list
sequence = cfg.Sequence(seq_list)

#sequence = cfg.Sequence([
#    eventSelector,
#    jsonAna, 
#    triggerAna,
#    vertexAna,
#    EMuTauAna,
#    jetAna,
#    pileUpAna,
##    tauDecayModeWeighter,
##    tauWeighter, 
##    muonWeighter, 
#    treeProducer,
#    ] )


selectedComponents = [comp for comp in selectedComponents if comp.dataset_entries > 0]



###test = 1
###if test==1:
###    # comp = embed_Run2012C_22Jan
###    # comp = DYJets
###    # comp = HiggsGGH125
###    # comp = HiggsSUSYGluGlu1000
####    comp = W1Jets_ext
####    comp = [WZJetsTo3LNu, ZZJetsTo4L]
###    # comp = data_Run2012A
####    selectedComponents = [comp]
####    selectedComponents = [WZJetsTo3LNu, ZZJetsTo4L]
###    selectedComponents = diboson_list
####    comp.splitFactor = 1
###    for comp in selectedComponents:
###        comp.splitFactor = 1
###
###    # comp.files = comp.files[:10]
###    # comp.files = ['tauMu_fullsel_tree_CMG.root']
###elif test==2:
###    selectedComponents = selectedComponents[:12]
###    for comp in selectedComponents:
###        comp.splitFactor = 1
###        comp.files = comp.files[:5]
###elif test==3:
###    # selectedComponents = [WJets, W1Jets, W2Jets, W3Jets, W4Jets]
###    # selectedComponents = higgs
###    # selectedComponents = data_list
###    # selectedComponents = embed_list
###    # selectedComponents += [DYJets, DY1Jets, DY2Jets, DY3Jets, DY4Jets]
###    # selectedComponents = mc_higgs_susy
###    selectedComponents = [WJets, W1Jets, W2Jets, W3Jets, W4Jets, W1Jets_ext, W2Jets_ext, W3Jets_ext]
###    # selectedComponents += higgs
###    # selectedComponents += mc_higgs_susy
###    # selectedComponents = [DYJets]


#selectedComponents = [TTJetsFullLept]

if not jobmode:
#    selectedComponents = diboson_list
#    selectedComponents = [WZJetsTo3LNu]
    selectedComponents = mc_tHW
#    selectedComponents = data_list    
#    selectedComponents = allsamples
#selectedComponents = []
#selectedComponents.extend(diboson_list)



if jobmode:
    selectedComponents = allsamples


if not jobmode:
#    selectedComponents = [WZJetsTo3LNu]
    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files[:1]

#for comp in selectedComponents:
#    comp.splitFactor = 1
#    comp.files[:1]
    
config = cfg.Config( components = selectedComponents,
                     sequence = sequence )

printComps(config.components, True)
