from mobspy import *

if __name__ == '__main__':
    Age, Color, Dense = BaseSpecies()

    Age.old, Age.young
    Color.red, Color.green
    Dense.dense, Dense.sparse

    Tree = Age * Color * Dense
    Grass = Age * Color * Dense

    with Age.old :
        with Color.red :
            Tree >> Grass [1]
        with Color.blue :
            Tree >> Grass [1]


    with Any.young.green.dense :
        Tree + Grass >> Tree + Tree [2]

    S = Simulation(Tree | Grass)
    S.method = 'stochastic'
    S.duration = 15
    S.output_event = True
    print(S.compile())
