
import random

def deciding_outcome():
    a = [user_choice(),comp_choice()]
    if a in winning_combinations:
        print("Congratulations, you have defeated the computer!")
    elif a in losing_combinations:
        print("Oop, you have been trounced by the computer.")
    elif a in draw_combinations:
        print("Ooo, a tie; try again.")

def comp_choice():
    c_choice = random.randint(1,3)
    return c_choice 

def user_choice():
    print ("Pick either rock(1), paper(2) or scissors(3)")
    u_choice = int(input())
    return u_choice

winning_combinations = ([1,3],[2,1],[3,2])
losing_combinations = ([1,2],[2,3],[3,1])
draw_combinations = ([1,1],[2,2],[3,3])

deciding_outcome()