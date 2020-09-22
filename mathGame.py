try:
    import myPythonFunctions as m

    userName = input('''Please enter you user name or 
    create a new one if this is the first time 
    you are running the program: ''')

    userScore = int(m.getUserScore(userName))
    
    newUser = False
    if userScore == -1:
        newUser = True
        userScore = 0
    
    userChoice = 0

    while userChoice != '-1':
        userScore += m.generateQuestion()
        print ("Current Score: ", userScore)
        userChoice = input("Press Enter to continue or -1 to Exit: ")
    
    m.updateUserPoints(newUser, userName, str(userScore))

except Exception as e:
    print ("An unexpected error occurred. Program wil be exited. Error: \n" + e)