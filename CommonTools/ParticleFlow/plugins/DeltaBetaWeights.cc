#include "CommonTools/ParticleFlow/plugins/DeltaBetaWeights.h"

DeltaBetaWeights::DeltaBetaWeights(const edm::ParameterSet& iConfig):
  src_(iConfig.getParameter<edm::InputTag>("src")),
  pfCharged_(iConfig.getParameter<edm::InputTag>("chargedFromPV")),
  pfPU_(iConfig.getParameter<edm::InputTag>("chargedFromPU"))
{
  produces<reco::PFCandidateCollection>();

  pfCharged_token = consumes<reco::PFCandidateCollection>(pfCharged_);
  pfPU_token = consumes<reco::PFCandidateCollection>(pfPU_);
  src_token = consumes<reco::PFCandidateCollection>(src_);

  // pfCharged_token = consumes<reco::PFCandidateCollection>(pfCharged_);
  // pfPU_token = consumes<reco::PFCandidateCollection>(pfPU_);
  // src_token = consumes<reco::PFCandidateCollection>(src_);

}


DeltaBetaWeights::~DeltaBetaWeights()
{
 
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
DeltaBetaWeights::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;

  // edm::Handle<edm::View<reco::Candidate> > pfCharged;
  // edm::Handle<edm::View<reco::Candidate> > pfPU;
  // edm::Handle<edm::View<reco::Candidate> > src;
  

  edm::Handle<reco::PFCandidateCollection> pfCharged;
  edm::Handle<reco::PFCandidateCollection> pfPU;
  edm::Handle<reco::PFCandidateCollection> src;

  iEvent.getByToken(src_token,src);
  iEvent.getByToken(pfCharged_token,pfCharged);
  iEvent.getByToken(pfPU_token,pfPU);

  double sumNPU = .0;
  double sumPU = .0;

  std::auto_ptr<reco::PFCandidateCollection> out(new reco::PFCandidateCollection); 


  for (const reco::PFCandidate & cand : *src) {
    if (cand.charge() !=0) {
      out->push_back(cand);
      continue;
    }

    sumNPU=1.0;
    sumPU=1.0;
    double eta=cand.eta();
    double phi=cand.phi();
    for (const reco::PFCandidate &chCand : *pfCharged ) {
      double sum = (chCand.pt()*chCand.pt())/(deltaR2(eta,phi,chCand.eta(),chCand.phi()));
      if(sum > 1.0) sumNPU *= sum;
    }
    sumNPU=0.5*log(sumNPU);

    for (const reco::PFCandidate &puCand : *pfPU ) {
      double sum = (puCand.pt()*puCand.pt())/(deltaR2(eta,phi,puCand.eta(),puCand.phi()));
      if(sum > 1.0) sumPU *= sum;
    }
    sumPU=0.5*log(sumPU);

    reco::PFCandidate neutral = cand;
    if (sumNPU+sumPU>0)
      neutral.setP4(((sumNPU)/(sumNPU+sumPU))*neutral.p4());
    out->push_back(neutral);

  }

  iEvent.put(out);
 
}
