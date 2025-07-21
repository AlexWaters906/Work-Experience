import random

inputFile = open("payment-template.json","r")
outputFile = open("Output-Payment.json","a")
lineNum = 0

for x in inputFile:
    lineNum += 1
    fieldStart = x.find("<<")
    if fieldStart < 0:
        outputFile.write(x)
        continue
    fieldEnd = x.find(">>")+2
    outputFile.write(x[:fieldStart])
    if lineNum == 2:
        field = str(random.randint(1000,9999))
    elif lineNum == 4:
        amount = random.random()
        amount = amount * 100
        amount = round(amount,2)
        field = str('{0:.2f}'.format(amount))
    outputFile.write(field)
    outputFile.write(x[fieldEnd:])

outputFile.write("\n\n")


inputFile.close()
outputFile.close()

#test
