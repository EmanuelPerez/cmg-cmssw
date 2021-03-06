#################################
# 
# 12 Nov 2013
# Y.Takahashi (Yuta.Takahashi@cern.ch)
# 
# This is the analyzer to obtain control samples for the kNN training
# python analysis_antiTau.py --mode (antiMu, antiE, antiEMu, signal)
#
#################################

import math, sys, array
import numpy as num
from array import array
from ROOT import TFile, TH1F, gDirectory, TMVA, TTree, Double
from ROOT import TLorentzVector, Double # for M(l2,tau) calculation
import optparse
import config as tool

### For options
parser = optparse.OptionParser()
parser.add_option('--channel', action="store", dest="channel", default='muon') # muon means jet->muon fake sample
parser.add_option('--phys', action="store", dest="phys", default='data') # muon means jet->muon fake sample
parser.add_option('--select', action="store_true", dest="select", default=False)
options, args = parser.parse_args()

print 
print '[INFO] Analysis channel = ', options.channel

elist = []

#for line in open('f3_signal_data_mauro_only.txt'):
if options.select:
    for line in open('yuta'):
        evt = line.rstrip().split(':')[2]
#        print evt
        elist.append(int(evt))
    print '[INFO] # of selected events = ', len(elist)
        

#process = ['WW','tt1l','tt2l','DY0','DY1','DY3','DY4']
#process = ['tt0l','tt1l','tt2l']
#process = ['tt1l']

### reading file ...
process = [options.phys]

db = tool.ReadFile(process)
filedict = db.returnFile()

outfile = [0 for i in range(len(process))]

for ii, pn in enumerate(process):
    outfile[ii] = 'EventList/Wjet_' + options.channel + '_' + options.phys + '.list'
    print '[INFO] Event list will be written at ', outfile[ii]

    
if __name__ == '__main__':

    for index, ifile in enumerate(filedict):

        pname = ifile[0]
        filename = ifile[1]
        lum_weight = ifile[2]
        ptype = ifile[3]

        fw = open(outfile[index], 'w')
        
#        outputfile = '/afs/cern.ch/user/y/ytakahas/public/forJan/kNN_training/Wjet_' + options.channel + '_training_' + pname[index] + '.root'
        outputfile = 'root_aux/Wjet_' + options.channel + '_training_' + pname + '.root'
        ofile = TFile(outputfile, 'recreate')
        t = TTree('kNNTrainingTree','kNNTrainingTree')

        lepton_pt = num.zeros(1, dtype=float)
        lepton_eta = num.zeros(1, dtype=float)
        lepton_phi = num.zeros(1, dtype=float)
        lepton_mass = num.zeros(1, dtype=float)
        lepton_jetpt = num.zeros(1, dtype=float)
        lepton_kNN_jetpt = num.zeros(1, dtype=float)
        lepton_njet = num.zeros(1, dtype=int)
        lepton_id = num.zeros(1, dtype=int)
        lepton_iso = num.zeros(1, dtype=int)
        lepton_reliso = num.zeros(1, dtype=float)
        lepton_MT = num.zeros(1, dtype=float)
        lepton_charge = num.zeros(1, dtype=int)
        lepton_dpt = num.zeros(1, dtype=float)

        slepton_pt = num.zeros(1, dtype=float)
        slepton_eta = num.zeros(1, dtype=float)
        slepton_phi = num.zeros(1, dtype=float)
        slepton_mass = num.zeros(1, dtype=float)
        slepton_jetpt = num.zeros(1, dtype=float)
        slepton_kNN_jetpt = num.zeros(1, dtype=float)
        slepton_njet = num.zeros(1, dtype=int)
        slepton_id = num.zeros(1, dtype=int)
        slepton_iso = num.zeros(1, dtype=int)
        slepton_reliso = num.zeros(1, dtype=float)
        slepton_MT = num.zeros(1, dtype=float)
        slepton_charge = num.zeros(1, dtype=int)
        slepton_dpt = num.zeros(1, dtype=float)

        evt_weight = num.zeros(1, dtype=float)
        evt_weight_raw = num.zeros(1, dtype=float)
        evt_weight_muid = num.zeros(1, dtype=float)
        evt_weight_mutrig = num.zeros(1, dtype=float)
        evt_weight_eid = num.zeros(1, dtype=float)
        evt_weight_etrig = num.zeros(1, dtype=float)

        evt_Mem = num.zeros(1, dtype=float)
        evt_run = num.zeros(1, dtype=int)
        evt_evt = num.zeros(1, dtype=int)
        evt_lum = num.zeros(1, dtype=int)
        evt_njet = num.zeros(1, dtype=int)
        evt_isMC = num.zeros(1, dtype=int)
        evt_isMCw = num.zeros(1, dtype=float)
        evt_dphi_mu_met = num.zeros(1, dtype=float)
        evt_dphi_e_met = num.zeros(1, dtype=float)
        evt_M_mujet = num.zeros(1, dtype=float)
        evt_M_ejet = num.zeros(1, dtype=float)
        
        
        evt_id = num.zeros(1, dtype=int)
        evt_met = num.zeros(1, dtype=float)
        
        t.Branch('lepton_pt',lepton_pt,'lepton_pt/D')
        t.Branch('lepton_eta',lepton_eta,'lepton_eta/D')
        t.Branch('lepton_phi',lepton_phi,'lepton_phi/D')
        t.Branch('lepton_mass', lepton_mass, 'lepton_mass/D')
        t.Branch('lepton_jetpt',lepton_jetpt, 'lepton_jetpt/D')
        t.Branch('lepton_kNN_jetpt',lepton_kNN_jetpt, 'lepton_kNN_jetpt/D')
        t.Branch('lepton_njet',lepton_njet, 'lepton_njet/I')
        t.Branch('lepton_id', lepton_id, 'lepton_id/I')
        t.Branch('lepton_iso', lepton_iso, 'lepton_iso/I')
        t.Branch('lepton_reliso', lepton_reliso, 'lepton_reliso/D')
        t.Branch('lepton_MT', lepton_MT, 'lepton_MT/D')
        t.Branch('lepton_charge', lepton_charge, 'lepton_charge/I')
        t.Branch('lepton_dpt', lepton_dpt, 'lepton_dpt/D')

        t.Branch('slepton_pt',slepton_pt,'slepton_pt/D')
        t.Branch('slepton_eta',slepton_eta,'slepton_eta/D')
        t.Branch('slepton_phi',slepton_phi,'slepton_phi/D')
        t.Branch('slepton_mass', slepton_mass, 'slepton_mass/D')
        t.Branch('slepton_jetpt',slepton_jetpt, 'slepton_jetpt/D')
        t.Branch('slepton_kNN_jetpt',slepton_kNN_jetpt, 'slepton_kNN_jetpt/D')
        t.Branch('slepton_njet',slepton_njet, 'slepton_njet/I')
        t.Branch('slepton_id', slepton_id, 'slepton_id/I')
        t.Branch('slepton_iso', slepton_iso, 'slepton_iso/I')
        t.Branch('slepton_reliso', slepton_reliso, 'slepton_reliso/D')
        t.Branch('slepton_MT', slepton_MT, 'slepton_MT/D')
        t.Branch('slepton_charge', slepton_charge, 'slepton_charge/I')
        t.Branch('slepton_dpt', slepton_dpt, 'slepton_dpt/D')

        t.Branch('evt_Mem', evt_Mem, 'evt_Mem/D')
        t.Branch('evt_weight', evt_weight, 'evt_weight/D')
        t.Branch('evt_weight_raw', evt_weight_raw, 'evt_weight_raw/D')
        t.Branch('evt_weight_muid', evt_weight_muid, 'evt_weight_muid/D')
        t.Branch('evt_weight_eid', evt_weight_eid, 'evt_weight_eid/D')
        t.Branch('evt_weight_mutrig', evt_weight_mutrig, 'evt_weight_mutrig/D')
        t.Branch('evt_weight_etrig', evt_weight_etrig, 'evt_weight_etrig/D')
        
        t.Branch('evt_njet', evt_njet, 'evt_njet/I')
        t.Branch('evt_isMC', evt_isMC, 'evt_isMC/I')
        t.Branch('evt_isMCw', evt_isMCw, 'evt_isMCw/D')
        t.Branch('evt_id', evt_id, 'evt_id/I')
        t.Branch('evt_run', evt_run, 'evt_run/I')
        t.Branch('evt_evt', evt_evt, 'evt_evt/I')
        t.Branch('evt_lum', evt_lum, 'evt_lum/I')
        t.Branch('evt_met', evt_met, 'evt_met/D')
        
        t.Branch('evt_dphi_mu_met', evt_dphi_mu_met, 'evt_dphi_mu_met/D')
        t.Branch('evt_dphi_e_met', evt_dphi_e_met, 'evt_dphi_e_met/D')        
        t.Branch('evt_M_mujet', evt_M_mujet, 'evt_M_mujet/D')
        t.Branch('evt_M_ejet', evt_M_ejet, 'evt_M_ejet/D')

        
        ###################

        print '[INFO] ', index, filename, 'is processing => ', outputfile

        myfile = TFile(filename)

        main = gDirectory.Get('H2TauTauTreeProducerEMT2')
        mchain = gDirectory.Get('H2TauTauTreeProducerEMT2_muon')
        echain = gDirectory.Get('H2TauTauTreeProducerEMT2_electron')
        tchain = gDirectory.Get('H2TauTauTreeProducerEMT2_tau')
        vmchain = gDirectory.Get('H2TauTauTreeProducerEMT2_vetomuon')
        vechain = gDirectory.Get('H2TauTauTreeProducerEMT2_vetoelectron')
        vtchain = gDirectory.Get('H2TauTauTreeProducerEMT2_vetotau')
        bchain = gDirectory.Get('H2TauTauTreeProducerEMT2_bjet')
        jchain = gDirectory.Get('H2TauTauTreeProducerEMT2_jet')

        ptr_m = 0        
        ptr_e = 0
        ptr_t = 0
        
        ptr_vm = 0      
        ptr_ve = 0
        ptr_vt = 0

        ptr_nb = 0
        ptr_nj = 0

        Total = main.GetEntries()
        Passed = 0

        counter = [0 for ii in range(11)]
        
        for jentry in xrange(main.GetEntries()):

            ientry = main.LoadTree(jentry)
            nb = main.GetEntry(jentry)

            evt_flag = False

            if options.select:
                for ievent in elist:
                    if main.evt == ievent:
                        print 'event = ', main.evt, ' has been choosen'
                        evt_flag = True




            counter[0] += 1
            
            if jentry%10000==0:
                print '[INFO]', jentry, '/', main.GetEntries() #nmuon, nelectron, ntau, nvmuon, nvelectron, nvtau

            nmuon      = int(main.nmuon)
            nelectron  = int(main.nelectron)
            ntau       = int(main.ntau)
            
            nvmuon     = int(main.nvmuon)
            nvelectron = int(main.nvelectron)
            nvtau      = int(main.nvtau)

            nbjets     = int(main.nBJets)
            njets      = int(main.nJets)

            if options.select:
                if evt_flag == False:
                    ptr_m += nmuon
                    ptr_e += nelectron
                    ptr_t += ntau
                    ptr_vm += nvmuon
                    ptr_ve += nvelectron
                    ptr_vt += nvtau
                    ptr_nb += nbjets
                    ptr_nj += njets                    
                    continue

            if options.select:
                print 'event is selected ! => ', main.evt
            counter[1] += 1

            # for real Leptons
            signal_muon = []
            signal_electron = []
            signal_tau = []
            
            for im in xrange(ptr_m, ptr_m + nmuon):
                mchain.LoadTree(im)
                mchain.GetEntry(im)

#                print 'Yuta_mu', ptr_m, mchain.muon_MT, mchain.muon_pt, mchain.muon_id, mchain.muon_iso
                                
                if ((options.channel=='muon' and mchain.muon_MT < 35.) or \
                    (options.channel=='electron' and mchain.muon_id and mchain.muon_reliso < 0.15 and mchain.muon_MT > 35.)):
#                if ((options.channel=='muon' and mchain.muon_MT < 35. and mchain.muon_pt > 10.) or \
#                    (options.channel=='electron' and mchain.muon_id and mchain.muon_reliso < 0.15 and mchain.muon_MT > 35 and mchain.muon_pt > 20.)):
#                if (options.channel=='muon' and mchain.muon_MT < 60. or \
#                    (options.channel=='electron' and mchain.muon_id and mchain.muon_reliso < 0.15 and mchain.muon_MT > 60)):

                    muon = tool.obj(mchain.muon_pt,
                               mchain.muon_eta,
                               mchain.muon_phi,
                               mchain.muon_mass,
                               mchain.muon_jetpt,
                               mchain.muon_njet,
                               mchain.muon_charge,
                               mchain.muon_trigmatch,
                               mchain.muon_trig_weight,
                               mchain.muon_id_weight,
                               mchain.muon_id,
                               mchain.muon_iso,
                               mchain.muon_reliso,
                               mchain.muon_MT)
                        
                    signal_muon.append(muon)


            for ie in xrange(ptr_e, ptr_e + nelectron):
                echain.LoadTree(ie)
                echain.GetEntry(ie)

#                print 'Yuta_e', ptr_e, echain.electron_MT, echain.electron_pt, echain.electron_id, echain.electron_iso

                if ((options.channel=='electron' and echain.electron_MT < 35.) or \
                    (options.channel=='muon' and echain.electron_id and echain.electron_iso and echain.electron_MT > 35.)):

#                if ((options.channel=='electron' and echain.electron_MT < 35. and echain.electron_pt > 20.) or \
#                    (options.channel=='muon' and echain.electron_id and echain.electron_iso and echain.electron_MT > 35. and echain.electron_pt > 20.)):
#                if (options.channel=='electron' and echain.electron_MT < 60. or \
#                    (options.channel=='muon' and echain.electron_id and echain.electron_iso and echain.electron_MT > 60.)):


                    electron = tool.obj(echain.electron_pt,
                                   echain.electron_eta,
                                   echain.electron_phi,
                                   echain.electron_mass,
                                   echain.electron_jetpt,
                                   echain.electron_njet,
                                   echain.electron_charge,
                                   echain.electron_trigmatch,
                                   echain.electron_trig_weight,
                                   echain.electron_id_weight,
                                   echain.electron_id,
                                   echain.electron_iso,
                                   echain.electron_reliso,
                                   echain.electron_MT                                   
                                   )
                    
                    signal_electron.append(electron)


            # e and mu should be 1


            if not (len(signal_muon)>=1 and len(signal_electron)>=1):
#                print 'Nmuon, Nelectron =', len(signal_muon), len(signal_electron)
                ptr_m += nmuon
                ptr_e += nelectron
                ptr_t += ntau
                ptr_vm += nvmuon
                ptr_ve += nvelectron
                ptr_vt += nvtau
                ptr_nb += nbjets
                ptr_nj += njets
                continue

            counter[2] += 1

            lepton_type = "None"

#            _muon_ = []
#            _electron_ = []
#
#
#            if options.channel=="electron":
#                _muon_ = [ii for ii in signal_muon if ii.pt > 10.]
#                _electron_ = [ii for ii in signal_electron if ii.pt > 10.]
#            elif options.channel=="muon":                
#                _muon_ = [ii for ii in signal_muon if ii.pt > 10.]
#                _electron_ = [ii for ii in signal_electron if ii.pt > 10.]



            
#            if not (len(signal_muon)==1 and len(signal_electron)==1):
#                ptr_m += nmuon
#                ptr_e += nelectron
#                ptr_t += ntau
#                ptr_vm += nvmuon
#                ptr_ve += nvelectron
#                ptr_vt += nvtau
#                ptr_nb += nbjets
#                continue

            muon = signal_muon
            electron = signal_electron
            

            #############################################
            # Tau 

            for it in xrange(ptr_t, ptr_t + ntau):
        
                tchain.LoadTree(it)
                tchain.GetEntry(it)

            
                if (tchain.tau_id and tchain.tau_iso):

                    tau = tool.tauobj(tchain.tau_pt,
                                      tchain.tau_eta,
                                      tchain.tau_phi,
                                      tchain.tau_mass,
                                      tchain.tau_charge,
                                      tchain.dBisolation,
                                      tchain.tau_againstMuTight,
                                      tchain.tau_againstEMedium,
                                      tchain.tau_decaymode,
                                      tchain.tau_ep
                                      )



#                    if tau.returnmindR(muon) < 0.5:
#                        continue
#
#                    if tau.returnmindR(electron) < 0.5:
#                        continue
#
#
#                    flag_mass_muon = False
#                    flag_mass_electron = False
#
#                    for imuon in muon:
#                        if tool.diobj(tau, imuon).returnmass() > 71.2 and tool.diobj(tau, imuon).returnmass() < 111.2:
#                            if not (tchain.tau_againstMuTight and
#                                    ((tchain.tau_decaymode==0 and tchain.tau_ep > 0.2) or (tchain.tau_decaymode!=0))):
#                                flag_mass_muon = True
#
#                    for ielectron in electron:
#                        if tool.diobj(tau, ielectron).returnmass() > 71.2 and tool.diobj(tau, ielectron).returnmass() < 111.2:
#                            if not tchain.tau_againstEMedium:
#                                flag_mass_electron = True
#                        
#                    if flag_mass_muon:
#                        continue
#                    
#                    if flag_mass_electron:
#                        continue

                    signal_tau.append(tau)

                    
            tau = signal_tau

            ptr_m += nmuon
            ptr_e += nelectron
            ptr_t += ntau


#            if len(signal_tau)>=1:
#                ptr_vm += nvmuon
#                ptr_ve += nvelectron
#                ptr_vt += nvtau
#                ptr_nb += nbjets
#                ptr_nj += njets
#                continue
#
#            counter[3] += 1


            #  VETO
            ######################

            veto_muon = []
            veto_electron = []
            veto_tau = []           
            veto_bjet = []
            veto_jet = []
            
            for im in xrange(ptr_vm, ptr_vm + nvmuon):
        
                vmchain.LoadTree(im)
                vmchain.GetEntry(im)

                vm = tool.easyobj(vmchain.veto_muon_pt,
                                  vmchain.veto_muon_eta,
                                  vmchain.veto_muon_phi)
                veto_muon.append(vm)
                
#                if vm.returndR(muon) > 0.4 and \
#                       vm.returndR(electron) > 0.4:


                

            for ie in xrange(ptr_ve, ptr_ve + nvelectron):
            
                vechain.LoadTree(ie)
                vechain.GetEntry(ie)

                ve = tool.easyobj(vechain.veto_electron_pt,
                                  vechain.veto_electron_eta,
                                  vechain.veto_electron_phi)
                veto_electron.append(ve)
                
#                if ve.returndR(muon) > 0.4 and \
#                       ve.returndR(electron) > 0.4:

                    

            for it in xrange(ptr_vt, ptr_vt + nvtau):
        
                vtchain.LoadTree(it)
                vtchain.GetEntry(it)
                
                vt = tool.easyobj(vtchain.veto_tau_pt,
                             vtchain.veto_tau_eta,
                             vtchain.veto_tau_phi)
                veto_tau.append(vt)
                
#                if vt.returndR(muon) > 0.4 and \
#                       vt.returndR(electron) > 0.4:
                    




            for ib in xrange(ptr_nb, ptr_nb+nbjets):

                bchain.LoadTree(ib)
                bchain.GetEntry(ib)

                bj = tool.easyobj(bchain.bjet_pt,
                             bchain.bjet_eta,
                             bchain.bjet_phi)

                if bj.pt > 20 and abs(bj.eta) < 2.4:
#                print 'bjet = ', bj.pt, bj.eta
#                if bj.pt > 20 and abs(bj.eta) < 2.4 and  bj.returndR(muon) > 0.4 and bj.returndR(electron) > 0.4:

                    veto_bjet.append(bj)



            
            for ij in xrange(ptr_nj, ptr_nj+njets):

                jchain.LoadTree(ij)
                jchain.GetEntry(ij)

                jj = tool.easyobj(jchain.jet_pt,
                                  jchain.jet_eta,
                                  jchain.jet_phi)

                if jj.pt > 20 and abs(jj.eta) < 5.0 and jchain.jet_looseJetId:

                    veto_jet.append(jj)

                    
            ptr_vm += nvmuon
            ptr_ve += nvelectron
            ptr_vt += nvtau
            ptr_nb += nbjets
            ptr_nj += njets


#            if options.channel=='muon':
#                if not len(electron)==1:
#                    continue
#
#            elif options.channel=='electron':
#                if not len(muon)==1:
#                    continue

            counter[4] += 1

            selectedLeptons = []

            for imuon in muon:
                for ielectron in electron:

                    if not imuon.charge*ielectron.charge==1:
                        continue

                        # Trigger matching
                        # Mu8_Ele17 : Trig_type = 1
                        # Mu17_Ele8 : Trig_type = 2

                    if not ((main.trig_type_M17E8 and imuon.pt > 20. and ielectron.pt > 10.) or \
                            (main.trig_type_M8E17 and imuon.pt > 10. and ielectron.pt > 20.)):
                        
                        continue
                    
                    if not (imuon.trigmatch and ielectron.trigmatch):
                        continue
#                            (main.trig_type_M8E17 and imuon.pt > 10. and ielectron.pt > 20. and imuon.trigmatch and ielectron.trigmatch)
#                            ):
                        


#                    if tool.diobj(imuon, ielectron).returnmass() < 20:
#                        continue

                    counter_tau = 0
                    for itau in tau:
                        
#                        if not itau.charge*imuon.charge==-1:
#                            continue
                    
                        if itau.returndR(imuon) < 0.5:
                            continue
                        
                        if itau.returndR(ielectron) < 0.5:
                            continue
                        
                        if tool.diobj(itau, imuon).returnmass() > 71.2 and tool.diobj(itau, imuon).returnmass() < 111.2:
                            if not (itau.againstMuTight and
                                    ((itau.decaymode==0 and itau.ep > 0.2) or (itau.decaymode!=0))):
                                
                                continue

                        if tool.diobj(itau, ielectron).returnmass() > 71.2 and tool.diobj(itau, ielectron).returnmass() < 111.2:
                            if not itau.againstEMedium:
                                continue
                        
                        # calculate M(l2,tau) => soft-lepton + tau
#                        Mass = -1
#                        if imuon.pt < ielectron.pt:
#                            Mass = tool.diobj(imuon, itau).returnmass()
#                        elif imuon.pt > ielectron.pt:
#                            Mass = tool.diobj(ielectron, itau).returnmass()
#                

 #                       if Mass < 20.:
 #                           continue



                        counter_tau += 1

                    if counter_tau >= 1:
                        continue
                        


#                    smuon.append(imuon)
#                    selectron.append(ielectron)
                    selectedLeptons.append((imuon, ielectron))
                    


            if not (len(selectedLeptons) >= 1):
#            if not (len(smuon) >= 1 and len(selectron) >= 1):
#                import pdb; pdb.set_trace()
                continue
            
            counter[5] += 1
            
            vmuon = []
            velectron = []
            vtau = []
            
            for iv in veto_muon:            
                if iv.returnmindR(muon) > 0.4 and \
                       iv.returnmindR(electron) > 0.4:
                    vmuon.append(iv)

            for iv in veto_electron:            
                if iv.returnmindR(muon) > 0.4 and \
                       iv.returnmindR(electron) > 0.4:
                    
                    velectron.append(iv)


            for iv in veto_tau:            
                if iv.returnmindR(muon) > 0.4 and \
                       iv.returnmindR(electron) > 0.4:
                    vtau.append(iv)

#            if not (len(vmuon)==0 and len(velectron)==0:
            if not (len(vmuon)==0 and len(velectron)==0 and len(vtau)==0):
                continue

            counter[6] += 1


            # bjet
            count_bjet = 0
            for bj in veto_bjet:
                if bj.returnmindR(muon) > 0.4 and bj.returnmindR(electron) > 0.4:
                    count_bjet += 1
                            
#            if not count_bjet >= 2:
            if count_bjet >= 1:
                continue

            counter[7] += 1

            count_njet = 0
            for jj in veto_jet:
                if jj.returnmindR(muon) > 0.4 and jj.returnmindR(electron) > 0.4:
                    count_njet += 1
                            
            if not count_njet >= 1:
                continue



#            if not main.nJets >= 3:
#                continue

            counter[8] += 1

            counter_pass = 0

            for imuon, ielectron in selectedLeptons:

                weight = 1.
                weight_raw = 1.
                weight_muid = 1.
                weight_eid = 1.
                weight_mutrig = 1.
                weight_etrig = 1.
                
                if pname == 'data':
                    pass
                else:
                    weight = main.weight*imuon.trig*imuon.id*ielectron.trig*ielectron.id*lum_weight
                    weight_raw = lum_weight
                    weight_muid = imuon.id
                    weight_eid = ielectron.id
                    weight_mutrig = imuon.trig
                    weight_etrig = ielectron.trig
                    
                if options.channel=="electron":
                    lepton_pt    [0] = ielectron.pt
                    lepton_eta   [0] = ielectron.eta
                    lepton_phi   [0] = ielectron.phi
                    lepton_mass  [0] = ielectron.mass
                    lepton_jetpt [0] = ielectron.jetpt
                    lepton_njet  [0] = ielectron.njet
                    lepton_id    [0] = ielectron.isid 
                    lepton_iso   [0] = ielectron.isiso
                    lepton_reliso[0] = ielectron.reliso
                    lepton_MT    [0] = ielectron.MT
                    lepton_charge[0] = ielectron.charge
                    lepton_dpt   [0] = ielectron.jetpt - ielectron.pt
                    lepton_kNN_jetpt [0] = ielectron.jetpt
                    
                    slepton_pt    [0] = imuon.pt
                    slepton_eta   [0] = imuon.eta
                    slepton_phi   [0] = imuon.phi
                    slepton_mass  [0] = imuon.mass
                    slepton_jetpt [0] = imuon.jetpt
                    slepton_njet  [0] = imuon.njet
                    slepton_id    [0] = imuon.isid 
                    slepton_iso   [0] = imuon.isiso
                    slepton_reliso[0] = imuon.reliso
                    slepton_MT    [0] = imuon.MT
                    slepton_charge[0] = imuon.charge
                    slepton_dpt   [0] = imuon.jetpt - imuon.pt
                    slepton_kNN_jetpt [0] = imuon.jetpt
                    
                    if ielectron.jetpt == -999:
                        lepton_kNN_jetpt [0] = ielectron.pt
                        
                    if ielectron.jetpt < ielectron.pt:
                        lepton_kNN_jetpt [0] = ielectron.pt
                    
                elif options.channel=="muon":
                    lepton_pt    [0] = imuon.pt
                    lepton_eta   [0] = imuon.eta
                    lepton_phi   [0] = imuon.phi
                    lepton_mass  [0] = imuon.mass
                    lepton_jetpt [0] = imuon.jetpt
                    lepton_njet  [0] = imuon.njet
                    lepton_id    [0] = imuon.isid 
                    lepton_iso   [0] = imuon.isiso
                    lepton_reliso[0] = imuon.reliso
                    lepton_MT    [0] = imuon.MT
                    lepton_charge[0] = imuon.charge
                    lepton_dpt   [0] = imuon.jetpt - imuon.pt
                    lepton_kNN_jetpt [0] = imuon.jetpt
                    
                    slepton_pt    [0] = ielectron.pt
                    slepton_eta   [0] = ielectron.eta
                    slepton_phi   [0] = ielectron.phi
                    slepton_mass  [0] = ielectron.mass
                    slepton_jetpt [0] = ielectron.jetpt
                    slepton_njet  [0] = ielectron.njet
                    slepton_id    [0] = ielectron.isid 
                    slepton_iso   [0] = ielectron.isiso
                    slepton_reliso[0] = ielectron.reliso
                    slepton_MT    [0] = ielectron.MT
                    slepton_charge[0] = ielectron.charge
                    slepton_dpt   [0] = ielectron.jetpt - ielectron.pt
                    slepton_kNN_jetpt [0] = ielectron.jetpt
                    
                    if imuon.jetpt == -999:
                        lepton_kNN_jetpt [0] = imuon.pt
                            
                    if imuon.jetpt < imuon.pt:
                        lepton_kNN_jetpt [0] = imuon.pt

                            
                isMC = False
                isMCw = 1.
            
                if pname == 'data':
                    pass
                else:
                    isMC = True
                    isMCw = -1.

                evt_weight[0] = weight
                evt_weight_raw[0] = weight_raw
                
                evt_Mem   [0] = tool.diobj(imuon, ielectron).returnmass()
                evt_njet [0] = main.nJets
                evt_id [0] = ptype
                evt_isMC [0] = isMC
                evt_isMCw [0] = isMCw
                evt_run[0] = main.run
                evt_evt[0] = main.evt
                evt_lum[0] = main.lumi
                evt_met[0] = main.pfmet
                    
                evt_weight_muid[0] = weight_muid
                evt_weight_mutrig[0] = weight_mutrig
                evt_weight_eid[0] = weight_eid
                evt_weight_etrig[0] = weight_etrig
                
                evt_dphi_mu_met[0] = imuon.phi
                evt_dphi_e_met[0] = ielectron.phi
                evt_M_mujet[0] = 1.
                evt_M_ejet[0] = 1.
#                    evt_dphi_mu_met[0] = imuon.phi() - main.met_phi
#                    evt_dphi_e_met[0] = ielectron.phi() - main.met_phi
#                    evt_M_mujet[0] = tool.diobject(imuon, jet[0]).returnmass()
#                    evt_M_ejet[0] = tool.diobject(ielectron, jet[0]).returnmass()
                    
                t.Fill()
                counter_pass += 1



            if counter_pass >= 1:
                line = str(int(main.run))+':'+str(int(main.lumi))+':'+str(int(main.evt))+'\n'
                fw.write(line)

            Passed += 1


        print '[INFO] pass, total, eff = ', Passed, '/' , Total
        fw.close()

        for ic in range(len(counter)):
            print '[INFO] cutflow : ', ic, counter[ic]

        ofile.Write()
        ofile.Close()
