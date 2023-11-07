from mobspy import *

if __name__ == '__main__':
    C = BaseSpecies()
    C.toto, C.titi

    A, B = New(C)

    A.a1, A.a2, B.b1, B.b2
    with Any.titi :
        A.a1 + B.b1 >> Zero [0.01]
        A.a2 + B.b2 >> Zero [0.02]

    A.titi(100), B.titi(120)
    S = Simulation(A | B)
    S.method = 'stochastic'
    S.duration = 15
    S.output_event = True

    logic_expression = (A <= 50) & (B <= 50)
    with Any.titi, S.event_condition(logic_expression):
            A(100), B(120)
    
    print(S.compile())
