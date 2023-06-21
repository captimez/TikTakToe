#NO USE
#NO USE

import random
from tiktaktoe_logic import player, tiktaktoe

tiktaktoe_game = None


def handle_response(message) -> str:
    
    message_list = message.split(" ")
    x = random.randint(1,6)
    
    if message == "!roll":
        return str(x)
    
    #if message == "!intern":
        
    
    
    if message_list[0] == '!move':
        if tiktaktoe_game!= None:
            tiktaktoe_game.current_player.make_move(message_list[1],message_list[2])
            return 
        else:
            return 'start a game first: !tiktaktoe'
    
    if message_list[0] == '!tiktaktoe':
        print("ttt")
        if (message_list[1] != '') and (message_list[2] != ''):
            tiktaktoe_game = tiktaktoe(player('X',message_list[1]), player('O',message_list[2]))
            tiktaktoe_game.start_game()
            return tiktaktoe_game.game_initialized()
        else:
            return 'Pls enter players: !tiktaktoe @player1 @player2'
        
    
   

    