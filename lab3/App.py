import copy
import random
import scipy.stats

def main():
    coinresults = []
    samplespace = ["head", "tail"]

    task_1f = True

    round = 0
    while (round < 3000):
        if task_1f:
            for i in ["head"] * 5 + ["tail"] * 5:
                coinresults.append(i)
            round += 1
        else:
            coinresults.append(random.choice(samplespace))


    print("Head count:", coinresults.count("head"))
    print("P-value:",
        scipy.stats.binom_test(
            x=[coinresults.count("head"), coinresults.count("tail")],
            p=.5
        )
    )

    cconprob = None

    if task_1f:
        cconprob = conProbTwoCon(coinresults)
    else:
        cconprob = conProb(coinresults)
    print(cconprob)

    print("\nBayes values:")

    if task_1f:
        bayescompTwoCon(coinresults, cconprob)
    else:
        bayescomp(coinresults, cconprob)

def bayescomp(coinresults, cconprob):
    conditions = cconprob.keys();
    for condition in conditions:
        firstp = condition[:4]
        secondp = condition[4:]

        if firstp != secondp:
            print(condition, ": ", cconprob[condition], " ?= ", sep="", end="")

            proboffirst = coinresults.count(firstp) / len(coinresults)
            probofsecond = coinresults.count(secondp) / len(coinresults)

            bayesres = (cconprob[secondp + firstp] * proboffirst / probofsecond)

            print(bayesres, " | Diff: ", abs(bayesres - cconprob[condition]), sep="")

def bayescompTwoCon(coinresults, cconprob):
    conditions = cconprob.keys()

    excconprob = conProbTwoEx(coinresults)

    for condition in conditions:
        firstp = condition[:4]
        secondp = condition[4:8]
        thirdp = condition[8:]

        print(condition, ": ", cconprob[condition], " ?= ", sep="", end="")

        proboffirst = coinresults.count(firstp) / len(coinresults)
        probofsecond = prob(secondp, thirdp, coinresults)

        bayesres = (excconprob[secondp + thirdp + firstp] * proboffirst / probofsecond)

        print(bayesres, " | Diff: ", abs(bayesres - cconprob[condition]), sep="")

def prob(f, s, coinresults):
    count = 0
    for i in range(0, len(coinresults) - 1):
        if (coinresults[i] == f and coinresults[i + 1] == s):
            count += 1
    return float(count) / len(coinresults)

def conProb(arr):
    prob = {
        "headtail": 0,
        "headhead": 0,
        "tailhead": 0,
        "tailtail": 0
    }

    for i in range(0, len(arr) - 1):
        key = arr[i + 1] + arr[i]
        prob[key] += 1

    probres = {}

    probres["headhead"] = prob["headhead"] / (prob["headhead"] + prob["tailhead"])
    probres["tailhead"] = prob["tailhead"] / (prob["headhead"] + prob["tailhead"])
    probres["headtail"] = prob["headtail"] / (prob["headtail"] + prob["tailtail"])
    probres["tailtail"] = prob["tailtail"] / (prob["headtail"] + prob["tailtail"])

    return probres

def conProbTwoCon(arr):
    prob = {
        "headheadhead": 0,
        "headheadtail": 0,
        "headtailhead": 0,
        "headtailtail": 0,
        "tailheadhead": 0,
        "tailheadtail": 0,
        "tailtailhead": 0,
        "tailtailtail": 0
    }

    for i in range(0, len(arr) - 2):
        key = arr[i + 2] + arr[i] + arr[i + 1]
        prob[key] += 1

    probres = {}

    conditions = prob.keys()

    for i in conditions:
        allspace = i[4:]
        probres[i] = prob[i] / (prob["tail" + allspace] + prob["head" + allspace])

    return probres

def conProbTwoEx(arr):
    prob = {
        "headheadhead": 0,
        "headheadtail": 0,
        "headtailhead": 0,
        "headtailtail": 0,
        "tailheadhead": 0,
        "tailheadtail": 0,
        "tailtailhead": 0,
        "tailtailtail": 0
    }

    for i in range(0, len(arr) - 2):
        key = arr[i + 1] + arr[i + 2] + arr[i]
        prob[key] += 1

    probres = {}

    conditions = prob.keys()

    for i in conditions:
        allspace = i[8:]
        probres[i] = prob[i] / (prob["tailtail" + allspace] + prob["tailhead" + allspace] + prob["headhead" + allspace] + prob["headtail" + allspace])

    return probres

if __name__ == "__main__":
    main()