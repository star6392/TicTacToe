#GAME FILES

from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[1]+' | '+ board[2]+' | '+board[3])
    print('---------')
    print(board[4]+' | '+ board[5]+' | '+board[6])
    print('---------')
    print(board[7]+' | '+ board[8]+' | '+board[9])

    
def player_input():
    #KEEP ASKING FOR CORRECT INPUT
    marker_1 = ''
    
    while marker_1.upper() != 'X' and marker_1.upper() != 'O':
        marker_1=input(f'{player_1} Choose your marker (X/O): ')
    
    if marker_1.upper()=='X':
        marker_2='O'
        
    else:
        marker_2='X'
        
    return (marker_1.upper(),marker_2.upper())
   
def place_marker(board, marker, position):
            board[position]=marker      
    
def win_check(board,mark):
    
    return (board[1]==board[2]==board[3]==mark or  
    board[4]==board[5]==board[6]==mark or          
    board[7]==board[8]==board[9]==mark or          
    board[1]==board[4]==board[7]==mark or 
    board[2]==board[5]==board[8]==mark or
    board[3]==board[6]==board[9]==mark or 
    board[1]==board[5]==board[9]==mark or 
    board[3]==board[5]==board[7]==mark)  
    
import random

def choose_first():
    if random.randint(0,2)==0:
        return player_1
    else:
        return player_2  
    
    
def space_check(board, position):
    return board[position]==' '    
    
    
def full_board_check(board):
    for num in range(1,10):
        if space_check(board,num):
            return False
        
    return True       
    
def player_choice(board,player):
    while True:
        player_pos_desired=int(input(f'{player},please enter your desired position (1-9): ')) 
        if player_pos_desired in list(range(1,10)):
            if space_check(board,player_pos_desired):
                return (player_pos_desired)
            else:
                print('Position already taken,please try again')
                continue
    
        else:
            print('Input is invalid,please try again')
            continue
        
        
def replay():
    x=input('Would you like to try again ?(Y/N):')
    return x.lower()[0]=='y'    

#GAME

print('Welcome to Tic Tac Toe!')

while True:
    tictactoe_board=[' ']*10
    
    
    #SETTING UP THE PLAYERS AND THEIR MARKERS  
    while True:
        player_1=input('Player 1,Enter your name: ')
        player_2=input('Player 2,Enter your name: ')
        
        if player_1==player_2:
            print("Player names can't be same.Please try again")
            continue
        else:
            break
            
    (marker_1,marker_2)=player_input()
    print(player_1 + f' has chosen {marker_1}')
    print(player_2 + f' has been given {marker_2}')
    
    #TURN
    
    turn=choose_first()
    
    print(f'{turn} will go first')
    
    
    start_play=input('Are you ready to play?(Y/N): ')
    
    if start_play.lower().startswith('y'):
        game_on=True
        
    else:
        game_on=False
        
    
    while game_on:
    
        if player_1==turn: 
        #Player 1 Turn
        
            display_board(tictactoe_board)       
            player_1_pos=player_choice(tictactoe_board,player_1)
            
            place_marker(tictactoe_board,marker_1,player_1_pos)
            
            if win_check(tictactoe_board,marker_1):
                display_board(tictactoe_board)
                print(f'Congratulations,{player_1} has won!!!' )
                
                game_on=False
            else:

                if full_board_check(tictactoe_board):
                    display_board(tictactoe_board)
                    print("It's a tie")
                    
                    game_on=False
                else:
                    turn=player_2
                    
        
        else:
            
        # Player2's turn.
          
        
            display_board(tictactoe_board)       
            player_2_pos=player_choice(tictactoe_board,player_2)
            place_marker(tictactoe_board,marker_2,player_2_pos)
            
            if win_check(tictactoe_board,marker_2):
                display_board(tictactoe_board)
                print(f'Congratulations,{player_2} has won!!!')
                
                game_on=False
            else:
                
                if full_board_check(tictactoe_board):
                    display_board(tictactoe_board)
                    print("It's a tie")
                    
                    game_on=False
                    
                else:
                    turn=player_1  

    if not replay():
        print('Thanks for playing :-)')
        break
