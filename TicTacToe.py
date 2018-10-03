from tkinter import *
from tkinter import ttk

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
    label = Label(root1, text='Log in successful.\nMoving on to game phase 1')
    label.configure(anchor="center")
    label.pack(padx=5, pady=3)
    button = Button(root1, text='Next', command=root1.destroy)
    button.pack(pady=5)
    root1.mainloop()


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
        self.currentTile = 'X'
        self.tiles = []
        self.startGame()

    def startGame(self):
        self.gameFrame = Frame(self.parent)

        for i in range(3):
            for j in range(3):
                tile = Tile(self.gameFrame, self.checkForWin)
                tile.grid(row=i, column=j)
                self.tiles.append(tile)
        self.gameFrame.pack()

    def checkForWin(self):
        for x, y, z in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
            if self.tiles[x].marked == self.tiles[y].marked == self.tiles[z].marked == 'X':
                print('p1 won')
            elif self.tiles[x].marked == self.tiles[y].marked == self.tiles[z].marked == 'Y':
                print('p2 won')


class Tile(Label):
    def __init__(self, parent, checkForWin):
        Button.__init__(self, parent, font=('',30), width=5, height=2, justify='center', relief='raised')
        self.checkForWin = checkForWin
        self.bind('<Button-1>', self.markSym)
        self.marked = '.'

    def markSym(self, event):
        global playerSymbol
        if not self.marked == '.':
            return
        else:
            self.config(text=playerSymbol)
            self.marked = playerSymbol
            if playerSymbol == 'X':
                playerSymbol = 'O'
            else:
                playerSymbol = 'X'
        self.checkForWin()


def main():
    root3 = Tk()
    Game(root3)
    root3.mainloop()
    #signin()


if __name__ == '__main__':
    main()