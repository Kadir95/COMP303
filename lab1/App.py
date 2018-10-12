# A primitive AI that can play rock, paper, scissors.
import copy
import random

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

def aivsai():
    playerStatisticPlayer1 = []
    playerStatisticPlayer2 = []

    gamemovestatisticPlayer1 = [["rock", 0], ["paper", 0], ["scissors", 0]]
    gamemovestatisticPlayer2 = [["rock", 0], ["paper", 0], ["scissors", 0]]

    roundnumber = 0
    while roundnumber != 100000:
        player1move = decition(playerStatisticPlayer1, gamemovestatisticPlayer1)
        player2move = decition(playerStatisticPlayer2, gamemovestatisticPlayer2)

        countmoves(player2move, gms=gamemovestatisticPlayer1)
        countmoves(player1move, gms=gamemovestatisticPlayer2)

        gameresult = resultdecition(player1move, player2move)

        gameresultplayer1 = ""

        if (gameresult == "L"):
            gameresultplayer1 = "W"
        elif (gameresult == "W"):
            gameresultplayer1 = "L"
        else:
            gameresultplayer1 = "D"

        playerStatisticPlayer1.append([roundnumber, player2move, player1move, gameresultplayer1])
        playerStatisticPlayer2.append([roundnumber, player1move, player2move, gameresult])

        roundnumber += 1

    player1winstat = [0, 0, 0] #L,D,W
    for round in playerStatisticPlayer1:
        if round[3] == "L":
            player1winstat[0] += 1
        elif round[3] == "W":
            player1winstat[2] += 1
        else:
            player1winstat[1] += 1

    print ("AI player1 > L:", (player1winstat[0] / len(playerStatisticPlayer1) * 100), " D:", (player1winstat[1] / len(playerStatisticPlayer1) * 100), " W:", (player1winstat[2] / len(playerStatisticPlayer1) * 100))


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

def decition(playerStatistic, gms=gamemovestatistic):
    moves = ["rock", "paper", "scissors"]
    if len(playerStatistic) == 0:
        return random.choice(moves)
    else:
        if playerStatistic[len(playerStatistic) - 1][3] == "W":
            return rules[playerStatistic[len(playerStatistic) - 1][1]][0]
        else:
            lastmove = playerStatistic[len(playerStatistic) - 1][1]

            gamemovestatistic_copy = copy.deepcopy(gms)

            gamemovestatistic_copy = sorted(gamemovestatistic_copy, key=lambda x: x[1], reverse=True)

            print("Sorted Game Statistic: ", gamemovestatistic_copy)

            for st in gamemovestatistic_copy:
                if st[0] != lastmove:
                    return rules[st[0]][0]

def countmoves(pmove, gms=gamemovestatistic):
    if pmove == "rock":
        gms[0][1] += 1
    elif pmove == "paper":
        gms[1][1] += 1
    else:
        gms[2][1] += 1

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

#game()
aivsai()