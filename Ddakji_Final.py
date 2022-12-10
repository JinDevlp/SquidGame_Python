import random 
from enum import IntEnum

class RpcGame(IntEnum):
    Rock = 0
    Paper = 1 
    Scissors = 2 

class Ddakji(IntEnum):
    Front = 0
    Back = 1

def user_selection():
    user_input = int(input("Enter a choice: (0(Rock), 1(Paper), 2(Scissors) " ))
    choice = RpcGame(user_input)
    return choice

def recruiter_selection():
    recruiter_input = random.randint(0,2)
    choice = RpcGame(recruiter_input)
    return choice

# All Ddakjis start with front side up!
def user_hit():
    user = Ddakji(random.randint(0,1))
    return user 

def recruiter_hit():
    recruiter = Ddakji(random.randint(0,1))
    return recruiter

def hit_result(user,recruiter):
    game_over = False 
    while not game_over:
        # No change
        if user == Ddakji.Front and recruiter == Ddakji.Front:
            print(f"It's a tie! You both did not flip the ddakji. Go again! ")
            break
        elif recruiter == Ddakji.Back:
            print(f"Recruiter flipped over your ddakji. You lose")
            game_over = True 
        
        elif user == Ddakji.Back:
            print("You flipped over the recruiter's ddakji. You win")
            game_over = True 

def rpc_game(user, recruiter):
    game_over = False 
    while not game_over:
        # Tie
        if user == recruiter:
            print(f"It's a tie! Recruitee chose: {user.name} and Recruiter chose: {recruiter.name} Go again")
            user = user_selection()
            recruiter = recruiter_selection()
            rpc_game(user,recruiter)
            
        # User == Rock
        elif user == RpcGame.Rock:
            if recruiter == RpcGame.Paper:
                print(f"Paper wins over Rock. You lose")
                recruiter = recruiter_hit()
                print(recruiter)
                user = user_hit()
                print(user)
                hit_result(user,recruiter)
                game_over = True
            else:
                print("Rock wins over Scissors. You win ")
                user = user_hit()
                print(user)
                recruiter = recruiter_hit()
                print(recruiter)
                hit_result(user,recruiter)
                game_over = True 
            
        # User == Paper        
        elif user == RpcGame.Paper:
            if recruiter == RpcGame.Scissors:
                print(f"Scissors wins over Paper. You lose")
                recruiter = recruiter_hit()
                print(recruiter) 
                user = user_hit()
                print(user)
                hit_result(user,recruiter)
                game_over = True
            else:
                print("Paper wins over Rock. You win ")
                user = user_hit()
                print(user)
                recruiter = recruiter_hit()
                print(recruiter)
                hit_result(user,recruiter)
                game_over = True 
            
        # User == Scissors
        elif user == RpcGame.Scissors:
            if recruiter == RpcGame.Rock:
                print(f"Rock wins over Scissors. You lose")
                recruiter = recruiter_hit()
                print(recruiter)
                user = user_hit()
                print(user)
                hit_result(user,recruiter)
                game_over = True
            else:
                print("Scissors wins over Paper. You win ")
                user = user_hit()
                print(user)
                recruiter = recruiter_hit()
                print(recruiter)
                hit_result(user,recruiter)
                game_over = True 



try:
    user = user_selection()
except:
    print("invalid slection. Enter a correct numerical value! (0,1,2): ")
    
recruiter = recruiter_selection()
rpc_game(user, recruiter)
    

        
        
    

# game_over = False 
# while not game_over:
#     recruitee = input("Enter a choice: (Rock, Paper, Sciossors) " ).lower()
#     rpc_choices = ["rock", "paper", "scissors"]
#     recruiter = random.choice(rpc_choices)
#     if recruiter == recruitee:
#         print(f"It's a tie! Recruitee chose: {recruitee} and Recruiter chose: {recruiter} Go again")

        
#     elif recruitee == 'rock':
#         if recruiter == 'paper':
#             print("Paper wins rock. Recruiter win! Recruiter goes first")
#         elif recruiter == 'scissors':
#             print("Rock wins over scissors. Recruitee win! Recruitee goes first")
#         game_over = True 
            
#     elif recruitee == 'paper':
#         if recruiter == 'rock':
#             print("Paper wins over rock. Recruitee win! Recruitee goes first")
#         elif recruiter == 'scissors':
#             print("Scissors win over paper. Recruiter win! Recruiter goes first")
#         game_over = True 
        
    
#     elif recruitee == 'scissors':
#         if recruiter == 'rock':
#             print("Rock wins over scissors. Recruiter wins! Recruiter goes first")
#         elif recruiter == 'paper':
#             print("Scissors win over paper. Recuitee wins! Recruitee goes first")
#         game_over = True 
        