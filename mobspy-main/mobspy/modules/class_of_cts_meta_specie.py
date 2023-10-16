from mobspy.modules.meta_class import *

class Cts_specie(Species) :
    """
        Class which inherits from Species. It is used to simplify the syntax of reactions inside a context.
    """
    current_context = None

    def __enter__(self):
        print("Entered the __enter__. Initializing the context")
        self.current_context = "This needs to be initialized"
        return self
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Exiting the __exit__. Reinitalizing the context")
        current_context = None
        return self

    def __call__(self, quantity):
        """
            The call operator is overloaded as the Cts specie cannot be called. Thus it raises an error when called.
        """
        simlog.error('The Cts specie cannot be called')

    def __getattr__(self, characteristic):
        """
            The .dot operator is overloaded.
        """
        # This is for IPython notebooks compatibility
        if characteristic == '_ipython_canary_method_should_not_exist_':
            return 0

        if self.current_context is None:
            simlog.error('The Cts specie can only be used inside a context')
        Species.check_if_valid_characteristic(characteristic)

        characteristics_from_references = mcu.unite_characteristics(self.get_references())
        characteristics = {characteristic}

        if characteristic not in characteristics_from_references and '$' not in characteristic:
            if len(self.get_characteristics()) == 0:
                self.first_characteristic = characteristic
            self.add_characteristic(characteristic)
        return self
    
__SCts = Cts_specie('Context_MetaSpecies')
Cts = __SCts