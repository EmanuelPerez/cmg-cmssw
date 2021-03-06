#include <iostream>
#include <sstream>
#include <string>
#include <memory>
#include <stdint.h>


#include "HepMC/GenEvent.h"
#include "HepMC/HEPEVT_Wrapper.h"
#include "HepMC/IO_HEPEVT.h"

#include "GeneratorInterface/Core/interface/ParameterCollector.h"
#include "GeneratorInterface/Core/interface/BaseHadronizer.h"
#include "GeneratorInterface/Core/interface/GeneratorFilter.h"
#include "GeneratorInterface/Core/interface/HadronizerFilter.h"
#include "GeneratorInterface/Core/interface/RNDMEngineAccess.h"
#include "FWCore/ParameterSet/interface/FileInPath.h"
#include "GeneratorInterface/Pythia6Interface/interface/Pythia6Service.h"
#include "GeneratorInterface/Core/interface/FortranCallback.h"


HepMC::IO_HEPEVT conv;

extern "C" {
  void steering_(const char*);
  //void vzero_(int&,int&);
  //void ffread_(int&, char*, char*, char*);
  //void ucopy_(char*, char*, int&);
  void hzha_init_(void);
  void hzha_event_(void);
  //void timel_(int&);
  void hzha_close_(void);
  void pyhepc_(int&);
}

extern "C" {
  extern struct {
    int n, npad, k[5][4000];
    double p[5][4000], v[5][4000];
  } pyjets_;
}

class HZHAHadronizer : public gen::BaseHadronizer {
public:
  HZHAHadronizer(const edm::ParameterSet &params);
  ~HZHAHadronizer();
  
  bool readSettings( int ) { return true; }
  bool initializeForInternalPartons();
  bool declareStableParticles(const std::vector<int> &pdgIds);
  bool declareSpecialSettings( const std::vector<std::string> ) { return true; }
  bool generatePartonsAndHadronize();
  bool decay();
  void statistics(){};
  bool residualDecay();
  void finalizeEvent();
  const char *classname() const { return "HZHAHadronizer"; }
  
private:
 
  //gen::Pythia6Service* fPy6Service;
  std::string _configPath;
  
};

HZHAHadronizer::HZHAHadronizer(const edm::ParameterSet &params) :
  BaseHadronizer(params),
  //fPy6Service( new gen::Pythia6Service() ),
  _configPath(params.getParameter<std::string>("CardsPath"))
   
{
}

HZHAHadronizer::~HZHAHadronizer()
{
}

bool HZHAHadronizer::initializeForInternalPartons()
{
  
  edm::FileInPath file( _configPath.c_str() );
  const char* filename = file.fullPath().c_str();
  //std::cout << file.fullPath() << std::endl;
  steering_(filename);
  //std::cout << "ciao" << std::endl;
  hzha_init_();
  return true;
}

#if 0
// naive Sherpa HepMC status fixup //FIXME 
static int getStatus(const HepMC::GenParticle *p)
{
  return status;
}
#endif

//FIXME
bool HZHAHadronizer::declareStableParticles(const std::vector<int> &pdgIds)
{
#if 0
  for(std::vector<int>::const_iterator iter = pdgIds.begin();
      iter != pdgIds.end(); ++iter)
    if (!markStable(*iter))
      return false;
  
  return true;
#else
  return false;
#endif
}


bool HZHAHadronizer::generatePartonsAndHadronize()
{
  //gen::Pythia6Service::InstanceWrapper guard(fPy6Service);
  //gen::FortranCallback::getInstance()->resetIterationsPerEvent();
  //get the next event
  hzha_event_();
  //convert hepevt to hepmc
  int mode=1; 
  pyhepc_(mode);
  //store hepmc in the event
  event().reset( conv.read_next_event() );
  return true;
}

bool HZHAHadronizer::decay()
{
	return true;
}

bool HZHAHadronizer::residualDecay()
{
	return true;
}

void HZHAHadronizer::finalizeEvent()
{
}

//GETTER for the external random numbers
//DECLARE_GETTER(CMS_SHERPA_RNG_Getter,"CMS_SHERPA_RNG",ATOOLS::External_RNG,ATOOLS::RNG_Key);

//ATOOLS::External_RNG *CMS_SHERPA_RNG_Getter::operator()(const ATOOLS::RNG_Key &) const
//{ return new CMS_SHERPA_RNG(); }

//void CMS_SHERPA_RNG_Getter::PrintInfo(std::ostream &str,const size_t) const
//{ str<<"CMS_SHERPA_RNG interface"; }

//double CMS_SHERPA_RNG::Get(){
//   return randomEngine->flat();
//   }
   
#include "GeneratorInterface/ExternalDecays/interface/ExternalDecayDriver.h"

typedef edm::GeneratorFilter<HZHAHadronizer, gen::ExternalDecayDriver> HZHAGeneratorFilter;
DEFINE_FWK_MODULE(HZHAGeneratorFilter);
