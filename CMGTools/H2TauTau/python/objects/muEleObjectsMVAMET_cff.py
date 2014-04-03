import FWCore.ParameterSet.Config as cms

from CMGTools.Common.diTau_cff import *
from CMGTools.H2TauTau.objects.muEleCuts_cff import * 

from CMGTools.Common.Tools.cmsswRelease import cmsswIs44X,cmsswIs52X

from CMGTools.Utilities.metRecoilCorrection.metRecoilCorrection_cff import *

from CMGTools.Common.factories.cmgMuEleCor_cfi import cmgMuEleCor
from CMGTools.H2TauTau.objects.muEleSVFit_cfi import muEleSVFit 
from CMGTools.Common.Tools.cmsswRelease import cmsswIs44X,cmsswIs52X



# no correction, no svfit ---------------------------------------------------

# attaching the cuts defined in this module
# to the di-tau factory

cmgMuEle.cuts = muEleCuts.clone()
#cmgMuEle.cfg.leg1Collection = 'cmgTauSel'
cmgMuEle.cfg.metsigCollection = cms.InputTag('')

# preselection 
cmgMuElePreSel = cmgMuEleSel.clone(
    # cut = ''
    #WARNING
    cut = 'getSelection("cuts_baseline")'
    )

# creates a tau-mu pair and applies loose preselection cuts
muEleStdSequence = cms.Sequence(
    cmgMuEle +
    cmgMuElePreSel
    )


# correction and svfit ------------------------------------------------------

# this is done for preselected di-taus

# mva MET

from CMGTools.Common.eventCleaning.goodPVFilter_cfi import goodPVFilter

from CMGTools.Utilities.mvaMET.mvaMET_cff import *
from CMGTools.Common.factories.cmgBaseMETFromPFMET_cfi import cmgBaseMETFromPFMET
mvaMETMuEle.recBosonSrc = 'cmgMuElePreSel'

cmgMuEleMVAPreSel = cmgMuEleCor.clone()
cmgMuEleMVAPreSel.cfg.diObjectCollection = 'cmgMuElePreSel'


# Correct tau pt (after MVA MET according to current baseline)

from CMGTools.Common.factories.cmgMuEleCor_cfi import cmgMuEleCor
cmgMuEleCor = cmgMuEleCor.clone()

cmgMuEleCor.cfg.diObjectCollection = cms.InputTag('mvaMETMuEle')

# JAN: It's debatable whether this should be applied after MVA MET
# and before the recoil correction instead of at the very beginning


# This selector goes after the tau pt correction
cmgMuEleTauPtSel = cms.EDFilter(
    "CmgMuEleSelector",
    src = cms.InputTag( "cmgMuEleCor" ),
#    cut = cms.string( "leg1().pt()>18." )
#    cut = cms.string( "leg1().pt()>10." )
    cut = cms.string( "(leg1().pt()>20. || leg2().pt()>20.)" )
    )

cmgMuEleTauPtSel = cmgMuEleTauPtSel.clone()


# recoil correction

diTausForRecoil = 'cmgMuEleTauPtSel'
recoilCorMETMuEle =  recoilCorrectedMETMuEle.clone(
    recBosonSrc = diTausForRecoil
    )

muEleMvaMETrecoilSequence = cms.Sequence( goodPVFilter + 
                               mvaMETMuEle +
                               cmgMuEleCor +
                               cmgMuEleTauPtSel +
                               recoilCorMETMuEle
                               )

# SVFit

cmgMuEleCorSVFitPreSel = muEleSVFit.clone()
cmgMuEleCorSVFitPreSel.diTauSrc = cms.InputTag('recoilCorMETMuEle')

# This module is not really necessary anymore
cmgMuEleCorSVFitFullSel = cmgMuEleSel.clone( src = 'cmgMuEleCorSVFitPreSel',
                                             cut = ''
                                             # WARNING!
                                             # cut = 'getSelection("cuts_baseline")'
                                             ) 

muEleCorSVFitSequence = cms.Sequence( #
    muEleMvaMETrecoilSequence +
    cmgMuEleCorSVFitPreSel +
    cmgMuEleCorSVFitFullSel
    )

muEleSequence = cms.Sequence( muEleStdSequence +
                              muEleCorSVFitSequence
                              )

