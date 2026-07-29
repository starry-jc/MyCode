# Problem: coci17c2p1

# K = piecesOfLand
# N = rows
# M = columns
piecesOfLand = int(input())
numberOfTurns = 0

for i in range(piecesOfLand):
    rows, columns = map(int, input().split())

    if rows <= columns:
        numberOfTurns = 2 * (rows - 1)
    if columns <= rows:
        numberOfTurns = 2 * (columns - 1)

    print(numberOfTurns)

    '''numberOfMoves = (rows * columns) - 1
    numberOfTurns = numberOfMoves - 1
    print(numberOfTurns)'''