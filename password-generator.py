
import time
import re
import string
import secrets

def menu():
    print("----------------------------------------------------------")
    print("Welcome to Password Generator.")
    valid = False
    while valid == False:
        print("Would you like to create your own password, generate one, or end the program?") # option to create or generate a password
        time.sleep(1)  
        print("     - Generate")
        print("     - Create")
        print("     - Terminate")
        user_choice = input("").lower()
        print("----------------------------------------------------------")
        time.sleep(1) 
        if user_choice == "create":
            valid = True
            user_password = create_password()
            retype_pswd(user_password)
            menu()
        elif user_choice == "generate":
            valid = True
            pswd_generator()
            menu()
        elif user_choice == "terminate":
            valid = True
        else:
            valid = False
            print("Please pick again.")
            input("")

def create_password():
    print("\nYour password must fulfill these conditions:")     # the lines below set the conditions for creating a password
    time.sleep(1)                                 
    print("\n    1. Include a lowercase and UPPERCASE letter")
    print("    2. Include a number")
    print("    3. Include a special character")
    print("    4. Length between 8 and 20 characters long")
    time.sleep(1)
    new = False
    while new == False:
        user_password = str(input("\nNew Password, make sure you remember it!: "))    ### loop that checks the created password fullfills the right conditions  ### 
        if 7 >= len(user_password) or 21 <= len(user_password) or re.search('[A-Z]', user_password) is None or re.search('[0-9]', user_password) is None or re.search('[a-z]', user_password) is None or re.search('[^a-zA-Z0-9]', user_password) is None:                             
            print("\nYour password must include an UPPERCASE letter.")
            print("Your password must include an lowercase letter.")
            print("Your password must include a number.")
            print("Your password must include a special character.")
            print("Your password must be between 8 and 20 characters long.")
            new = False
        else:
            print("Password is probably fairly strong :)")
            new = True
    time.sleep(1)
    return user_password

def pswd_generator():
    var = False
    while var == False:
        print("----------------------------------------------------------")
        try:
            char_length = int(input("\nHow many characters long do you wish your password to be? (8-20) "))
            if char_length <8 or char_length >20:
                print("Number is outwith the suggested range, please try again.")
                time.sleep(3)
                var = False
            if 20 >= char_length >= 8 :
                var = True
                user_pswd = password_generator(char_length)
                print(f"Your password is:   {user_pswd}")
                retype_pswd(user_pswd)
        except:
            var = False
            print("Error please try again.")
            time.sleep(1)

def retype_pswd(pswd):
    var = False
    input("\nPress enter to retype password.")
    print("----------------------------------------------------------")
    retyped_password = str(input("\nRetype password: "))       ### prompt to retype password ###
    while var == False:          ### loop for retyping password ###
        if retyped_password == pswd:
            var = True
            print("\nPassword valid! Keep it safe.")
            time.sleep(1)
            print("Press Enter to restart")
            input("")
            print("----------------------------------------------------------")
            print("You will be sent back to the main menu in: 3s")
            time.sleep(3)
        else:
            print("Sorry this does not match the original, try again. ")
            time.sleep(0.5)
            retyped_password = str(input(f"\nRestart (r) or please retype password: "))    ### option to retype password, or restart the programme ###
            if retyped_password == 'r':
                var = True           ### restarts code from the top ###
            else:
                var = False

def password_generator(width):
    lowercase = string.ascii_lowercase          ### variable for the set of lowercase letters ###
    uppercase = string.ascii_uppercase          ### variable for the set of uppercase letters ###
    digits = string.digits                      ### variable for the set of digits ###
    special_characters = string.punctuation + "£"    ### variable for the set of punctuation and special characters ##
    length = width                 ### sets the length of password that the generator will create ###
    characters = lowercase + uppercase + digits + special_characters    ### the characters the generator will pick from, to scramble ###
    user_password = "".join(secrets.choice(characters) for i in range(length))  ### generates the password ###
    return user_password

menu()