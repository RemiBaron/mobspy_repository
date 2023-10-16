from mobspy.modules.meta_class import *
from contextlib import contextmanager

class Cts_specie(Species) :
    """
        Class which inherits from Species. It is used to simplify the syntax of reactions inside a context.
    """

    @contextmanager
    def __getattr__(self, characteristic):
        try:
            print("TRY", characteristic)
            self.add_characteristic(characteristic)
            yield 0
        finally:
            self.remove_characteristic(characteristic)
            print("FINALLY")


    current_context = None

    def __call__(self, quantity):
        """
            The call operator is overloaded as the Cts specie cannot be called. Thus it raises an error when called.
        """
        simlog.error('The Cts specie cannot be called')

   

    
__SCts = Cts_specie('Context_MetaSpecies')
Cts = __SCts