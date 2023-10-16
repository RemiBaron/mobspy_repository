from mobspy import *

if __name__ == '__main__':
    A = BaseSpecies()

    A.a1, A.a2, A.a3.b
    A.a1 >> Zero [1]
    A.a1 + Cts >> Zero [1]
    S = Simulation(A)
    S.level = -1
    with S.event_time(5):
        All[A](f'{A} + 1')
    
    Cts.titi
    print("Cts characteristics :", Cts.get_characteristics())
    print("Species cts_characteristics :", Species.cts_context)
    with S.event_time(10):
        All[A.a1](f'{A} + 1')
    print("\n\n\nGoing into the feature")
    with Cts.toto :
        print("Inside the body of the with")
        print("Cts characteristics :", Cts.get_characteristics())
        print("Species cts_characteristics :", Species.cts_context)
    print("Gone out of the feature\n\n\n")
    print("Cts characteristics :", Cts.get_characteristics())
    print("Species cts_characteristics :", Species.cts_context)
    