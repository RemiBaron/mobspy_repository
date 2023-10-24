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
            self.cts_context_initiator(characteristic)
            yield 0
        finally:
            self.cts_context_finish(characteristic)

    def __call__(self, quantity):
        """
            The call operator is overloaded as the Cts specie cannot be called. Thus it raises an error when called.
        """
        simlog.error('The Cts specie cannot be called')
    
    def __add__(self, other):
        """
            The add operator is overloaded as the Cts specie cannot be added. Thus it raises an error when added.
        """
        simlog.error('The Cts specie cannot be added')
    
    def __radd__(self, other):
        """
            The add operator is overloaded as the Cts specie cannot be added. Thus it raises an error when added.
        """
        simlog.error('The Cts specie cannot be added')
    
    def __rmul__(self, other):
        """
            The multiplication operator is overloaded as the Cts specie cannot be multiplied. Thus it raises an error when multiplied.
        """
        simlog.error('The Cts specie cannot be multiplied')

    def __rshift__(self, other):
        """
            The >> operator is overloaded so that  it raises an error when used.
        """
        simlog.error('The >> operator cannot be used on the Cts specie')

   

    
__SCts = Cts_specie('Context_MetaSpecies')
Cts = __SCts