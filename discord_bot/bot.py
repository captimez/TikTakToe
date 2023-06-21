
import discord
import response
import random
from tiktaktoe_logic import player, tiktaktoe

global  player1, player2
tiktaktoe_game = None

async def send_message(message, user_message, isPrivate):
    
    try:
        res = response.handle_response(user_message)
        await message.author.send(res) if isPrivate else await message.channel.send(res)

    except  Exception as e:
        print(e, user_message)

def run_discord_bot():
    TOKEN = 'MTEwMzgxMzMxMTgwOTcyMDQzMQ.GHhSOh.74eGWPxRXSpN7HJ4h7ghPAqW6KsUAYqYu4mhVE'
    #intents = discord.Intents.all()
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')


    @client.event
    async def on_message(message):
        global tiktaktoe_game, channel

        if message.author == client.user:
            return 
        
        username = str(message.author)
        user_message = str(message.content)
        print("message: " + user_message + "by:" + username)
        
        channel = message.channel

        if user_message.startswith('!intern'):
            spieler = user_message.split(' ')
            max_anzahl = (len(spieler)-1)/2
            team1 = []
            team2 = []
            
            for c in spieler:
                   
                randm = random.randint(1,2)
                if randm == 1:
                    if c == '!intern':
                        pass
                    else:
                        
                        if len(team1) == max_anzahl:
                            team2.append(c)
                        else:
                            team1.append(c)

                else:
                    if c == '!intern':
                        pass
                    else:
                        
                        if len(team2) == max_anzahl:
                            team1.append(c)
                        else:
                            team2.append(c)


            def print_teams():
                    teams = '__**Team CHAD:**__\n'
                    teams+= '\n'
                    
                    for i in team1:
                        teams += f'--{i.upper()}--\n'

                    teams+= '\n'
                    teams += '__**Team :**__\n'
                    teams+= '\n'

                    for j in team2:
                        teams += f'--{j.upper()}--\n'

                    return teams    
                    
            await channel.send(print_teams())



        if user_message.startswith('!tiktaktoe'):
            message_content = user_message.split(' ')

            if tiktaktoe_game == None:
                player1 = player(':x:',message.author)
                player2 = player(':o:',message.mentions[0])
                tiktaktoe_game = tiktaktoe(player1,player2)
            
            await start_game()
            
        else:
            await send_message(message, user_message, isPrivate=False)

    async def start_game():
        global channel, tiktaktoe_game
        def wait_for_move(player):
            def check(message):
                if message.author == tiktaktoe_game.currentPlayer.name:
                    try:
                        row, col = [int(x) for x in message.content.split()]
                        if 0 <= row <=2 and 0 <= col <= 2:
                            
                            return True
                        else:
                            return False
                    except ValueError:
                        return False
                    
            return check

        await channel.send(f'Player1: {tiktaktoe_game.player1.name}, {tiktaktoe_game.player1.symbol}')
        await channel.send(f'Player2: {tiktaktoe_game.player2.name}, {tiktaktoe_game.player2.symbol}\n')
        await channel.send(tiktaktoe_game.print_grid())

        while not tiktaktoe_game.game_over():

            #await channel.send(f'<@{tiktaktoe_game.currentPlayer.name}>, gib deine Koordinaten ein (z.B. "0 0" für das obere linke Feld):')
            move = await client.wait_for('message', check= wait_for_move(tiktaktoe_game.currentPlayer))
            
            row, col = [int(x) for x in move.content.split()]
            if tiktaktoe_game.make_move(row, col):
                await channel.send(tiktaktoe_game.print_grid())
                tiktaktoe_game.switch_player()
            else:
                await channel.send('Ungültiges Feld')
            
            

        winner = tiktaktoe_game.get_winner()
        if winner == 'Tie':
            await channel.send("The game is tied")
            #tiktaktoe_game.reset()
        else:
            await channel.send(f"{winner} wins!!!")
            #tiktaktoe_game.reset()
        
    client.run(TOKEN)
