#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "RecoTauTag/RecoTau/interface/RecoTauQualityCuts.h"
#include "RecoTauTag/RecoTau/interface/RecoTauVertexAssociator.h"

#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/TauReco/interface/PFTau.h"
#include "DataFormats/TauReco/interface/PFTauFwd.h"
#include "DataFormats/TauReco/interface/PFTauDiscriminator.h"
#include "DataFormats/TrackReco/interface/Track.h"

#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/JetReco/interface/GenJetCollection.h"

#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"

#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/GsfTrackReco/interface/GsfTrack.h"

#include <vector>
#include <string>
#include <sstream>

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1.h"
#include "TProfile.h"
#include "TProfile2D.h"
#include "TH1F.h"
#include "TH2D.h"
#include "TH1D.h"
#include "TTree.h"
#include "TFile.h"

typedef edm::View<reco::GenJet> GenJetView;

class RecoTauDifferenceAnalyzer : public edm::EDFilter {

public:
  explicit RecoTauDifferenceAnalyzer(const edm::ParameterSet& pset);
  virtual ~RecoTauDifferenceAnalyzer() {}
  virtual bool filter(edm::Event& evt, const edm::EventSetup& es);
  virtual void endJob();

private:
  reco::tau::RecoTauQualityCuts qcuts_;
  std::auto_ptr<reco::tau::RecoTauVertexAssociator> vertexAssociator_;
  edm::InputTag src1_;
  edm::InputTag src2_;
  edm::InputTag disc1_;
  edm::InputTag disc2_;
  edm::InputTag jetSrc_;
  edm::InputTag jetSrcCHS_;
  edm::InputTag genSrc_;
  edm::InputTag genTauSrc_;

  double matchingDistance_;

  edm::InputTag vertexTag_;
  edm::InputTag chIso1_;
  edm::InputTag chIso2_;
  edm::InputTag nIso1_;
  edm::InputTag nIso2_;
  edm::InputTag PUIso1_;
  edm::InputTag PUIso2_;
  edm::InputTag cmbIso1_;
  edm::InputTag cmbIso2_;

  /* branch definition */

  TTree* isoTuple_;
  TTree* eventTuple_;
  TTree* genTuple_;
  ULong64_t _eventNum_;
  UChar_t _nVx_;
  UChar_t _type_;

  Float_t  _pt_;
  Float_t _eta_;
  Float_t _phi_;
  Float_t _m_;
  Float_t _chIso_;
  Float_t _nIso_;
  Float_t _puIso_;
  Float_t _cmbIso_;
  Float_t _vz_;
  Float_t _track_pt_;
  Float_t _track_eta_;
  Float_t _track_phi_;
  Float_t _track_chi_;
  Float_t _track_dz_;
  Float_t _track_dxy_;
  Float_t _closest_dr_;
  Float_t _closest_dr_CHS_;
  Int_t _track_nhit_;
  Int_t  _match_;
  Int_t  _dmf_;
  Int_t  _ncharged_;
  Int_t  _npizero_;
  
  Float_t  _pt2_;
  Float_t _eta2_;
  Float_t _phi2_;
  Float_t _m2_;
  Float_t _chIso2_;
  Float_t _nIso2_;
  Float_t _puIso2_;
  Float_t _cmbIso2_;
  Float_t _vz2_;
  Float_t _track_pt2_;
  Float_t _track_eta2_;
  Float_t _track_phi2_;
  Float_t _track_chi2_;
  Float_t _track_dz2_;
  Float_t _track_dxy2_;
  Float_t _closest_dr2_;
  Float_t _closest_dr2_CHS_;
  Int_t _track_nhit2_;
  Int_t  _match2_;
  Int_t  _dmf2_;
  Int_t  _ncharged2_;
  Int_t  _npizero2_;

  Int_t _nak5jet_;
  Int_t _nak5jetCHS_;
  Int_t _ntau_;
  Int_t _ntauCHS_;
  Int_t _ngentau_;

  Float_t _genTau_pt_;
  Float_t _genTau_eta_;
  Float_t _genTau_phi_;
  Float_t _genTau_mass_;
  Float_t _genTau_z_;
  Float_t _vertex_z_;
  Float_t _genTau_vertex_dz_;

  Int_t _Tau1_match_;
  Float_t _Tau1_pt_;
  Float_t _Tau1_eta_;
  Float_t _Tau1_phi_;
  Float_t _Tau1_mass_;
  Float_t _Tau1_dR_;
  Float_t _Tau1_chIso_;
  Float_t _Tau1_nIso_;
  Float_t _Tau1_puIso_;
  Float_t _Tau1_cmbIso_;
  Float_t _Tau1_vz_;
  Float_t _Tau1_track_pt_;
  Float_t _Tau1_track_eta_;
  Float_t _Tau1_track_phi_;
  Float_t _Tau1_track_chi_;
  Float_t _Tau1_track_nhit_;
  Float_t _Tau1_track_dz_;
  Float_t _Tau1_track_dxy_;
  Float_t _Tau1_z_;
  Int_t _Tau1_dmf_;
  Int_t _Tau1_dmfraw_;
  Int_t _Tau1_ncharged_;
  Int_t _Tau1_npizero_;


  Int_t _Tau2_match_;
  Float_t _Tau2_pt_;
  Float_t _Tau2_eta_;
  Float_t _Tau2_phi_;
  Float_t _Tau2_mass_;
  Float_t _Tau2_dR_;
  Float_t _Tau2_chIso_;
  Float_t _Tau2_nIso_;
  Float_t _Tau2_puIso_;
  Float_t _Tau2_cmbIso_;
  Float_t _Tau2_vz_;
  Float_t _Tau2_track_pt_;
  Float_t _Tau2_track_eta_;
  Float_t _Tau2_track_phi_;
  Float_t _Tau2_track_chi_;
  Float_t _Tau2_track_nhit_;
  Float_t _Tau2_track_dz_;
  Float_t _Tau2_track_dxy_;
  Float_t _Tau2_z_;
  Int_t _Tau2_dmf_;
  Int_t _Tau2_dmfraw_;
  Int_t _Tau2_ncharged_;
  Int_t _Tau2_npizero_;



};

RecoTauDifferenceAnalyzer::RecoTauDifferenceAnalyzer(const edm::ParameterSet& pset): 
  qcuts_(pset.exists("qualityCuts") ? pset.getParameterSet("qualityCuts").getParameterSet("isolationQualityCuts") : pset.getParameterSet("qualityCuts")){

  src1_ = pset.getParameter<edm::InputTag>("src1");
  src2_ = pset.getParameter<edm::InputTag>("src2");
  disc1_ = pset.getParameter<edm::InputTag>("disc1");
  disc2_ = pset.getParameter<edm::InputTag>("disc2");
  
  vertexAssociator_.reset(new reco::tau::RecoTauVertexAssociator(pset.getParameterSet("qualityCuts"),consumesCollector()));
  
  if(pset.exists("genSrc")) genSrc_= pset.getParameter<edm::InputTag>("genSrc");
  if(pset.exists("genTauSrc")) genTauSrc_ = pset.getParameter<edm::InputTag>("genTauSrc");
  if(pset.exists("jetSrc")) jetSrc_ = pset.getParameter<edm::InputTag>("jetSrc");
  if(pset.exists("jetSrcCHS")) jetSrcCHS_ = pset.getParameter<edm::InputTag>("jetSrcCHS");
  matchingDistance_ = pset.exists("matchingDistance") ? pset.getParameter<double>("matchingDistance"): 0.1 ;
  vertexTag_ = edm::InputTag("offlinePrimaryVertices", "");
  if(pset.exists("primaryVertexSrc")) vertexTag_ = pset.getParameter<edm::InputTag>("primaryVertexSrc");
  
  chIso1_ = pset.exists("chIso1") ? pset.getParameter<edm::InputTag>("chIso1"): pset.getParameter<edm::InputTag>("disc1");
  chIso2_ = pset.exists("chIso2") ? pset.getParameter<edm::InputTag>("chIso2"): pset.getParameter<edm::InputTag>("disc2");
  nIso1_ = pset.exists("nIso1") ? pset.getParameter<edm::InputTag>("nIso1"): pset.getParameter<edm::InputTag>("disc1");
  nIso2_ = pset.exists("nIso2") ? pset.getParameter<edm::InputTag>("nIso2"): pset.getParameter<edm::InputTag>("disc2");
  PUIso1_ = pset.exists("PUIso1") ? pset.getParameter<edm::InputTag>("PUIso1"): pset.getParameter<edm::InputTag>("disc1");
  PUIso2_ = pset.exists("PUIso2") ? pset.getParameter<edm::InputTag>("PUIso2"): pset.getParameter<edm::InputTag>("disc2");
  cmbIso1_ = pset.exists("cmbIso1") ? pset.getParameter<edm::InputTag>("cmbIso1"): pset.getParameter<edm::InputTag>("disc1");
  cmbIso2_ = pset.exists("cmbIso2") ? pset.getParameter<edm::InputTag>("cmbIso2"): pset.getParameter<edm::InputTag>("disc2");


  isoTuple_= new TTree("isoTuple","isoTuple");
  isoTuple_->Branch("nVx",&_nVx_, "_nVx_/b");
  isoTuple_->Branch("type",&_type_, "_type_/b");
  isoTuple_->Branch("_eventNum_",&_eventNum_,"_eventNum_/l");

  isoTuple_->Branch("pt",&_pt_,"_pt_/F");
  isoTuple_->Branch("eta", &_eta_,"_eta_/F");
  isoTuple_->Branch("phi",&_phi_, "_phi_/F");
  isoTuple_->Branch("m",&_m_, "_m_/F");
  isoTuple_->Branch("chIso",&_chIso_, "_chIso_/F");
  isoTuple_->Branch("nIso",&_nIso_, "_nIso_/F");
  isoTuple_->Branch("puIso",&_puIso_, "_puIso_/F");
  isoTuple_->Branch("cmbIso",&_cmbIso_, "_cmbIso_/F");
  isoTuple_->Branch("vz",&_vz_, "_vz_/F");
  isoTuple_->Branch("closest_dr",&_closest_dr_, "_closest_dr_/F");
  isoTuple_->Branch("closest_dr_CHS",&_closest_dr_CHS_, "_closest_dr_CHS_/F");
  isoTuple_->Branch("track_pt",&_track_pt_, "_track_pt_/F");
  isoTuple_->Branch("track_eta",&_track_eta_, "_track_eta_/F");
  isoTuple_->Branch("track_phi",&_track_phi_, "_track_phi_/F");
  isoTuple_->Branch("track_chi",&_track_chi_, "_track_chi_/F");
  isoTuple_->Branch("track_nhit",&_track_nhit_, "_track_nhit_/I");


  isoTuple_->Branch("match",&_match_, "_match_/I");
  isoTuple_->Branch("dmf",&_dmf_, "_dmf_/I");
  isoTuple_->Branch("ncharged",&_ncharged_, "_ncharged_/I");
  isoTuple_->Branch("npizero",&_npizero_, "_npizero_/I");
  isoTuple_->Branch("pt2",&_pt2_,"_pt2_/F");
  isoTuple_->Branch("eta", &_eta2_,"_eta2_/F");
  isoTuple_->Branch("phi2",&_phi2_, "_phi2_/F");
  isoTuple_->Branch("m2",&_m2_, "_m2_/F");
  isoTuple_->Branch("chIso2",&_chIso2_, "_chIso2_/F");
  isoTuple_->Branch("nIso2",&_nIso2_, "_nIso2_/F");
  isoTuple_->Branch("puIso2",&_puIso2_, "_puIso2_/F");
  isoTuple_->Branch("cmbIso2",&_cmbIso2_, "_cmbIso2_/F");
  isoTuple_->Branch("vz2",&_vz2_, "_vz2_/F");
  isoTuple_->Branch("closest_dr2",&_closest_dr2_, "_closest_dr2_/F");
  isoTuple_->Branch("closest_dr2_CHS",&_closest_dr2_CHS_, "_closest_dr2_CHS_/F");
  isoTuple_->Branch("match2",&_match2_, "_match2_/I");
  isoTuple_->Branch("dmf2",&_dmf2_, "_dmf2_/I");
  isoTuple_->Branch("ncharged2",&_ncharged2_, "_ncharged2_/I");
  isoTuple_->Branch("npizero2",&_npizero2_, "_npizero2_/I");
  isoTuple_->Branch("track_pt2",&_track_pt2_, "_track_pt2_/F");
  isoTuple_->Branch("track_eta2",&_track_eta2_, "_track_eta2_/F");
  isoTuple_->Branch("track_phi2",&_track_phi2_, "_track_phi2_/F");
  isoTuple_->Branch("track_chi2",&_track_chi2_, "_track_chi2_/F");
  isoTuple_->Branch("track_nhit2",&_track_nhit2_, "_track_nhit2_/I");

  eventTuple_= new TTree("eventTuple","eventTuple");
  eventTuple_->Branch("nak5jet",&_nak5jet_, "_nak5jet_/I");
  eventTuple_->Branch("nak5jetCHS",&_nak5jetCHS_, "_nak5jetCHS_/I");
  eventTuple_->Branch("ntau",&_ntau_, "_ntau_/I");
  eventTuple_->Branch("ntauCHS",&_ntauCHS_, "_ntauCHS_/I");
  eventTuple_->Branch("ngentau",&_ngentau_, "_ngentau_/I");

  genTuple_= new TTree("genTuple","genTuple");
  genTuple_->Branch("genTau_pt",&_genTau_pt_, "_genTau_pt_/F");
  genTuple_->Branch("genTau_eta",&_genTau_eta_, "_genTau_eta_/F");
  genTuple_->Branch("genTau_phi",&_genTau_phi_, "_genTau_phi_/F");
  genTuple_->Branch("genTau_mass",&_genTau_mass_, "_genTau_mass_/F");
  genTuple_->Branch("genTau_z",&_genTau_z_, "_genTau_z_/F");
  genTuple_->Branch("vertex_z",&_vertex_z_, "_vertex_z_/F");
  genTuple_->Branch("genTau_vertex_dz",&_genTau_vertex_dz_, "_genTau_vertex_dz_/F");

  genTuple_->Branch("Tau1_match",&_Tau1_match_, "_Tau1_match_/I");
  genTuple_->Branch("Tau1_pt",&_Tau1_pt_, "_Tau1_pt_/F");
  genTuple_->Branch("Tau1_eta",&_Tau1_eta_, "_Tau1_eta_/F");
  genTuple_->Branch("Tau1_phi",&_Tau1_phi_, "_Tau1_phi_/F");
  genTuple_->Branch("Tau1_mass",&_Tau1_mass_, "_Tau1_mass_/F");
  genTuple_->Branch("Tau1_dR",&_Tau1_dR_, "_Tau1_dR_/F");
  genTuple_->Branch("Tau1_chIso",&_Tau1_chIso_, "_Tau1_chIso_/F");
  genTuple_->Branch("Tau1_nIso",&_Tau1_nIso_, "_Tau1_nIso_/F");
  genTuple_->Branch("Tau1_puIso",&_Tau1_puIso_, "_Tau1_puIso_/F");
  genTuple_->Branch("Tau1_cmbIso",&_Tau1_cmbIso_, "_Tau1_cmbIso_/F");
  genTuple_->Branch("Tau1_vz",&_Tau1_vz_, "_Tau1_vz_/F");
  genTuple_->Branch("Tau1_track_pt",&_Tau1_track_pt_, "_Tau1_track_pt_/F");
  genTuple_->Branch("Tau1_track_eta",&_Tau1_track_eta_, "_Tau1_track_eta_/F");
  genTuple_->Branch("Tau1_track_phi",&_Tau1_track_phi_, "_Tau1_track_phi_/F");
  genTuple_->Branch("Tau1_track_chi",&_Tau1_track_chi_, "_Tau1_track_chi_/F");
  genTuple_->Branch("Tau1_track_nhit",&_Tau1_track_nhit_, "_Tau1_track_nhit_/I");
  genTuple_->Branch("Tau1_track_dz",&_Tau1_track_dz_, "_Tau1_track_dz_/I");
  genTuple_->Branch("Tau1_track_dxy",&_Tau1_track_dxy_, "_Tau1_track_dxy_/I");
  genTuple_->Branch("Tau1_z",&_Tau1_z_, "_Tau1_z_/F");
  genTuple_->Branch("Tau1_dmf",&_Tau1_dmf_, "_Tau1_dmf_/I");
  genTuple_->Branch("Tau1_dmfraw",&_Tau1_dmfraw_, "_Tau1_dmfraw_/I");
  genTuple_->Branch("Tau1_ncharged",&_Tau1_ncharged_, "_Tau1_ncharged_/I");
  genTuple_->Branch("Tau1_npizero",&_Tau1_npizero_, "_Tau1_npizero_/I");


  genTuple_->Branch("Tau2_match",&_Tau2_match_, "_Tau2_match_/I");
  genTuple_->Branch("Tau2_pt",&_Tau2_pt_, "_Tau2_pt_/F");
  genTuple_->Branch("Tau2_eta",&_Tau2_eta_, "_Tau2_eta_/F");
  genTuple_->Branch("Tau2_phi",&_Tau2_phi_, "_Tau2_phi_/F");
  genTuple_->Branch("Tau2_mass",&_Tau2_mass_, "_Tau2_mass_/F");
  genTuple_->Branch("Tau2_dR",&_Tau2_dR_, "_Tau2_dR_/F");
  genTuple_->Branch("Tau2_chIso",&_Tau2_chIso_, "_Tau2_chIso_/F");
  genTuple_->Branch("Tau2_nIso",&_Tau2_nIso_, "_Tau2_nIso_/F");
  genTuple_->Branch("Tau2_puIso",&_Tau2_puIso_, "_Tau2_puIso_/F");
  genTuple_->Branch("Tau2_cmbIso",&_Tau2_cmbIso_, "_Tau2_cmbIso_/F");
  genTuple_->Branch("Tau2_vz",&_Tau2_vz_, "_Tau2_vz_/F");
  genTuple_->Branch("Tau2_track_pt",&_Tau2_track_pt_, "_Tau2_track_pt_/F");
  genTuple_->Branch("Tau2_track_eta",&_Tau2_track_eta_, "_Tau2_track_eta_/F");
  genTuple_->Branch("Tau2_track_phi",&_Tau2_track_phi_, "_Tau2_track_phi_/F");
  genTuple_->Branch("Tau2_track_chi",&_Tau2_track_chi_, "_Tau2_track_chi_/F");
  genTuple_->Branch("Tau2_track_nhit",&_Tau2_track_nhit_, "_Tau2_track_nhit_/I");
  genTuple_->Branch("Tau2_track_dz",&_Tau2_track_dz_, "_Tau2_track_dz_/I");
  genTuple_->Branch("Tau2_track_dxy",&_Tau2_track_dxy_, "_Tau2_track_dxy_/I");
  genTuple_->Branch("Tau2_z",&_Tau2_z_, "_Tau2_z_/F");
  genTuple_->Branch("Tau2_dmf",&_Tau2_dmf_, "_Tau2_dmf_/I");
  genTuple_->Branch("Tau2_dmfraw",&_Tau2_dmfraw_, "_Tau2_dmfraw_/I");
  genTuple_->Branch("Tau2_ncharged",&_Tau2_ncharged_, "_Tau2_ncharged_/I");
  genTuple_->Branch("Tau2_npizero",&_Tau2_npizero_, "_Tau2_npizero_/I");




}

namespace {
  reco::PFJetRef getJetRef(const reco::PFTau& tau) {
    if (tau.jetRef().isNonnull())
      return tau.jetRef();
    else if (tau.pfTauTagInfoRef()->pfjetRef().isNonnull())
      return tau.pfTauTagInfoRef()->pfjetRef();
    else throw cms::Exception("cant find jet ref");
  }
}

bool RecoTauDifferenceAnalyzer::filter(edm::Event& evt, const edm::EventSetup& es) {


  edm::Handle<reco::PFTauCollection> taus1;
  evt.getByLabel(src1_, taus1);
  edm::Handle<reco::PFTauCollection> taus2;
  evt.getByLabel(src2_, taus2);
  edm::Handle<reco::GenParticleCollection> genParticles;
  evt.getByLabel(genSrc_, genParticles);
  edm::Handle<std::vector<reco::GenJet> > genTaus;
  evt.getByLabel(genTauSrc_, genTaus);

  edm::Handle<std::vector<reco::PFJet> > ak5jet;
  evt.getByLabel(jetSrc_, ak5jet);

  edm::Handle<std::vector<reco::PFJet> > ak5jetCHS;
  evt.getByLabel(jetSrcCHS_, ak5jetCHS);

  edm::Handle<reco::PFTauDiscriminator> disc1;
  evt.getByLabel(disc1_, disc1);
  edm::Handle<reco::PFTauDiscriminator> disc2;
  evt.getByLabel(disc2_, disc2);
  edm::Handle<reco::PFTauDiscriminator> chIso1;
  evt.getByLabel(chIso1_,chIso1);
  edm::Handle<reco::PFTauDiscriminator> chIso2;
  evt.getByLabel(chIso2_,chIso2);
  edm::Handle<reco::PFTauDiscriminator> nIso1;
  evt.getByLabel(nIso1_,nIso1);
  edm::Handle<reco::PFTauDiscriminator> nIso2;
  evt.getByLabel(nIso2_,nIso2);
  edm::Handle<reco::PFTauDiscriminator> PUIso1;
  evt.getByLabel(PUIso1_,PUIso1);
  edm::Handle<reco::PFTauDiscriminator> PUIso2;
  evt.getByLabel(PUIso2_,PUIso2);
  edm::Handle<reco::PFTauDiscriminator> cmbIso1;
  evt.getByLabel(cmbIso1_,cmbIso1);
  edm::Handle<reco::PFTauDiscriminator> cmbIso2;
  evt.getByLabel(cmbIso2_,cmbIso2);

  edm::Handle<reco::VertexCollection> verticesH_;
  evt.getByLabel(vertexTag_, verticesH_);
  int nVx = verticesH_->size();
  vertexAssociator_->setEvent(evt);
  reco::Vertex::Point evtVertexPos;
  if ( verticesH_->size() > 0 ){
    evtVertexPos = verticesH_->front().position();
    //std::cout << "check vertex Z : " << evtVertexPos.Z() << std::endl;
  }
  
  
  
  
  // First, produce generator trees

  for(size_t i = 0; i < genTaus->size(); ++ i){
      
    const reco::GenJet & TauCand = (*genTaus)[i];
    reco::Particle::LorentzVector visibleP4 = ((*genTaus)[i]).p4();
      
    if(visibleP4.pt() < 5.0) continue;
    
    const std::vector <const reco::GenParticle*> mRefs = TauCand.getGenConstituents();
    unsigned int decayMode = 0; // 0 = hadronic, 1=electron, 2=muon 
    Float_t tau_z = -999;

    for(size_t igTauD =0; igTauD < mRefs.size(); igTauD++) {
      if(abs(mRefs[igTauD]->pdgId())==11) decayMode = 1;
      if(abs(mRefs[igTauD]->pdgId())==13) decayMode = 2;

      //      std::cout << "vertex : " << mRefs[igTauD]->vertex().z() << " " << TauCand.vertex().z() << std::endl;
      tau_z = mRefs[igTauD]->vertex().z();
    }
    
    if(decayMode!=0) continue; 

    bool match1 = false;
    reco::PFTauRef bestMatch1;
    Float_t min_dR1 = 1000;

    for (size_t iTau1 = 0; iTau1 < taus1->size(); ++iTau1) {
      reco::PFTauRef tau1(taus1, iTau1);
      //      if(tau1->pt() < 5.) continue;
      
      double dR_MC = deltaR(tau1->p4(),((*genTaus)[i]).p4());
      
      //      if(dR_MC < min_dR1 && dR_MC < 0.1){
      if(dR_MC < min_dR1){
	match1 = true;
	bestMatch1 = tau1;
	min_dR1 = dR_MC;
      }
    }

    bool match2 = false;
    reco::PFTauRef bestMatch2;
    Float_t min_dR2 = 1000;

    for (size_t iTau2 = 0; iTau2 < taus2->size(); ++iTau2) {
      reco::PFTauRef tau2(taus2, iTau2);
      //if(tau2->pt() < 5.) continue;
      
      double dR_MC = deltaR(tau2->p4(),((*genTaus)[i]).p4());
      
      //      if(dR_MC < min_dR2 && dR_MC < 0.1){
      if(dR_MC < min_dR2){
	match2 = true;
	bestMatch2 = tau2;
	min_dR2 = dR_MC;
      }
    }


    std::cout << "check1" << std::endl;
    
    _genTau_pt_ = visibleP4.pt();
    _genTau_eta_ = visibleP4.eta();
    _genTau_phi_ = visibleP4.phi();
    _genTau_mass_ = visibleP4.mass();
    _genTau_z_ = tau_z;

    if ( verticesH_->size() > 0 ){
      _vertex_z_ = evtVertexPos.Z();
      _genTau_vertex_dz_ = tau_z - _vertex_z_;
    }else{
      _vertex_z_ = -99;
      _genTau_vertex_dz_ = -99;
    }
    

    _Tau1_match_ = (Int_t)match1;
    _Tau2_match_ = (Int_t)match2;


    _Tau1_dmf_ = -99;
    _Tau1_dmfraw_ = -99;
    _Tau1_pt_ = -99;
    _Tau1_eta_ = -99;
    _Tau1_phi_ = -99;
    _Tau1_mass_ = -99;
    _Tau1_dR_ = -99;
    _Tau1_chIso_ = -99;
    _Tau1_nIso_ = -99;
    _Tau1_puIso_ = -99;
    _Tau1_cmbIso_ = -99;
    _Tau1_ncharged_ = -99;
    _Tau1_npizero_ = -99;    
    _Tau1_vz_ =  -99;
    _Tau1_track_pt_ = -99; 
    _Tau1_track_eta_ = -99;
    _Tau1_track_phi_ = -99;
    _Tau1_track_chi_ = -99;
    _Tau1_track_nhit_ = -99;
    _Tau1_track_dz_ = -99;
    _Tau1_track_dxy_ = -99;
    _Tau1_z_ = -99;

    _Tau2_dmf_ = -99;
    _Tau2_dmfraw_ = -99;
    _Tau2_pt_ = -99;
    _Tau2_eta_ = -99;
    _Tau2_phi_ = -99;
    _Tau2_mass_ = -99;
    _Tau2_dR_ = -99;
    _Tau2_chIso_ = -99;
    _Tau2_nIso_ = -99;
    _Tau2_puIso_ = -99;
    _Tau2_cmbIso_ = -99;
    _Tau2_ncharged_ = -99;
    _Tau2_npizero_ = -99;    
    _Tau2_vz_ =  -99;
    _Tau2_track_pt_ = -99; 
    _Tau2_track_eta_ = -99;
    _Tau2_track_phi_ = -99;
    _Tau2_track_chi_ = -99;
    _Tau2_track_nhit_ = -99;
    _Tau2_track_dz_ = -99;
    _Tau2_track_dxy_ = -99;
    _Tau2_z_ = -99;

    if(match1){
      _Tau1_dmf_ = ((*disc1)[bestMatch1] > 0.5);
      _Tau1_dmfraw_ = (*disc1)[bestMatch1];
      _Tau1_pt_ = bestMatch1->pt();
      _Tau1_eta_ = bestMatch1->eta();
      _Tau1_phi_ = bestMatch1->phi();
      _Tau1_mass_ = bestMatch1->mass();
      _Tau1_dR_ = min_dR1;
      _Tau1_chIso_ = (*chIso1)[bestMatch1];
      _Tau1_nIso_ = (*nIso1)[bestMatch1];
      _Tau1_puIso_ = (*PUIso1)[bestMatch1];
      _Tau1_cmbIso_ = (*cmbIso1)[bestMatch1];
      _Tau1_ncharged_ = bestMatch1->signalPFChargedHadrCands().size();
      _Tau1_npizero_ = bestMatch1->signalPiZeroCandidates().size();
      
      _Tau1_z_ = bestMatch1->vertex().z();
	//      std::cout << "check ! " <<  << std::endl;

      if(bestMatch1->leadPFChargedHadrCand().isNonnull() && bestMatch1->leadPFChargedHadrCand()->trackRef().isNonnull()){
	_Tau1_vz_ = bestMatch1->leadPFChargedHadrCand()->trackRef()->vz();
	_Tau1_track_pt_ = bestMatch1->leadPFChargedHadrCand()->trackRef()->pt();
	_Tau1_track_eta_ = bestMatch1->leadPFChargedHadrCand()->trackRef()->eta();
	_Tau1_track_phi_ = bestMatch1->leadPFChargedHadrCand()->trackRef()->phi();
	_Tau1_track_chi_ = bestMatch1->leadPFChargedHadrCand()->trackRef()->normalizedChi2();
	_Tau1_track_nhit_ = bestMatch1->leadPFChargedHadrCand()->trackRef()->hitPattern().numberOfValidTrackerHits();
	_Tau1_track_dz_ = bestMatch1->leadPFChargedHadrCand()->trackRef()->dz(evtVertexPos);
	_Tau1_track_dxy_ = bestMatch1->leadPFChargedHadrCand()->trackRef()->dxy(evtVertexPos);
      }
    }

    std::cout << "check2" << std::endl;

    if(match2){
      _Tau2_dmf_ = ((*disc2)[bestMatch2] > 0.5);
      _Tau2_dmfraw_ = (*disc2)[bestMatch2];
      _Tau2_pt_ = bestMatch2->pt();
      _Tau2_eta_ = bestMatch2->eta();
      _Tau2_phi_ = bestMatch2->phi();
      _Tau2_mass_ = bestMatch2->mass();
      _Tau2_dR_ = min_dR2;
      _Tau2_chIso_ = (*chIso2)[bestMatch2];
      _Tau2_nIso_ = (*nIso2)[bestMatch2];
      _Tau2_puIso_ = (*PUIso2)[bestMatch2];
      _Tau2_cmbIso_ = (*cmbIso2)[bestMatch2];
      _Tau2_ncharged_ = bestMatch2->signalPFChargedHadrCands().size();
      _Tau2_npizero_ = bestMatch2->signalPiZeroCandidates().size();
      
      _Tau2_z_ = bestMatch2->vertex().z();

      if(bestMatch2->leadPFChargedHadrCand().isNonnull() && bestMatch2->leadPFChargedHadrCand()->trackRef().isNonnull()){
	_Tau2_vz_ = bestMatch2->leadPFChargedHadrCand()->trackRef()->vz();
	_Tau2_track_pt_ = bestMatch2->leadPFChargedHadrCand()->trackRef()->pt();
	_Tau2_track_eta_ = bestMatch2->leadPFChargedHadrCand()->trackRef()->eta();
	_Tau2_track_phi_ = bestMatch2->leadPFChargedHadrCand()->trackRef()->phi();
	_Tau2_track_chi_ = bestMatch2->leadPFChargedHadrCand()->trackRef()->normalizedChi2();
	_Tau2_track_nhit_ = bestMatch2->leadPFChargedHadrCand()->trackRef()->hitPattern().numberOfValidTrackerHits();
	_Tau2_track_dz_ = bestMatch2->leadPFChargedHadrCand()->trackRef()->dz(evtVertexPos);
	_Tau2_track_dxy_ = bestMatch2->leadPFChargedHadrCand()->trackRef()->dxy(evtVertexPos);
      }
    }
    
    std::cout << "check3" << std::endl;
    genTuple_->Fill();

  }
  




  //////////////////////////////////////////

  for (size_t iTau1 = 0; iTau1 < taus1->size(); ++iTau1) {
    reco::PFTauRef tau1(taus1, iTau1);
    if(tau1->pt() < 10.) continue;

    bool match_tau1 = false;
    Int_t match_index = -1;

    for(size_t i = 0; i < genTaus->size(); ++ i){
      
      const reco::GenJet & TauCand = (*genTaus)[i];
      reco::Particle::LorentzVector visibleP4 = ((*genTaus)[i]).p4();
      
      if(visibleP4.pt() < 5.0) continue;

      const std::vector <const reco::GenParticle*> mRefs = TauCand.getGenConstituents();
      unsigned int decayMode = 0; // 0 = hadronic, 1=electron, 2=muon 
      for(size_t igTauD =0; igTauD < mRefs.size(); igTauD++) {
	if(abs(mRefs[igTauD]->pdgId())==11) decayMode = 1;
	if(abs(mRefs[igTauD]->pdgId())==13) decayMode = 2;
      }
      
      if(decayMode!=0) continue; 

      double dR_MC = deltaR(tau1->p4(),((*genTaus)[i]).p4());
      
      if(dR_MC < matchingDistance_){
	match_tau1 = true;
	match_index = i;
      }
    }


    //    if(match_tau1==false) continue;

    Float_t min_dr = 1000;
    Float_t min_dr_CHS = 1000;

    if(match_tau1==false){
      for(size_t i = 0; i < ak5jet->size(); ++ i) {
	const reco::PFJet &jet = (*ak5jet)[i];

	double dR_jet = deltaR(tau1->p4(), jet.p4());
	
	if(dR_jet < min_dr){
	  min_dr = dR_jet;
	}
      }

      for(size_t i = 0; i < ak5jetCHS->size(); ++ i) {
	const reco::PFJet &jet = (*ak5jetCHS)[i];

	double dR_jet = deltaR(tau1->p4(), jet.p4());
	
	if(dR_jet < min_dr_CHS){
	  min_dr_CHS = dR_jet;
	}
      }
    }


    // check if tau2 has a same contents
	

    bool match_tau2 = false;
    reco::PFTauRef bestMatch;

    for (size_t iTau2 = 0; iTau2 < taus2->size(); ++iTau2) {
      reco::PFTauRef tau2(taus2, iTau2);
      if(tau2->pt() < 10.) continue;

      double dR_MC = -1;
      if(match_index!=-1) dR_MC = deltaR(tau2->p4(),((*genTaus)[match_index]).p4());


      if(dR_MC < matchingDistance_){
	match_tau2 = true;
	bestMatch = tau2;
      }
    }



    bool result1 = -99;
    bool result2 = -99; 
    double pt1 = -99; 
    double pt2 = -99; 
    double eta1 = -99;
    double eta2 = -99;
    double phi1 = -99;
    double phi2 = -99;
    double vz1 = -99;
    double vz2 = -99;
    double track_pt1 = -99;
    double track_pt2 = -99;
    double track_eta1 = -99;
    double track_eta2 = -99;
    double track_phi1 = -99;
    double track_phi2 = -99;
    double track_chi1 = -99;
    double track_chi2 = -99;
    double track_dz1 = -99;
    double track_dz2 = -99;
    double closest_dr1 = -99;
    double closest_dr2 = -99;
    double closest_dr1_CHS = -99;
    double closest_dr2_CHS = -99;
    double track_dxy1 = -99;
    double track_dxy2 = -99;
    int track_nhit1 = -99;
    int track_nhit2 = -99;

    double mass1 = -99;
    double mass2 = -99;
    double ResultChIso1 = -99;
    double ResultChIso2 = -99;
    double ResultNIso1 = -99; 
    double ResultNIso2 = -99; 
    double ResultPUIso1 = -99;
    double ResultPUIso2 = -99; 
    double ResultCmbIso1 = -99; 
    double ResultCmbIso2 = -99; 

    int ncharged1 = -99;
    int npizero1 = -99;
    int ncharged2 = -99;
    int npizero2 = -99;
    

    result1 = ((*disc1)[tau1] > 0.5);
    pt1 = tau1->pt();
    eta1 = tau1->eta();
    phi1 = tau1->phi();
    
    mass1 = tau1->mass();
    ResultChIso1 = (*chIso1)[tau1];
    ResultNIso1 = (*nIso1)[tau1];
    ResultPUIso1 = (*PUIso1)[tau1];
    ResultCmbIso1 = (*cmbIso1)[tau1];
    ncharged1 = tau1->signalPFChargedHadrCands().size();
    npizero1 = tau1->signalPiZeroCandidates().size();
    closest_dr1 = min_dr;
    closest_dr1_CHS = min_dr_CHS;

    if(tau1->leadPFChargedHadrCand().isNonnull() && tau1->leadPFChargedHadrCand()->trackRef().isNonnull()){
      vz1 = tau1->leadPFChargedHadrCand()->trackRef()->vz();
      track_pt1 = tau1->leadPFChargedHadrCand()->trackRef()->pt();
      track_eta1 = tau1->leadPFChargedHadrCand()->trackRef()->eta();
      track_phi1 = tau1->leadPFChargedHadrCand()->trackRef()->phi();
      track_chi1 = tau1->leadPFChargedHadrCand()->trackRef()->normalizedChi2();
      track_nhit1 = tau1->leadPFChargedHadrCand()->trackRef()->hitPattern().numberOfValidTrackerHits();
      track_dz1 = tau1->leadPFChargedHadrCand()->trackRef()->dz(evtVertexPos);
      track_dxy1 = tau1->leadPFChargedHadrCand()->trackRef()->dxy(evtVertexPos);
    }
  
  
    if(match_tau2){
      result2 = ((*disc2)[bestMatch] > 0.5);
      pt2 = bestMatch->pt();
      eta2 = bestMatch->eta();
      phi2 = bestMatch->phi();
      
      mass2 = bestMatch->mass();
      ResultChIso2 = (*chIso2)[bestMatch];
      ResultNIso2 = (*nIso2)[bestMatch];
      ResultPUIso2 = (*PUIso2)[bestMatch];
      ResultCmbIso2 = (*cmbIso2)[bestMatch];
      ncharged2 = bestMatch->signalPFChargedHadrCands().size();
      npizero2 = bestMatch->signalPiZeroCandidates().size();
      closest_dr2 = 1000;
      closest_dr2_CHS = 1000;
    
      if(bestMatch->leadPFChargedHadrCand().isNonnull() && bestMatch->leadPFChargedHadrCand()->trackRef().isNonnull()){
	vz2 = bestMatch->leadPFChargedHadrCand()->trackRef()->vz();
	track_pt2 = bestMatch->leadPFChargedHadrCand()->trackRef()->pt();
	track_eta2 = bestMatch->leadPFChargedHadrCand()->trackRef()->eta();
	track_phi2 = bestMatch->leadPFChargedHadrCand()->trackRef()->phi();
	track_chi2 = bestMatch->leadPFChargedHadrCand()->trackRef()->normalizedChi2();
	track_nhit2 = bestMatch->leadPFChargedHadrCand()->trackRef()->hitPattern().numberOfValidTrackerHits();
	track_dz2 = bestMatch->leadPFChargedHadrCand()->trackRef()->dz(evtVertexPos);
	track_dxy2 = bestMatch->leadPFChargedHadrCand()->trackRef()->dxy(evtVertexPos);
      }
    }

   
    _eventNum_ = ULong64_t(evt.id().event());
    _nVx_  = UChar_t(nVx);
    _type_ = Int_t(0);
    
    _pt_ = Float_t(pt1);
    _eta_  = Float_t(eta1);
    _phi_  = Float_t(phi1);
    _m_    = Float_t(mass1);
    _chIso_= Float_t(ResultChIso1);
    _nIso_ = Float_t(ResultNIso1);
    _puIso_= Float_t(ResultPUIso1);
    _cmbIso_=Float_t(ResultCmbIso1);
    _vz_ = Float_t(vz1);
    _match_ = Int_t(match_tau1);
    _dmf_ = Int_t(result1);
    _ncharged_ = Int_t(ncharged1);
    _npizero_ = Int_t(npizero1);
    _track_pt_ = Float_t(track_pt1);
    _track_eta_ = Float_t(track_eta1);
    _track_phi_ = Float_t(track_phi1);
    _track_chi_ = Float_t(track_chi1);
    _track_dz_ = Float_t(track_dz1);
    _track_dxy_ = Float_t(track_dxy1);
    _track_nhit_ = Int_t(track_nhit1);
    _closest_dr_ = Float_t(closest_dr1);
    _closest_dr_CHS_ = Float_t(closest_dr1_CHS);
	
    _pt2_ = Float_t(pt2);
    _eta2_  = Float_t(eta2);
    _phi2_  = Float_t(phi2);
    _m2_    = Float_t(mass2);
    _chIso2_= Float_t(ResultChIso2);
    _nIso2_ = Float_t(ResultNIso2);
    _puIso2_= Float_t(ResultPUIso2);
    _cmbIso2_=Float_t(ResultCmbIso2);
    _vz2_ = Float_t(vz2);
    _match2_ = Int_t(match_tau2);
    _dmf2_ = Int_t(result2);
    _ncharged2_ = Int_t(ncharged2);
    _npizero2_ = Int_t(npizero2);
    _track_pt2_ = Float_t(track_pt2);
    _track_eta2_ = Float_t(track_eta2);
    _track_phi2_ = Float_t(track_phi2);
    _track_chi2_ = Float_t(track_chi2);    
    _track_dz2_ = Float_t(track_dz2);
    _track_dxy2_ = Float_t(track_dxy2);
    _track_nhit2_ = Int_t(track_nhit2);
    _closest_dr2_ = Float_t(closest_dr2);
    _closest_dr2_CHS_ = Float_t(closest_dr2_CHS);
    
    isoTuple_->Fill();
  }


  ////////////////////////////////////////////////////


  for (size_t iTau2 = 0; iTau2 < taus2->size(); ++iTau2) {
    reco::PFTauRef tau2(taus2, iTau2);
    if(tau2->pt() < 10.) continue;

    bool match_tau2 = false;
    Int_t match_index = -1;

    for(size_t i = 0; i < genTaus->size(); ++ i){
      
      const reco::GenJet & TauCand = (*genTaus)[i];
      reco::Particle::LorentzVector visibleP4 = ((*genTaus)[i]).p4();
      
      if(visibleP4.pt() < 5.0) continue;

      const std::vector <const reco::GenParticle*> mRefs = TauCand.getGenConstituents();
      unsigned int decayMode = 0; // 0 = hadronic, 1=electron, 2=muon 
      for(size_t igTauD =0; igTauD < mRefs.size(); igTauD++) {
	if(abs(mRefs[igTauD]->pdgId())==11) decayMode = 1;
	if(abs(mRefs[igTauD]->pdgId())==13) decayMode = 2;
      }
      
      if(decayMode!=0) continue; 

      double dR_MC = deltaR(tau2->p4(),((*genTaus)[i]).p4());
      
      if(dR_MC < matchingDistance_){
	match_tau2 = true;
	match_index = i;
      }
    }


    Float_t min_dr = 1000;
    Float_t min_dr_CHS = 1000;

    //    if(match_tau2==false) continue;

    if(match_tau2==false){
      for(size_t i = 0; i < ak5jet->size(); ++ i) {
	const reco::PFJet &jet = (*ak5jet)[i];

	double dR_jet = deltaR(tau2->p4(), jet.p4());
	
	if(dR_jet < min_dr){
	  min_dr = dR_jet;
	}
      }

      for(size_t i = 0; i < ak5jetCHS->size(); ++ i) {
	const reco::PFJet &jet = (*ak5jetCHS)[i];

	double dR_jet = deltaR(tau2->p4(), jet.p4());
	
	if(dR_jet < min_dr_CHS){
	  min_dr_CHS = dR_jet;
	}
      }

      //      continue;
    }


    // check if tau1 has a same contents
	

    bool match_tau1 = false;
    reco::PFTauRef bestMatch;


    for (size_t iTau1 = 0; iTau1 < taus1->size(); ++iTau1) {
      reco::PFTauRef tau1(taus1, iTau1);
      if(tau1->pt() < 10.) continue;
      
      double dR_MC = -1;
      if(match_index!=-1) dR_MC = deltaR(tau1->p4(),((*genTaus)[match_index]).p4());

      if(dR_MC < matchingDistance_){
	match_tau1 = true;
	bestMatch = tau1;
      }
    }



    bool result1 = -99;
    bool result2 = -99; 
    double pt1 = -99; 
    double pt2 = -99; 
    double eta1 = -99;
    double eta2 = -99;
    double phi1 = -99;
    double phi2 = -99;
    double vz1 = -99;
    double vz2 = -99;
    double track_pt1 = -99;
    double track_pt2 = -99;
    double track_eta1 = -99;
    double track_eta2 = -99;
    double track_phi1 = -99;
    double track_phi2 = -99;
    double track_chi1 = -99;
    double track_chi2 = -99;
    double track_dz1 = -99;
    double track_dz2 = -99;
    double closest_dr1 = -99;
    double closest_dr2 = -99;
    double closest_dr1_CHS = -99;
    double closest_dr2_CHS = -99;
    double track_dxy1 = -99;
    double track_dxy2 = -99;
    int track_nhit1 = -99;
    int track_nhit2 = -99;

    double mass1 = -99;
    double mass2 = -99;
    double ResultChIso1 = -99;
    double ResultChIso2 = -99;
    double ResultNIso1 = -99; 
    double ResultNIso2 = -99; 
    double ResultPUIso1 = -99;
    double ResultPUIso2 = -99; 
    double ResultCmbIso1 = -99; 
    double ResultCmbIso2 = -99; 

    int ncharged1 = -99;
    int npizero1 = -99;
    int ncharged2 = -99;
    int npizero2 = -99;
    

    result1 = ((*disc2)[tau2] > 0.5);
    pt1 = tau2->pt();
    eta1 = tau2->eta();
    phi1 = tau2->phi();
    
    mass1 = tau2->mass();
    ResultChIso1 = (*chIso2)[tau2];
    ResultNIso1 = (*nIso2)[tau2];
    ResultPUIso1 = (*PUIso2)[tau2];
    ResultCmbIso1 = (*cmbIso2)[tau2];
    ncharged1 = tau2->signalPFChargedHadrCands().size();
    npizero1 = tau2->signalPiZeroCandidates().size();
    closest_dr1 = min_dr;
    closest_dr1_CHS = min_dr_CHS;

    if(tau2->leadPFChargedHadrCand().isNonnull() && tau2->leadPFChargedHadrCand()->trackRef().isNonnull()){
      vz1 = tau2->leadPFChargedHadrCand()->trackRef()->vz();
      track_pt1 = tau2->leadPFChargedHadrCand()->trackRef()->pt();
      track_eta1 = tau2->leadPFChargedHadrCand()->trackRef()->eta();
      track_phi1 = tau2->leadPFChargedHadrCand()->trackRef()->phi();
      track_chi1 = tau2->leadPFChargedHadrCand()->trackRef()->normalizedChi2();
      track_nhit1 = tau2->leadPFChargedHadrCand()->trackRef()->hitPattern().numberOfValidTrackerHits();
      track_dz1 = tau2->leadPFChargedHadrCand()->trackRef()->dz(evtVertexPos);
      track_dxy1 = tau2->leadPFChargedHadrCand()->trackRef()->dxy(evtVertexPos);
    }
  
  
    if(match_tau1){
      result2 = ((*disc1)[bestMatch] > 0.5);
      pt2 = bestMatch->pt();
      eta2 = bestMatch->eta();
      phi2 = bestMatch->phi();
      
      mass2 = bestMatch->mass();
      ResultChIso2 = (*chIso1)[bestMatch];
      ResultNIso2 = (*nIso1)[bestMatch];
      ResultPUIso2 = (*PUIso1)[bestMatch];
      ResultCmbIso2 = (*cmbIso1)[bestMatch];
      ncharged2 = bestMatch->signalPFChargedHadrCands().size();
      npizero2 = bestMatch->signalPiZeroCandidates().size();
      closest_dr2 = 1000;
      closest_dr2_CHS = 1000;
    
      if(bestMatch->leadPFChargedHadrCand().isNonnull() && bestMatch->leadPFChargedHadrCand()->trackRef().isNonnull()){
	vz2 = bestMatch->leadPFChargedHadrCand()->trackRef()->vz();
	track_pt2 = bestMatch->leadPFChargedHadrCand()->trackRef()->pt();
	track_eta2 = bestMatch->leadPFChargedHadrCand()->trackRef()->eta();
	track_phi2 = bestMatch->leadPFChargedHadrCand()->trackRef()->phi();
	track_chi2 = bestMatch->leadPFChargedHadrCand()->trackRef()->normalizedChi2();
	track_nhit2 = bestMatch->leadPFChargedHadrCand()->trackRef()->hitPattern().numberOfValidTrackerHits();
	track_dz2 = bestMatch->leadPFChargedHadrCand()->trackRef()->dz(evtVertexPos);
	track_dxy2 = bestMatch->leadPFChargedHadrCand()->trackRef()->dxy(evtVertexPos);
      }
    }

   
    _eventNum_ = ULong64_t(evt.id().event());
    _nVx_  = UChar_t(nVx);
    _type_ = Int_t(1);
    
    _pt_ = Float_t(pt1);
    _eta_  = Float_t(eta1);
    _phi_  = Float_t(phi1);
    _m_    = Float_t(mass1);
    _chIso_= Float_t(ResultChIso1);
    _nIso_ = Float_t(ResultNIso1);
    _puIso_= Float_t(ResultPUIso1);
    _cmbIso_=Float_t(ResultCmbIso1);
    _vz_ = Float_t(vz1);
    _match_ = Int_t(match_tau2);
    _dmf_ = Int_t(result1);
    _ncharged_ = Int_t(ncharged1);
    _npizero_ = Int_t(npizero1);
    _track_pt_ = Float_t(track_pt1);
    _track_eta_ = Float_t(track_eta1);
    _track_phi_ = Float_t(track_phi1);
    _track_chi_ = Float_t(track_chi1);
    _track_dz_ = Float_t(track_dz1);
    _track_dxy_ = Float_t(track_dxy1);
    _track_nhit_ = Int_t(track_nhit1);
    _closest_dr_ = Float_t(closest_dr1);
    _closest_dr_CHS_ = Float_t(closest_dr1_CHS);

    _pt2_ = Float_t(pt2);
    _eta2_  = Float_t(eta2);
    _phi2_  = Float_t(phi2);
    _m2_    = Float_t(mass2);
    _chIso2_= Float_t(ResultChIso2);
    _nIso2_ = Float_t(ResultNIso2);
    _puIso2_= Float_t(ResultPUIso2);
    _cmbIso2_=Float_t(ResultCmbIso2);
    _vz2_ = Float_t(vz2);
    _match2_ = Int_t(match_tau2);
    _dmf2_ = Int_t(result2);
    _ncharged2_ = Int_t(ncharged2);
    _npizero2_ = Int_t(npizero2);
    _track_pt2_ = Float_t(track_pt2);
    _track_eta2_ = Float_t(track_eta2);
    _track_phi2_ = Float_t(track_phi2);
    _track_chi2_ = Float_t(track_chi2);    
    _track_dz2_ = Float_t(track_dz2);
    _track_dxy2_ = Float_t(track_dxy2);
    _track_nhit2_ = Int_t(track_nhit2);
    _closest_dr2_ = Float_t(closest_dr2);
    _closest_dr2_CHS_ = Float_t(closest_dr2_CHS);

    isoTuple_->Fill();
  }


  _nak5jet_ = ak5jet->size();
  _nak5jetCHS_ = ak5jetCHS->size();
  _ntau_ = taus2->size();
  _ntauCHS_ = taus1->size();
  _ngentau_ = genTaus->size();
  eventTuple_->Fill();

  return true;
}

void RecoTauDifferenceAnalyzer::endJob() {
  //  isoTuple_->Print();

  TTree *savetree = isoTuple_->CloneTree();
  TTree *savetree2 = eventTuple_->CloneTree();
  TTree *savetree3 = genTuple_->CloneTree();
  TFile* file = new TFile("ntuple.root","recreate");
  savetree->Write();
  savetree2->Write();
  savetree3->Write(); 
  file->Close();

  delete savetree;
  delete savetree2;
  delete savetree3;
  delete isoTuple_;
  delete eventTuple_;
  delete genTuple_;


}


#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(RecoTauDifferenceAnalyzer);
