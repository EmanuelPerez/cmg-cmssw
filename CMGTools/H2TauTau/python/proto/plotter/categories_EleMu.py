import copy

from CMGTools.H2TauTau.proto.plotter.categories_common import *
from CMGTools.H2TauTau.proto.plotter.cut import * 

from CMGTools.Common.Tools.cmsswRelease import cmsswIs44X,cmsswIs52X

pt1 = 10.
pt2 = 10. # 2011

#inc_sig_tau = Cut('l1_looseMvaIso>0.5 && (l1_EOverp>0.2 || l1_decayMode!=0) && l1_againstMuonTight>0.5 && l1_againstElectronLoose>0.5 && l1_dxy<0.045 && l1_dz<0.2 && l1_pt>{pt1}'.format(pt1=pt1))
#inc_sig_tau = Cut('l1_looseMvaIso>0.5 && l1_againstMuonTight>0.5 && l1_againstElectronLoose>0.5 && l1_dxy<0.045 && l1_dz<0.2 && l1_pt>{pt1}'.format(pt1=pt1))

# NEW one - to be implemented as soon as trees are there
inc_sig_tau = Cut('leptonAccept && thirdLeptonVeto && l1_threeHitIso<1.5 && l1_againstMuonTight>0.5 && l1_againstElectronLoose>0.5 && l1_dxy<0.045 && l1_dz<0.2 && l1_pt>{pt1}'.format(pt1=pt1))
inc_sig_mu = Cut('l1_relIso05<0.1 && l1_tightId>0.5 && TMath::Abs(l1_dxy)<0.045 && TMath::Abs(l1_dz)<0.2 && l1_pt>{pt1}'.format(pt1=pt1))
inc_sig_ele = Cut('l2_relIso05<0.1 && l2_tightId>0.5 && TMath::Abs(l2_dxy)<0.045 && TMath::Abs(l2_dz)<0.2 && l2_pt>{pt2}'.format(pt2=pt2))
inc_common = Cut('leptonAccept && thirdLeptonVeto')

inc_sig = inc_sig_mu & inc_sig_ele & inc_common



inc_sig_mu_elelike = Cut('l2_relIso05<0.1 && l2_tightId>0.5 && l2_dxy<0.045 && l2_dz<0.2 && l2_pt>{pt2}'.format(pt2=24.))

inc_sig_elelike = inc_sig_mu_elelike & inc_sig_tau

def cutstr_signal():
    return inc_sig

def cutstr_rlxmuiso(cutstr, muIsoCut):
    '''WARNING: assumes mu iso cut is 0.1'''
    return cutstr.replace( 'l2_relIso05<0.1',
                           'l2_relIso05<{cut}'.format(cut=muIsoCut) )

def cutstr_rlxtauiso(cutstr, tauIsoCut):
    '''WARNING: assumes mu iso cut is 0.1'''
    return cutstr.replace('l1_looseMvaIso>0.5',
                          'l1_rawMvaIso>{cut}'.format(cut=tauIsoCut) )

def cutstr_rlxtaumuiso(cutstr, tauIsoCut, muIsoCut):
    '''WARNING: assumes mu iso cut is 0.1'''
    cutstr = cutstr_rlxmuiso(cutstr, muIsoCut)
    return cutstr_rlxtauiso(cutstr, tauIsoCut)


cat_Inc_RlxMuIso = str(inc_sig).replace('l2_relIso05<0.1','l2_relIso05<1.0')
cat_Inc_RlxTauIso = str(inc_sig).replace('l1_threeHitIso<1.5', 'l1_threeHitIso<10.0')
cat_Inc_RlxMuTauIso = str(inc_sig).replace('l2_relIso05<0.1','l2_relIso05<0.5').replace('l1_threeHitIso<1.5', 'l1_threeHitIso<10.0')
cat_Inc_AntiMuTauIso = str(inc_sig).replace('l2_relIso05<0.1','l2_relIso05>0.1').replace('l1_looseMvaIso>0.5', 'l1_looseMvaIso<0.5')
cat_Inc_AntiMuTauIso_B = str(inc_sig).replace('l2_relIso05<0.1','l2_relIso05>0.2').replace('l1_looseMvaIso>0.5', 'l1_rawMvaIso>-0.75')

cat_Inc_AntiMuTauIsoJosh = str(inc_sig).replace('l2_relIso05<0.1','l2_relIso05>0.2 && l2_relIso05<0.5').replace('l1_looseMvaIso>0.5', 'l1_rawMvaIso>0.7')
cat_Inc_AntiMuIso = str(inc_sig).replace('l2_relIso05<0.1','l2_relIso05>0.1')
cat_Inc_AntiMuIsoJan = str(inc_sig).replace('l2_relIso05<0.1','l2_relIso05>0.2 && l2_relIso05<0.5')
cat_Inc_TightAntiMuIsoJan = str(inc_sig).replace('l2_relIso05<0.1','l2_relIso05>0.1 && l2_relIso05<0.2')
cat_Inc_AntiMuAntiTauIsoJan = str(inc_sig).replace('l2_relIso05<0.1','l2_relIso05>0.2 && l2_relIso05<0.5').replace('l1_threeHitIso<1.5', 'l1_threeHitIso>1.5 && l1_threeHitIso<10.0')
cat_Inc_AntiMuRlxTauIsoJan = str(inc_sig).replace('l2_relIso05<0.1','l2_relIso05>0.2 && l2_relIso05<0.5').replace('l1_threeHitIso<1.5', 'l1_threeHitIso<10.0')
#cat_Inc_AntiTauIso = str(inc_sig).replace('l1_looseMvaIso>0.5', 'l1_looseMvaIso<0.5')
# cat_Inc_AntiTauIso = str(inc_sig).replace('l1_threeHitIso<1.5', 'l1_threeHitIso>1.5') # && l1_threeHitIso<10.0')
cat_Inc_AntiTauIsoJan = str(inc_sig).replace('l1_threeHitIso<1.5', 'l1_threeHitIso>1.5 && l1_threeHitIso<10.0')
cat_Inc_AntiTauIso = str(inc_sig).replace('l1_threeHitIso<1.5', 'l1_threeHitIso>1.5 && l1_threeHitIso<5.0')

cat_Inc_RlxMuTauIso_b = str(inc_sig).replace('l2_relIso05<0.1','l2_relIso05<0.5').replace('l1_looseMvaIso>0.5', 'l1_rawMvaIso>0.5')
cat_Inc = str(inc_sig)

cat_Inc_elelike = str(inc_sig_elelike)

# Yuta added


#import pdb; pdb.set_trace()

categories = {
    'Xcat_Inc_AntiMuTauIsoJoshX':cat_Inc_AntiMuTauIsoJosh,
    'Xcat_Inc_RlxMuIsoX':cat_Inc_RlxMuIso,
    'Xcat_Inc_RlxTauIsoX':cat_Inc_RlxTauIso,
    'Xcat_IncX':cat_Inc,
    'Xcat_Inc_AntiTauIsoX':cat_Inc_AntiTauIso,
    'Xcat_Inc_AntiTauIsoJanX':cat_Inc_AntiTauIsoJan,
    'Xcat_Inc_AntiMuIsoJanX':cat_Inc_AntiMuIsoJan,
    'Xcat_Inc_TightAntiMuIsoJanX':cat_Inc_TightAntiMuIsoJan,
    'Xcat_Inc_AntiMuAntiTauIsoJanX':cat_Inc_AntiMuAntiTauIsoJan,
    'Xcat_Inc_AntiMuRlxTauIsoJanX':cat_Inc_AntiMuRlxTauIsoJan,
    'Xcatinc_sig_elelikeX':cat_Inc_elelike
    }

categories.update( categories_common )

#update categories

categories['Xcat_J0_oldhighX'] = categories['Xcat_J0_oldhighX'].replace('l1_pt>40.','l1_pt>35. && mva_emu>-0.5')
categories['Xcat_J0_oldlowX']  = categories['Xcat_J0_oldlowX'].replace('l1_pt<=40.','l1_pt<=35.&& mva_emu>-0.5 ')

categories['Xcat_J1_oldhighX'] = categories['Xcat_J1_oldhighX'].replace('l1_pt>40.','l1_pt>35. && mva_emu>-0.5')
categories['Xcat_J1_oldlowX']  = categories['Xcat_J1_oldlowX'].replace('l1_pt<=40.','l1_pt<=35.&& mva_emu>-0.5')

categories['Xcat_VBF_tightX']  = categories['Xcat_VBF_tightX'].replace('l1_pt>30.','(l1_pt>10. || l2_pt>10.) && mva_emu>-0.5')
categories['Xcat_VBF_looseX']  = categories['Xcat_VBF_looseX'].replace('l1_pt>30.','(l1_pt>10. || l2_pt>10.) && mva_emu>-0.5')

#cat_J0_high = str(cat_J0_oldhigh).replace('l1_pt>40.','l1_pt>35.')
#cat_J0_low  = str(cat_J0_oldlow).replace('l1_pt<=40.','l1_pt<=35.')
#
#cat_J1_oldhigh = str(cat_J1_oldhigh).replace('l1_pt>40.','l1_pt>35.')
#cat_J1_oldlow = str(cat_J1_oldlow).replace('l1_pt<=40.','l1_pt<=35.')
#
#cat_VBF_tight = str(cat_VBF_tight).replace('l1_pt>30.','l1_pt>20.')
#cat_VBF_loose = str(cat_VBF_loose).replace('l1_pt>30.','l1_pt>20.')
