import random, math, os

def RockPaperScissor():
    List = ["rock", "paper", "scissor"]
    global Bot_points, Your_points, tie_points, rounds, winPoints
    Bot_points, Your_points, tie_points = 0, 0, 0

    rounds = int(input("\nWelcome to Rock Paper Scissor Game!, Enter a value to set rounds for match: "))
    winPoints = math.floor(rounds/2)+1

    def displayPoints(text):
        print("\n"+text+" rounds: "+str(rounds)+"\nBot points: "+str(Bot_points)+"\nYour points:"+str(Your_points)
              +"\nTie points:"+str(tie_points))

    def findWinner():
        if (Your_points == Bot_points):
            print("\nMatch Draw !")
        elif (Your_points > Bot_points):
            print("\nYou Won !")
        else:
            print("\nBot Won !")

        endGame = input("\nGame End, Want to play again? Yes-Y, No-N : ")
        if (endGame.lower() == "y"):
            os.system('cls')  # clear terminal
            RockPaperScissor()
        else:
            print("\n...........x...........")

    displayPoints("Total")  # display total rounds count & points

    def startGame():
        global Bot_points, Your_points, tie_points, rounds,  winPoint
        for i in range(0, rounds):
            # convert input to lowercase for case insensitive & strip for remove white spaces at beginning and end of the input
            user_input = input("\nEnter your choice: ").lower().strip()
            if ((user_input != "rock" and user_input != "paper") and user_input != "scissor"):
                print("Invalid Text")
                startGame()  # start game again if user input is invalid
                break

            # choose a random value in the list for bot
            bot = random.randint(0, 2)
            print("User: "+user_input+"\nBot: "+List[bot])

            # points calculation
            if (((List[bot] == "paper" and user_input == "scissor") or (List[bot] == "scissor" and user_input == "rock"))
               or (List[bot] == "rock" and user_input == "paper")):
                Your_points += 1
            elif (List[bot] != user_input):
                Bot_points += 1
            else:
                tie_points += 1
            rounds -= 1

            # display remaining rounds count with bot & user points
            displayPoints("Remaining")

            # terminate the loop if anyone gets enough points to win.
            if (Your_points == winPoints or Bot_points == winPoints):
                break
                     
    startGame()
    findWinner()

if __name__ == "__main__":
    RockPaperScissor()
