from tkinter import *

class TicTacToe:
    def __init__(self, root, b, states):  
        for i in range(3):
            for j in range(3):
                b[i][j] = Button(font=('Verdana', 56), width=3, bg='yellow',command = lambda r=i,c=j: self.callback(r,c))
                b[i][j].grid(row = i, column = j)
        self.player = 'X'
        self.stop_game = False
        

    def check_for_winner(self):
        for i in range(3):
            if states[i][0]==states[i][1]==states[i][2]!=0:
                b[i][0].configure(bg='grey')
                b[i][1].configure(bg='grey')
                b[i][2].configure(bg='grey')
                self.stop_game = True

        for i in range(3):
            if states[0][i]==states[1][i]==states[2][i]!=0:
                b[0][i].configure(bg='grey')
                b[1][i].configure(bg='grey')
                b[2][i].configure(bg='grey')
                self.stop_game = True

        if states[0][0]==states[1][1]==states[2][2]!=0:
            b[0][0].configure(bg='grey')
            b[1][1].configure(bg='grey')
            b[2][2].configure(bg='grey')
            self.stop_game = True

        if states[2][0]==states[1][1]==states[0][2]!=0:
            b[2][0].configure(bg='grey')
            b[1][1].configure(bg='grey')
            b[0][2].configure(bg='grey')
            self.stop_game = True

    def callback(self,r,c):
        if self.player == 'X' and states[r][c] == 0 and self.stop_game==False:
            b[r][c].configure(text='X', fg='blue', bg='white')
            states[r][c] = 'X'
            self.player = 'O'
        if self.player == 'O' and states[r][c] == 0 and self.stop_game==False:
            b[r][c].configure(text='O', fg='orange', bg='black')
            states[r][c] = 'O'
            self.player = 'X'
        self.check_for_winner()


frame = Tk()
b = [[0,0,0],[0,0,0],[0,0,0]]
states = [[0,0,0],[0,0,0],[0,0,0]]
t = TicTacToe(frame,b,states)
frame.mainloop()