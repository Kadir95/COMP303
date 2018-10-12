import copy
import random
import scipy.stats

def main():
    coinresults = []
    samplespace = ["head", "tail"]

    round = 0
    while (round < 80):
        coinresults.append(random.choice(samplespace))
        round += 1

    print(coinresults.count("head"))
    print(
        scipy.stats.binom_test(
        x=[coinresults.count("head"), coinresults.count("tail")],
        p=.5)
    )
    print(conProb(coinresults))

def conProb(arr):
    prob = {
        "headtail": 0,
        "headhead": 0,
        "tailhead": 0,
        "tailtail": 0
    }

    for i in range(0, len(arr) - 1):
        key = arr[i] + arr[i + 1]

        prob[key] += 1


    probres = copy.deepcopy(prob)

    probres["headhead"] = prob["headhead"] / (prob["headhead"] + prob["headtail"])
    probres["headtail"] = prob["headtail"] / (prob["headhead"] + prob["headtail"])

    probres["tailhead"] = prob["tailhead"] / (prob["tailhead"] + prob["tailtail"])
    probres["tailtail"] = prob["tailtail"] / (prob["tailhead"] + prob["tailtail"])

    return probres

if __name__ == "__main__":
    main()