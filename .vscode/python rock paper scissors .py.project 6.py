# step 1 : define the rules of the game
#step 2 : writting the code
#step 3 :understand the code

import random

user_choice =int(input("Heloo! and welcome.Type 0 for Rock,1 for Paper,2 for scissors \n : "))
computer_choice = random.randint(0,2)
print(f"Computer choose {computer_choice}")

if user_choice >=3 or user_choice < 0 :
    print("You typed an invalid number , you lose!")
elif user_choice == 0 and computer_choice == 2 :
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice :
    print("You win!")
elif user_choice > computer_choice :
    print("You win!")
elif computer_choice == user_choice :
    print("It's a draw")    
                     
    
    
    
       
    
    
    
    

          
