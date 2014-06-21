import FWCore.ParameterSet.Config as cms
from CMGTools.Common.Tools.cmsswRelease import isNewerThan

is53X = isNewerThan('CMSSW_5_2_X')

def getEleCuts(leg, channel='tauEle', skim=False):

    ptCut = None
    etaCut = None
#    lmvaID = -99999
    lmvaID1 = -99999
    lmvaID2 = -99999
    lmvaID3 = -99999
    lmvaID4 = -99999
    lmvaID5 = -99999
    lmvaID6 = -99999

    smvaID = cms.string('')
#    isoCut = 100
    if channel == 'tauEle':
        ptCut = 20.
        if is53X:
            ptCut = 24.
        etaCut = 2.1
#        lmvaID = 0.9
        lmvaID1 = 0.925
        lmvaID2 = 0.975
        lmvaID3 = 0.985
        
        smvaID = cms.string('(abs({leg}().sourcePtr().superCluster().eta())<0.8 && {leg}().mvaNonTrigV0() > {lmvaID1}) || (abs({leg}().sourcePtr().superCluster().eta())>0.8 && abs({leg}().sourcePtr().superCluster().eta())<1.479 && {leg}().mvaNonTrigV0() > {lmvaID2}) || (abs({leg}().sourcePtr().superCluster().eta())>1.479 && {leg}().mvaNonTrigV0() > {lmvaID3})'.format(leg=leg, lmvaID1=lmvaID1, lmvaID2=lmvaID2, lmvaID3=lmvaID3))
#        isoCut = 0.3
    elif channel == 'muEle':
        ptCut = 10.
        etaCut = 2.3

        lmvaID1 = 0.925
        lmvaID2 = 0.915
        lmvaID3 = 0.965
        lmvaID4 = 0.905
        lmvaID5 = 0.955
        lmvaID6 = 0.975

        smvaID = cms.string('({leg}().pt()<20. && abs({leg}().sourcePtr().superCluster().eta())<0.8 && {leg}().mvaNonTrigV0() > {lmvaID1}) || ({leg}().pt() < 20. && abs({leg}().sourcePtr().superCluster().eta())>0.8 && abs({leg}().sourcePtr().superCluster().eta())<1.479 && {leg}().mvaNonTrigV0() > {lmvaID2}) || ({leg}().pt() < 20. && abs({leg}().sourcePtr().superCluster().eta())>1.479 && {leg}().mvaNonTrigV0() > {lmvaID3}) || ({leg}().pt()>20. && abs({leg}().sourcePtr().superCluster().eta())<0.8 && {leg}().mvaNonTrigV0() > {lmvaID4}) || ({leg}().pt() > 20. && abs({leg}().sourcePtr().superCluster().eta())>0.8 && abs({leg}().sourcePtr().superCluster().eta())<1.479 && {leg}().mvaNonTrigV0() > {lmvaID5}) || ({leg}().pt() > 20. && abs({leg}().sourcePtr().superCluster().eta())>1.479 && {leg}().mvaNonTrigV0() > {lmvaID6})'.format(leg=leg, lmvaID1=lmvaID1, lmvaID2=lmvaID2, lmvaID3=lmvaID3,lmvaID4=lmvaID4, lmvaID5=lmvaID5, lmvaID6=lmvaID6))
        
    else:
        raise ValueError('bad channel specification:'+channel)

    if skim:
        print 'WARNING: skimming not implemented in getEleCuts!'

    eleCuts = cms.PSet(
        kinematics = cms.PSet(
          pt = cms.string('{leg}().pt()>{ptCut}'.format(leg=leg, ptCut=ptCut)),
          eta = cms.string('abs({leg}().eta())<{etaCut}'.format(leg=leg, etaCut=etaCut))
        ),
        ID = cms.PSet(
            hitsnum = cms.string('{leg}().numberOfHits==0'.format(leg=leg)),
            convVeto = cms.string('{leg}().passConversionVeto()!=0'.format(leg=leg)),
            mvaID = smvaID
#            dxy = cms.string('abs({leg}().dxy()) < 0.02'.format(leg=leg)),
#            dz = cms.string('abs({leg}().dz()) < 0.2'.format(leg=leg))

        ),
#         iso = cms.PSet(
#           #COLIN the iso elest be done on charged particles, not charged hadrons
#           relIsoDBeta = cms.string('{leg}().relIso(0.5, 1)<{isoCut}'.format(leg=leg,isoCut=isoCut))
#         )
    )

    return eleCuts

