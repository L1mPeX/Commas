fp = open("m5-line-by-line.txt", encoding="UTF-8")
line = fp.readline()
lineN = " "
cntWords = 0
cntWordsG = 0
cntStr = 0
while len(line) != 0:
    for i in line:
        if i == ",":
            cntWordsG = cntWordsG + 1
        if i == " ":
            cntWords = cntWords + 1
    lineN = line[::-1]
    line = fp.readline()
    cntStr = cntStr + 1
fp.close()
print("The percentage of words with a comma: " + str(cntWordsG / (cntWords + cntStr) * 100) + " %")
print("The number of words with a comma: " + str(cntWordsG))
print("The number of words without a comma: " + str(cntWords+cntStr))
