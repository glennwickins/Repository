import tkinter as tk
from tkinter import ttk
import random
import time

def initiateGame(turn, name):
    global playerScore
    game(turn)
    writeScoreboard(name)
    

def game(playerTurn):
    """Calculates the winner and returns the new score"""
    global playerScore
    pyTurn = random.randint(0,2)
    options = ['paper', 'rock', 'scissors']
    pyTurn = options[pyTurn]
    # message
    replyMessage = tk.Label(text='   Computer chooses:   ')
    replyMessage.grid(column=1, row=5)
    time.sleep(1)
    replyMessage = tk.Label(text='   Computer chooses: %s   ' %(pyTurn))
    replyMessage.grid(column=1, row=5)

    if pyTurn == 'rock' and playerTurn == 'paper' or pyTurn == 'paper' and playerTurn == 'scissors' or pyTurn == 'scissors' and playerTurn == 'rock':
        replyMessage = tk.Label(text='   You win!!   ')
        replyMessage.grid(column=1, row=6)
        playerScore += 1
        updateScoreboard()

    if pyTurn == 'rock' and playerTurn == 'scissors' or pyTurn == 'paper' and playerTurn == 'rock' or pyTurn == 'scissors' and playerTurn == 'paper':
        replyMessage = tk.Label(text='   You lose!!   ')
        replyMessage.grid(column=1, row=6)
        playerScore -= 1
        updateScoreboard()

    if pyTurn == 'rock' and playerTurn == 'rock' or pyTurn == 'paper' and playerTurn == 'paper' or pyTurn == 'scissors' and playerTurn == 'scissors':
        replyMessage = tk.Label(text='   It\'s a draw!!   ')
        replyMessage.grid(column=1, row=6)
    if loggedIn == True:
        writeScoreboard()


def goButtonPressed():
    loggedIn = True
    name = login.current()
    name = listOfNames[name]
    # Welcome line
    welcome = tk.Label(text='User: %s.            \n                    Hello, %s                    ' %(name, name), font=('Times New Roman', 10))
    welcome.grid(column=1, row=1, pady=5)



def writeScoreboard(name):
    writeScore = open('PRSHighscore_%s.txt' %(name), 'w')
    writeScore.write(str(playerScore))     
    writeScore.close()


def readScoreboard(name):
    global playerScore
    try:
        readScore = open('PRSHighscore_%s.txt' %(name))
        for line in readScore:
            playerScore = readScore.readline()
        readScore.close()

    except:
        score = 0
    updateScoreboard()
    return score

# Scoreboard - FIX THIS and call it everytime score changes
def updateScoreboard():
    global playerScore
    if loggedIn == True:
        try:
            playerScore = readScoreboard(name)
        except:
            pass
    scoreBoard = tk.Label(text='Your score: ' + str(playerScore), font=('Times New Roman', 14))
    scoreBoard.grid(column=1, row=7, pady=10)
  

playerScore = 0
playerName = ""
window = tk.Tk()
window.title('Paper, Rock, Scissors')        # Window title

window.geometry('335x400')  # Window size

# Title
title = tk.Label(text='Welcome to \nPaper, Rock, Scissors', font=('Times New Roman', 20))
title.grid(column=1, row=0, pady=10)

# Welcome line
welcome = tk.Label(text='User: Guest. \nLogin to store your high score.', font=('Times New Roman', 10))
welcome.grid(column=1, row=1, pady=5)

# Combo box and go button
loggedIn = False    
listOfNames = ('Glenn', 'Kate', 'Mikayla', 'Kyle')
login = ttk.Combobox(window, values=listOfNames)
login.grid(row=2, column=1)

goButton = tk.Button(text="Log in", command=lambda *args:goButtonPressed())
goButton.grid(row=2, column=2)

# Paper button
paperButton = tk.Button(text='Paper', bg='paleturquoise', command=lambda *args:initiateGame('paper', playerName))
paperButton.grid(column=0, row=3, padx=2)


# Rock button
rockButton = tk.Button(text='Rock', bg='lightsalmon', command=lambda *args:initiateGame('rock', playerName))
rockButton.grid(column=1, row=3, padx=2)


# Scissors button
scissorsButton = tk.Button(text='Scissors', bg='mediumspringgreen', command=lambda *args:initiateGame('scissors', playerName))
scissorsButton.grid(column=2, row=3, padx=2)


#Instructions label
instructionsLabel = tk.Label(text='Click on a word to play')
instructionsLabel.grid(column=1, row=4, pady=10)

# Scoreboard
updateScoreboard()

# Quit button
quitButton = tk.Button(text='Quit', bg='white')
quitButton.grid(column=1, row=8)
quitButton['command'] = window.destroy


window.mainloop()





