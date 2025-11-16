# THe game() fn in a  program lets a user paly a game and return the hi-score as an integer
# you need to read a file "hi-score.txt" 
# write a program to update the hi-score whenever the game() fn breaks the previous hisco

import random
def game():
    print("YOU ARE PLAYING A GAME!!")
    score=random.randint(1,10000)
#   Fetch the hiscore
    with open("chapter 9/6.2.txt") as f:
        hiscore=f.read()
        if(hiscore!=""):
           hiscore= int(hiscore)

        else: 
            hiscore=0


    print(f"Your score is:{score}")
    if (score>hiscore):
            # write this new hiscore to the file
        with open("chapter 9/6.2.txt","w") as f:
            f.write(str(score))
    
    return score
game()