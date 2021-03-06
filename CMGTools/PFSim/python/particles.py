import copy
from CMGTools.RootTools.physicsobjects.Particle import Particle as BaseParticle

class ParticleWithP4(BaseParticle):
    def __init__(self, p4, pdgId ):
        self._p4 = copy.copy(p4)
        self._pdgId = pdgId
    def p4(self):
        return self._p4
    def pdgId(self):
        return self._pdgId
    def smear(self, factor):
        self._p4 *= factor


class RecParticle(ParticleWithP4):
    def __init__(self, obj):
        self.physObj = obj       
        super(RecParticle,self).__init__(obj.p4(), obj.pdgId())
        

class GenParticle(ParticleWithP4):
    def __init__(self, obj):
        self.physObj = obj       
        super(GenParticle,self).__init__(obj.p4(), obj.pdgId())
        

class SimParticle(ParticleWithP4):
    def __init__(self, obj):
        self.physObj = obj       
        super(SimParticle,self).__init__(obj.p4(), obj.pdgId())
##     def __getattr__(self, name):
##         return getattr(self.physObj, name)
        

class GenJet(ParticleWithP4):
    def __init__(self, p4):
        super(GenJet,self).__init__(p4, 1)
    

class PFJet(ParticleWithP4):
    def __init__(self, obj):
        self.physObj = obj 
        super(PFJet,self).__init__(obj, 1)
    def __getattr__(self, name):
        return getattr(self.physObj, name)


class SimJet(ParticleWithP4):
    def __init__(self, p4):
        super(SimJet,self).__init__(p4, 1)

class Jet(ParticleWithP4):
    def __init__(self, p4):
        super(Jet,self).__init__(p4, 1)
    

class Electron(ParticleWithP4):
    def __init__(self, p4):
        super(Electron,self).__init__(p4, 11)
    

class Muon(ParticleWithP4):
    def __init__(self, p4):
        super(Muon,self).__init__(p4, 13)
    


