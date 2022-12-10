# 12/09/2022

# Go against the opponent 1 VS 1
# 1. Rock/ Paper/ Scissors to choose who goes first 
# 2. Each person gets a Ddakji
# 3. Person who won rock/paper/scissors goes first. 
# 4. Goal is to flip your opponent's ddakji on the ground by striking it with your own ddakji.


import random 


game_over = False 
while not game_over:
    recruitee = input("Enter a choice: (Rock, Paper, Sciossors) " ).lower()
    rpc_choices = ["rock", "paper", "scissors"]
    recruiter = random.choice(rpc_choices)
    if recruiter == recruitee:
        print(f"It's a tie! Recruitee chose: {recruitee} and Go again")

        
    elif recruitee == 'rock':
        if recruiter == 'paper':
            print("Paper wins rock. Recruiter win! Recruiter goes first")
        elif recruiter == 'scissors':
            print("Rock wins over scissors. Recruitee win! Recruitee goes first")
        game_over = True 
            
    elif recruitee == 'paper':
        if recruiter == 'rock':
            print("Paper wins over rock. Recruitee win! Recruitee goes first")
        elif recruiter == 'scissors':
            print("Scissors win over paper. Recruiter win! Recruiter goes first")
        game_over = True 
        
    
    elif recruitee == 'scissors':
        if recruiter == 'rock':
            print("Rock wins over scissors. Recruiter wins! Recruiter goes first")
        elif recruiter == 'paper':
            print("Scissors win over paper. Recuitee wins! Recruitee goes first")
        game_over = True 
        