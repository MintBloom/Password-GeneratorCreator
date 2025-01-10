
import random

def deciding_outcome():
    '''the combo variable will take the user and computer choices and covert it to an [x,y] combination. This is done 
    so that a matching combination can be found in one of the tuples.''' 
    combo = [user_choice(),comp_choice()]
    if combo in winning_combinations: #checks for a match in the tuple winning_combinations
        print("Congratulations, you have defeated the computer!")
    elif combo in losing_combinations: #checks for a match in the tuple losing_combinations
        print("Oop, you have been trounced by the computer.")
    elif combo in draw_combinations: #checks for a match in the tuple draw_combinations
        print("Ooo, a tie; try again.")

#this function will return an integer which has been randomly generated via. the random module
def comp_choice():    
    c_choice = random.randint(1,3)
    print (f"The computer plays {c_choice}.")
    return c_choice
 
#this function will return a number - 1, 2, 3 - which the user has picked
def user_choice():
    print ("Pick either rock(1), paper(2) or scissors(3)")
    u_choice = int(input())
    return u_choice

'''the tuples below contain different combinations of rock, paper, scissors (1, 2, 3 respectively). These combinations represent
possible outcomes of a game of rock, paper, scissors. The outcomes have been grouped into winning, losing or leading to a draw combinations,
from the point of the user e.g winning_combinations includes all combinations in which the user wins. 
What the user plays always comes first in the combination e.g. [1,3] for this, the user has played rock(1) and the computer has played scissors(3),
hence the user wins''' 
winning_combinations = ([1,3],[2,1],[3,2])
losing_combinations = ([1,2],[2,3],[3,1])
draw_combinations = ([1,1],[2,2],[3,3])

deciding_outcome()