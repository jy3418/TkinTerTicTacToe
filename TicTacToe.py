from tkinter import *
from tkinter import ttk
from winsound import *


playerSymbol = 'X'

def signin():
    global entry1
    global entry2
    global root

    root = Tk()
    root.title('Tic Tac Toe Version 1.0')

    label1 = Label(root, text="Username")
    label2 = Label(root, text="Password")
    entry1 = Entry(root)
    entry2 = Entry(root, show='*')

    label1.grid(row=0, column=0)
    label2.grid(row=1, column=0)
    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)


    check = Checkbutton(root, text="Remember me")
    button1 = Button(root, text="Play the game!", fg='red', command=checkID)
    button2 = Button(root, text="Exit Program", fg='blue', command=root.destroy, padx=10)
    check.grid(row=2, columnspan=2)
    button1.grid(row=3)
    button2.grid(row=3, column=1)
    root.mainloop()


def checkID():
    id = entry1.get()
    password = entry2.get()

    if id == 'Justin' and password == 'Youn':
        root.destroy()
        successful()
    else:
        failure()


def successful():
    root1 = Tk()
    root1.title('Success!')
    label = Label(root1, text='Log in successful.\nMoving on to the game')
    label.configure(anchor="center")
    label.pack(padx=5, pady=3)
    button = Button(root1, text='Next', command=root1.destroy)
    button.pack(pady=5)
    root1.mainloop()
    root3 = Tk()
    Game(root3)
    root3.mainloop()


def failure():
    root2 = Tk()
    root2.title('Failed to log in!')
    label = Label(root2, text='Wrong Username and Password!')
    label.configure(anchor="center")
    label.pack(padx=5, pady=3)
    label.pack()
    button = Button(root2, text='Try again', command=root2.destroy)
    button.pack()
    root2.mainloop()


class Game:
    def __init__(self, parent):
        self.parent = parent
        self.tiles = []
        self.startGame()

    def startGame(self):
        self.gameFrame = Frame(self.parent)
        self.parent.title("Tic Tac Toe: Player 1's Turn (X)")
        self.tiles = []
        global playerSymbol
        playerSymbol = 'X'

        for i in range(3):
            for j in range(3):
                tile = Tile(self.gameFrame, self.checkForWin, self.parent)
                tile.grid(row=i, column=j)
                self.tiles.append(tile)
        self.gameFrame.pack()

    def checkForWin(self):
        for x, y, z in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
            if self.tiles[x].marked == self.tiles[y].marked == self.tiles[z].marked == 'X':
                self.printResult('Player 1')
            elif self.tiles[x].marked == self.tiles[y].marked == self.tiles[z].marked == 'O':
                self.printResult('Player 2')

        # Check for tie
        counter = 0
        for i in range(9):
            if not self.tiles[i].marked == '.' and not self.tiles[i].marked == ',':
                counter += 1
        if counter == 9:
            self.printResult('Tie')

    def printResult(self, player):
        for i in range(9):
            self.tiles[i].marked = ','
        root4 = Tk()
        root4.title('Winner Winner Chicken Dinner!')
        label = Label(root4)
        if player == 'Tie':
            label.config(text='Game Tied!')
        else:
            label.config(text=player + ' Won!')
        label.configure(anchor="center")
        label.grid(row=0, columnspan=2)
        button = Button(root4, text='Play again', command=lambda: self.playAgain(root4))
        button.grid(row=1, padx=10, pady=10)
        button2 = Button(root4, text='Close Game', command=lambda: self.closeApp(root4))
        button2.grid(row=1,column=1, padx=10, pady=10)
        root4.mainloop()

    def closeApp(self, subRoot):
        subRoot.destroy()
        self.parent.destroy()

    def playAgain(self, subRoot):
        subRoot.destroy()
        for widget in self.parent.winfo_children():
            widget.destroy()
        self.startGame()


class Tile(Label):
    def __init__(self, parent, checkForWin, root):
        Button.__init__(self, parent, font=('',30), width=5, height=2, justify='center', relief='raised', bg='blue')
        self.root = root
        self.checkForWin = checkForWin
        self.bind('<Button-1>', self.markSym)
        self.marked = '.'

    def markSym(self, event):
        global playerSymbol
        if not self.marked == '.':
            return
        else:
            if playerSymbol == 'X':
                self.config(fg='black')
                self.root.title("Tic Tac Toe: Player 2's Turn (O)")
            else:
                self.config(fg='white')
                self.root.title("Tic Tac Toe: Player 1's Turn (X)")
            self.config(text=playerSymbol)
            self.marked = playerSymbol
            if playerSymbol == 'X':
                playerSymbol = 'O'
            else:
                playerSymbol = 'X'
        self.checkForWin()


def main():
    signin()


if __name__ == '__main__':
    main()