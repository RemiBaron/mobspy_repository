from mobspy.modules.meta_class import *
from contextlib import contextmanager

class Cts_specie(Species) :
    """
        Class which inherits from Species. It is used to simplify the syntax of reactions inside a context.
    """

    def cts_context_initiator(self,characteristic):
        self.add_characteristic(characteristic)
        # Set context in all meta-species
        Species.update_cts_context(self.get_characteristics())

    def cts_context_finish(self,characteristic):
        self.remove_characteristic(characteristic)
        # Set context in all meta-species
        Species.update_cts_context(self.get_characteristics())

    @contextmanager
    def __getattr__(self, characteristic):
        try:
            print("TRY", characteristic)
            self.cts_context_initiator(characteristic)
            yield 0
        finally:
            self.cts_context_finish(characteristic)
            print("FINALLY")

    def __call__(self, quantity):
        """
            The call operator is overloaded as the Cts specie cannot be called. Thus it raises an error when called.
        """
        simlog.error('The Cts specie cannot be called')

   

    
__SCts = Cts_specie('Context_MetaSpecies')
Cts = __SCts