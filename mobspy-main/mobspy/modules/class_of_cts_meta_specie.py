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
    # This is the set of characteristics which are currently under the active Cts context.
    _set_of_characteristics_currently_under_cts_context = set()

    # This is the list of all the nested Cts contexts which are currently active.
    _list_of_nested_cts_contexts = []

    def __getattr__(self, item):
        """
            This method is called when an attribute is called on the Cts specie. It is used to add the characteristic to the currently active Cts context.

            :param item: (str) characteristic to be added to the currently active Cts context.

            :raise simlog.error: if the Cts specie is given a characteristic outside of a context.

            :return self: to allow for assigning multiple characteristics to the Cts specie in the same line.
        """
        code_line = inspect.stack()[1].code_context[0][:-1]
        code_line = code_line.split(' ')
        is_with = [x for x in code_line if x != ''][0]
        if is_with == 'with':
            pass
        else:
            simlog.error('Characteristics cannot be added to the Cts specie outside of a context')
        self._set_of_characteristics_currently_under_cts_context.add(item)
        return self

    def __enter__(self):
        """
            Context manager for Cts characteristics. Called in "with Simulation.event_time(time) :" format, when entering. 
        """
        self.cts_context_initiator()
        return 0

    def __exit__(self, *args):
        """
            Context manager for Cts characteristics. Called in "with Simulation.event_time(time) :" format, when exiting. 
        """
        self.cts_context_finish()

    def cts_context_initiator(self):
        """
            This adds the current context in _list_of_nested_cts_contexts and then updates the Cts context in all meta-species.
        """
        self._list_of_nested_cts_contexts.append(set(self._set_of_characteristics_currently_under_cts_context))
        Species.update_cts_context(self._set_of_characteristics_currently_under_cts_context)

    def cts_context_finish(self):
        """
            This removes the context which is ending from _list_of_nested_cts_contexts and updates the current Cts context.
            Then, it updates the Cts context in all meta-species.
        """
        self._list_of_nested_cts_contexts.pop()
        if len(self._list_of_nested_cts_contexts) > 0:
            self._set_of_characteristics_currently_under_cts_context = self._list_of_nested_cts_contexts[-1]
        else:
            self._set_of_characteristics_currently_under_cts_context = set()
        Species.update_cts_context(self._set_of_characteristics_currently_under_cts_context)

    

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

   
#Cts is the only object of the Cts_specie class that will be used. It is defined here.
__SCts = Cts_specie('Context_MetaSpecies')
Cts = __SCts