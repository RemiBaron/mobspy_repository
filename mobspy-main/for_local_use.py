from mobspy import *

if __name__ == '__main__':
    Hunger, Mortal, Money = BaseSpecies()
    Hunger.full, Hunger.starving
    Money.poor, Money.rich
    Mortal >> Zero[lambda r1 : 0.5 if r1.starving else 0]
    Hunger.full >> Hunger.starving[1]


    Grass = BaseSpecies()
    Antelope = Hunger * Mortal * Money
    Tiger = Hunger * Mortal * Money
    Zero >> Grass[3]
    Antelope.starving + Grass >> Antelope.full[0.5]
    Antelope.full >> 2*Antelope.starving[0.5]
    Tiger.rich >> 2*Tiger.rich[0.5]
    print("\n\n\nGoing into the feature")
    with Cts.toto, Cts.titi, Cts.rich :
        Tiger(25)
        print("Inside the body of the with")
    print("Gone out of the feature\n\n\n")
    All[Antelope](5), Grass(50), Tiger(100)
    S = Simulation(Antelope | Grass | Tiger)
    S.method = 'stochastic'
    S.duration = 20
    S.run()
    
    