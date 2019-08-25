from random import randint

gamerX = randint(1, 10)
gamerY = randint(1, 10)
treasureX = randint(1, 10)
treasureY = randint(1, 10)
amountOfMoves = 0

def getAmountOfMovesToTreasure():
    return abs(treasureX - gamerX) + abs(treasureY - gamerY)

requiredAmountOfMoves = getAmountOfMovesToTreasure()

def getIsGamergainedTreasure():
    return treasureX == gamerX and treasureY == gamerY
def getIsGamerBeyondBoard():
    return gamerX <= 0 or gamerX > 10 or gamerY <= 0 or gamerY > 10

while True:
    amountBeforeMove = getAmountOfMovesToTreasure()
    print('W - up, A - left, S - down, D - right ')
    move = input('Where do you want to go?... ')
    move = move.lower()
    amountOfMoves += 1
    if move == 'w':
        gamerY += 1
    elif move == 'a':
        gamerX -= 1
    elif move == 's':
        gamerY -= 1
    elif move == 'd':
        gamerX += 1

    amountAfterMove = getAmountOfMovesToTreasure()
    print('')
    print(f'The gamer is on position {gamerX}, {gamerY}.')

    if getIsGamergainedTreasure():
        print(f'The treasure is yours. You have need {amountOfMoves} moves.')
        break
    if getIsGamerBeyondBoard():
        print('You fell into the abyss. Game over.')
        break
    if randint(1, 5) != 5:
        if amountAfterMove < amountBeforeMove:
            print('*' * 50)
            print('Near.. You\'re moving closer the treasure')
            print('*' * 50)
        else:
            print('*' * 50)
            print('Missing.. You\'re wandering of the treasure')
            print('*' * 50)
    if amountOfMoves >= requiredAmountOfMoves * 2:
        treasureX = randint(1, 10)
        treasureY = randint(1, 10)
        amountOfMoves = 0
        requiredAmountOfMoves = getAmountOfMovesToTreasure()
        print('The treasure run away and changed his position')
