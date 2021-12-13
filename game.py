ai='X'
human='O'
#from shutil import get_terminal_size
class Board:

    a=[['-','-','-'],['-','-','-'],['-','-','-']]

    def __init__(self):
        pass


    def cell(self,c):
        if c=='-':
            return " "
        else:
            return c

    def printBoard(self):
        print('*'*13)
        print("*   |   |   *")

        print("* "+self.cell(self.a[0][0])+" | "+self.cell(self.a[0][1])+" | "+ self.cell(self.a[0][2])+" *")
        print("*   |   |   *")
        print("*-----------*")
        print("*   |   |   *")
        print("* "+self.cell(self.a[1][0])+" | "+self.cell(self.a[1][1])+" | "+ self.cell(self.a[1][2])+" *")
        print("*   |   |   *")
        print("*-----------*")
        print("*   |   |   *")
        print("* "+self.cell(self.a[2][0])+" | "+self.cell(self.a[2][1])+" | "+ self.cell(self.a[2][2])+" *")
        print("*   |   |   *")
        print('*'*13)
        print("\n")

    def move(self,player,x,y):
        if (player=='X' or player=='O') and self.a[x][y]=='-':
            self.a[x][y]=player
            return True
        else:
            return False

    
    def movesLeft(self,cells):
        left=0
        for i in range(3):
            for j in range(3):
                if cells[i][j]=='-':
                    left=+1
        return left

    @staticmethod
    def evaluate(cells):
        
        for row in range(3):
            if (cells[row][0] == cells[row][1] and cells[row][0]==cells[row][2]):
                if(cells[row][0]==ai):
                    return 100
                if(cells[row][0]==human):
                    return -100
            
        for col in range(3):
            if (cells[0][col] == cells[1][col] and cells[0][col] == cells[2][col]):
                if (cells[0][col]==ai):
                    return 100
                if (cells[0][col]==human):
                    return -100

        if (cells[0][0]==cells[1][1] and cells[1][1]==cells[2][2]):
            if cells[0][0]==ai:
                return 100
            if cells[0][0]==human:
                return -100
        
        if (cells[0][2]==cells[1][1] and cells[1][1]==cells[2][0]):
            if cells[0][2]==ai:
                return 100
            if cells[0][2]==human:
                return -100
            
        return 0



    def nextMove(self):
        maxscore=-10000
        move=None
        cells=self.a.copy()
        #print(cells)
        for i in range(3):
            for j in range(3):
                if cells[i][j]=='-':
                   cells[i][j]=ai
                   score=self.minimax(cells,0,False)
                   if(maxscore<score):
                       move=(i,j)
                       maxscore=score
                   cells[i][j]='-'
        return move

    def clear(self):
        for i in range(3):
            for j in range(3):
                self.a[i][j]='-'


    
    def minimax(self,cells,depth,isMax):
        arr=cells.copy()
        score=Board.evaluate(cells)
        #print(score)
        if score==100:
            return score
        elif score==-100:
            return score

        if self.movesLeft(cells)==0:
           return 0

        if isMax:
            best=-1000

            for i in range(3):
                for j in range(3):
                    if arr[i][j]=='-':
                        arr[i][j]=ai
                        best=max(best, self.minimax(arr,depth+1,not isMax))
                        arr[i][j]='-'

            return best
        else:
            best=1000

            for i in range(3):
                for j in range(3):
                    if arr[i][j]=='-':
                        arr[i][j]=human
                        best=min(best, self.minimax(arr,depth+1,not isMax))
                        arr[i][j]='-'

            return best



if __name__=="__main__":

    b=Board()
    print(f"You: {human}\nComputer: {ai}\nYou go first.")


    while(True):
        b.printBoard()
        while True:
            
            move=int(input(f"enter the cell number of your move 1-9({human})\n"))

            if 1<=move<=9:
                move-=1
                if b.a[move//3][move%3]=='-':
                    b.move(human,move//3, move%3)
                    b.printBoard()
                    #print(Board.evaluate(b.a))
                    if Board.evaluate(b.a)==-100:
                        print('You win')
                        break
                    else:
                        if (b.movesLeft(b.a)==0):
                            print('TIE')
                            break
                        else:
                            move=b.nextMove()
                            b.move(ai,move[0],move[1])
                            print('Computer Move')
                            b.printBoard()
                            if Board.evaluate(b.a)==100:
                                print('You lose')
                                break
                            elif (b.movesLeft(b.a)==0):
                                print('TIE')
                                break
                else:
                    print('Place Occupied. Try again.')
                    continue
            else:
                print('enter number between 1 and 9.')
        
        b.clear()
        print('-'*40)
        inp=input("do you want to play a new game?[Y/n]\n")
        if(inp=='n'):
            print('Thanks for playing')
            break
        else:
            ai,human=human,ai
            print(f"You: {human}\nComputer: {ai}\nYou go first.")
