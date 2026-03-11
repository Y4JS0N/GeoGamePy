import drivingsidequiz
import countrydomain

def gameHandler():

    score = 0


    while True:


        print("What quiz would you like to play?")
        gameChoice = input("Enter 1 for Drivingside or 2 for Countrydomain: ")

        if gameChoice == "1":

            gameRunning = True

            while gameRunning:
                resultDS = drivingsidequiz.ask()

                if resultDS == "help":
                    print("Enter help for this view")
                    print("Enter quit to go to main menu")
                    print("Enter score for the score")
                
                elif resultDS == "quit":
                    gameRunning = False

                elif resultDS == "score":
                    print(f"Your score is: {score}")

                elif resultDS[0] == True:
                    score += 1
                    print(f"Your Answer is {resultDS[0]}!")
                    print(f"Your new Streak is {score}!")

                else:
                    score = 0
                    print(f"The right answer for {resultDS[1]} would have been {resultDS[2]}")
                    print(f"Your new Streak is {score}!")
                
        elif gameChoice == "2":

            gameRunning = True

            while gameRunning:
                resultCD = countrydomain.ask()
        
                if resultCD == "help":
                    print("Enter help for this view")
                    print("Enter quit to go to main menu")
                    print("Enter score for the score")
                
                elif resultCD == "quit":
                    gameRunning = False

                elif resultCD == "score":
                    print(f"Your score is: {score}")

                elif resultCD[0] == True:
                    score += 1
                    print(f"Your Answer is {resultCD[0]}!")
                    print(f"Your new Streak is {score}!")

                else:
                    score = 0
                    print(f"The right answer for {resultCD[1]} would have been {resultCD[2]}")
                    print(f"Your new Streak is {score}!")

        else:
            print("fail")



if __name__ == "__main__":
    gameHandler()