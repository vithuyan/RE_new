def luckCheck(str):
    stringList = list(str)
    leftSum = 0
    rightSum = 0
    half = int(len(stringList)/2)

    for i in range(0, half):
        leftSum += int(stringList[i])

    for j in range(half, len(stringList)):
        rightSum += int(stringList[j])
