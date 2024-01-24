import numpy as np
import math
import pandas as pd


class Game:
    def __init__(self, tab, actions):
        self.actions = actions
        m = np.array(tab, dtype=[("x", object), ("y", object)])
        self.size = int(math.sqrt(len(tab)))
        self.scores = m.reshape(self.size, self.size)

    def prettyPrint(self):
        game = pd.DataFrame(np.nan, self.actions, self.actions, dtype=oject)
        for i in range(self.size):
            for j in range(self.size):
                game.iat[i, j] = self.scores[i][j]
        print(game)


def getNash(self):
    max_x = np.matrix(self.scores["x"].max(0)).repeat(self.size, axis=0)
    bool_x = self.scores["x"] == max_x
    max_y = np.matrix(self.scores["y"].max(1)).transpose().repeat(self.size, axis=1)
    bool_y = self.scores["y"] == max_y
    bool_x_y = bool_x & bool_y
    result = np.where(bool_x_y == True)
    listOfCoordinates = list(zip(result[0], result[1]))
    return listOfCoordinates


def isPareto(self, t, s):
    return (
        True
        if (len(s) == 0)
        else (s[0][0] <= t[0] or s[0][1] <= t[1]) and isPareto(self, t, s[1:])
    )


def getPareto(self):
    x = 0
    y = 0
    res = list()
    liste = self.scores.flatten()
    for s in liste:
        if x == self.size:
            x = 0
            y = y + 1
        if isPareto(self, s, liste):
            res.append((x, y))
        x = x + 1
    return res


rpc = [(0, 0), (-1, 1), (1, -1), (1, -1), (0, 0), (-1, 1), (-1, 1), (1, -1), (0, 0)]
g = Game(rpc, ["R", "P", "C"])


listOfCoordinates = getNash(g)
print("The indexes of Nash's equilibrium: ")
print(listOfCoordinates)

print("The corresponding rounds : ")
for cor in listOfCoordinates:
    print(g.actions[cor[0]], g.actions[cor[1]])

print("The corresponding scores: ")
for cor in listOfCoordinates:
    print(g.scores[cor[0]][cor[1]])

# We recover the indexes of the pareto optimum(s)
listOfCoordinates = getPareto(g)
print("The indexes of Pareto's optimums : ")
print(listOfCoordinates)

# We print the moves corresponding to these optimums
print("The corresponding rounds : ")
for cor in listOfCoordinates:
    print(g.actions[cor[0]], g.actions[cor[1]])

# We print the corresponding scores
print("The corresponding scores : ")
for cor in listOfCoordinates:
    print(g.scores[cor[0]][cor[1]])
