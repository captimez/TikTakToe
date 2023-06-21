from array import *


class tiktaktoe:
    global background

    def __init__(self,player1,player2):
        self.background = ":heavy_minus_sign:"
        self.gameGrid = [[self.background,self.background,self.background],[self.background,self.background,self.background],[self.background,self.background,self.background]]
        self.player1 = player1
        self.player2 = player2
        self.currentPlayer = player1
        
        
        
    def game_initialized(self):
        
        return f'Game has been initalized: Player1: {self.player1.name} | {self.player1.symbol} Player2: {self.player2.name} | {self.player2.symbol}'

    
        
    def game_over(self):
        return self.get_winner() is not None or self.grid_full()


    def make_move(self, row, col):
        if self.gameGrid[row][col]is not self.background:
            return False
        else:
            self.gameGrid[row][col] = self.currentPlayer.symbol
            return True

    def grid_full(self):
        for i in self.gameGrid:
            for k in i:
                if self.background in k:
                    return False
                
        return True

    def get_winner(self):
        for i in range(3):
            # prüfe zeile
            if self.gameGrid[i][0] == self.gameGrid[i][1] == self.gameGrid[i][2] != self.background:
                return self.gameGrid[i][0]
            # prüfe spalte
            if self.gameGrid[0][i] == self.gameGrid[1][i] == self.gameGrid[2][i] != self.background:
                return self.gameGrid[0][i]
        # prüfe diagonalen
        if self.gameGrid[0][0] == self.gameGrid[1][1] == self.gameGrid[2][2] != self.background:
            return self.gameGrid[0][0]
        if self.gameGrid[0][2] == self.gameGrid[1][1] == self.gameGrid[2][0] != self.background:
            return self.gameGrid[0][2]
        if self.grid_full():
            return 'Tie'
        return None

    async def get_move(self, player):
        await player.make_move()
        return player.move
    
    #Ausgabe des Spielfeldes
    def print_grid(self):
        count = 0
        row1= ""
        row2= ""
        row3= ""
        #return f'{grid[0][0]}|{grid[0][1]}|{grid[0][2]}\n {grid[1][0]}|{grid[1][1]}|{grid[1][2]} \n {grid[2][0]}|{grid[2][1]}|{grid[2][2]}'
        for i in self.gameGrid:
            for j in i:
                if count==0:
                    #row1 += "|"+ j + "|"
                    row1 += j
                    print(j)
                if count ==1:
                    #row2 += "|"+ j + "|"
                    row2 += j
                    print(j)
                if count ==2:
                    #row3 += "|"+ j + "|"
                    row3 += j
                    print(j)

            count+=1
            top = ':white_small_square::black_small_square::white_small_square::black_small_square::white_small_square:'
        return f'{top}\n:black_small_square:{row1}:black_small_square:\n:white_small_square:{row2}:white_small_square:\n:black_small_square:{row3}:black_small_square:\n{top}'
        #return f'`Spielfeld: \n {row1} \n {row2} \n {row3}`'

    def switch_player(self):
        if self.currentPlayer == self.player1:
            self.currentPlayer = self.player2
        else:
            self.currentPlayer = self.player1

    #def game_loop(grid, ):
    async def run_game():
        #torungame
        pass

class player:
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name
       # self.id  = id
        self.previous_move = None

    def player_made_move(self):
       return self.previous_move != self.move

    async def make_move(self, row, col):
        
        if self.previous_move != (row,col):
            self.move= (row,col)

        
    
        
        