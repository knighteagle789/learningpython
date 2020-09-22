from random import randint
from os import remove, rename

def getUserScore (userName):
    try:
        inputFile = open ('userScores.txt','r')
        for line in inputFile:
            content = line.split(", ")
            if userName in content:
                return(content[1])
            else:
                continue
        return("-1")
    except IOError:
        inputFile = open ('userScores.txt','w')
        return("-1")    
    
    inputFile.close()

def updateUserPoints (newUser,userName,score):
    if newUser == True:
        inputFile = open ('userScores.txt','a')
        entry = "\n" + userName + ", " + str(score)
        inputFile.write(entry)
        inputFile.close()
        return
    else:
        tempFile = open ('userScores.tmp','w')
        inputFile = open ('userScores.txt','r')
        for line in inputFile:
            content = line.split(", ")
            if userName in content:
                entry = content[0] + ", " + str(score) + "\n"
            else:
                entry = content[0] + ", " + content[1]
            tempFile.write(entry)
        tempFile.close()
        inputFile.close()
        remove('userScores.txt')
        rename('userScores.tmp','userScores.txt')

def generateQuestion():
    operandList = [0,0,0,0,0]
    operatorList = ['','','','']
    operatorDict = {1:'+',2:'-',3:'*',4:'/',5:'**'}

    result = 500001

    while result > 50000 or result < -50000:
        for index in range(0,5):
            operandList[index] = randint(1,9)

        for index in range(0,4):
            if index > 0 and operatorList[index-1] != '**':
                operator = operatorDict[randint(1,4)]
            else:
                operator = operatorDict[randint(1,5)]
            operatorList[index] = operator
        
        openBracket = randint(0,3)
        closeBracket = randint(openBracket+1,4)

        if openBracket == 0:
            questionString = '(' + str(operandList[0])
        else:
            questionString = str(operandList[0])
        
        for index in range(1,5):
            if index == openBracket:
                questionString = questionString + operatorList[index-1] + '(' + str(operandList[index])
            elif index == closeBracket:
                questionString = questionString + operatorList[index-1]  + str(operandList[index]) + ')'
            else:
                questionString = questionString + operatorList[index-1] + str(operandList[index])
        
        result = round(eval(questionString),2)

        ### END WHILE LOOP

    questionString = questionString.replace("**","^")

    print("\n" + questionString)
    userAnswer = input("Answer (correct to 2 decimal places if not an integer): ")

    while True:
        try:
            if float(userAnswer) == result:
                print("Great Job!  You got it right!")
                return 1
            else:
                print("The correct answer is: " + result)
                return 0
        except Exception as e:
            print ("You did not enter a number.  Please try again.")
            userAnswer = input("Answer (correct to 2 decimal places if not an integer): ")