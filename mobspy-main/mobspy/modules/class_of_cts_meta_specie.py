"""
    The class_of_cts_meta_specie.py model is responsible for defining the Cts_specie class.
"""
from mobspy.modules.meta_class import *
from contextlib import contextmanager

class Cts_specie(Species) :
    """
        Class which inherits from Species. It only has one object, Cts, which is defined at the end of this script.
        It is used to simplify the syntax of reactions and count setting inside the body of a "with Cts.example_characteristic :" statement.
        Is is compatible with event_condition and event_time methods of the Simulation class. 
        It can be nested and used several time in the same with statement.
    """

    def cts_context_initiator(self,characteristic):
        """
            This sets the Cts context in all meta-species.

            :params characteristic: (str) characteristic of the Cts specie in this specific context. Characteristic to be added.
        """
        self.add_characteristic(characteristic)
        Species.update_cts_context(self.get_characteristics())

    def cts_context_finish(self,characteristic):
        """
            This removes the Cts context in all meta-species.

            :params characteristic: (str) characteristic of the Cts specie in this specific context. Characteristic to be removed.
        """
        self.remove_characteristic(characteristic)
        Species.update_cts_context(self.get_characteristics())

    @contextmanager
    def __getattr__(self, characteristic):
        """
            Called inside a with statement. It manages the characteristic in the Cts_context.

            :params characteristic: (str) characteristic of the Cts specie in this specific context. Characteristic to be managed.
        """
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