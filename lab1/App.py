import copy
import random

allPlayers = []

randomPlayer = True

rules = {
    "rock": ["paper", "scissors"],
    "paper": ["scissors", "rock"],
    "scissors": ["rock", "paper"]
}

gamemovestatistic = [["rock", 0], ["paper", 0], ["scissors", 0]]

def game():
    playerStatistic = []

    roundnumber = 0
    while roundnumber != 10000:
        move = decition(playerStatistic)
        playerMove = takePlayerMove()

        countmoves(playerMove)

        gameresult = resultdecition(playerMove, move)

        playerStatistic.append([roundnumber, playerMove, move, gameresult])
        if not randomPlayer:
            print("Player Statistic: ", playerStatistic)

        roundnumber += 1
        print("Game Statistic: ", gamemovestatistic)
        ratio(playerStatistic)
        pass

    allPlayers.append(playerStatistic)

def ratio(playerstatistic):
    lostroundcount = 0
    for round in playerstatistic:
        if round[3] == "L":
            lostroundcount += 1

    print("AI win ratio: ", (lostroundcount / len(playerstatistic)) * 100)

def resultdecition(pmove, amove):
    if rules[pmove][0] == amove:
        return "L"
    elif rules[pmove][1] == amove:
        return "W"
    else:
        return "D"

def decition(playerStatistic):
    moves = ["rock", "paper", "scissors"]
    if len(playerStatistic) == 0:
        return random.choice(moves)
    else:
        if playerStatistic[len(playerStatistic) - 1][3] == "W":
            return rules[playerStatistic[len(playerStatistic) - 1][1]][0]
        else:
            lastmove = playerStatistic[len(playerStatistic) - 1][1]

            gamemovestatistic_copy = copy.deepcopy(gamemovestatistic)

            gamemovestatistic_copy = sorted(gamemovestatistic_copy, key=lambda x: x[1], reverse=True)

            print("Sorted Game Statistic: ", gamemovestatistic_copy)

            for st in gamemovestatistic_copy:
                if st[0] != lastmove:
                    return rules[st[0]][0]

def countmoves(pmove):
    if pmove == "rock":
        gamemovestatistic[0][1] += 1
    elif pmove == "paper":
        gamemovestatistic[1][1] += 1
    else:
        gamemovestatistic[2][1] += 1

def takePlayerMove():
    moves = ["rock", "paper", "scissors"]
    if randomPlayer:
        return random.choice(moves)

    print("1- rock\n2- paper\n3- scissors")
    decition = input("choose: ")

    if decition == "1":
        return "rock"
    elif decition == "2":
        return "paper"
    else:
        return "scissors"

game()