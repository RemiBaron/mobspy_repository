from mobspy import *

if __name__ == '__main__':
    Age, Color, Dense = BaseSpecies()
    Age.old, Age.young
    Color.red, Color.green
    Dense.dense, Dense.sparse
    Tree = Age * Color * Dense
    Grass = Age * Color * Dense

    with Age.old, Dense.sparse :
        with Any.red:
                Tree >> Grass [1]
        with Color.blue :
            Tree >> Grass [1]
            Tree(10)
        Tree(9)
        All[Grass](1)

    S = Simulation(Tree | Grass)
    print(S.compile())