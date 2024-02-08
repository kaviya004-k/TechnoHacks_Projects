from tkinter import *
import random

def next_turn(row, column):

    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+"'s turn"))

            elif check_winner() is True:
                label.config(text=(players[0]+" wins!"), fg= "yellow", bg = "red")

            elif check_winner() == "Tie":
                label.config(text="It's a Tie!", fg= "yellow", bg = "red")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+"'s turn"))

            elif check_winner() is True:
                label.config(text=(players[1]+" wins!"), fg= "yellow", bg = "red")

            elif check_winner() == "Tie":
                label.config(text="It's a Tie!", fg= "yellow", bg = "red")

def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="firebrick")
            buttons[row][1].config(bg="firebrick")
            buttons[row][2].config(bg="firebrick")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="firebrick")
            buttons[1][column].config(bg="firebrick")
            buttons[2][column].config(bg="firebrick")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="firebrick")
        buttons[1][1].config(bg="firebrick")
        buttons[2][2].config(bg="firebrick")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="firebrick")
        buttons[1][1].config(bg="firebrick")
        buttons[2][0].config(bg="firebrick")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="midnightblue")
        return "Tie"

    else:
        return False


def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def new_game():

    global player

    player = random.choice(players)

    label.config(text=player+"'s turn", fg = "white" , bg ="purple")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="teal")


window = Tk()
window.title("Tic-Tac-Toe")
players = ["X","O"]
window.configure(bg = "purple")
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

welcome = Label(text = "Tic Tac Toe", font= ("arial", 40, "bold"), height = 1, width =10, fg = "greenyellow", bg = "purple" )
welcome.pack(side = "top")

label = Label(text=player + "'s turn", font=('arial',30), bg = "purple", fg = "snow")
label.pack(side="top")

reset_button = Button(text="Restart", font=('ivy',20), command=new_game, bg = "lightsalmon", fg = "indigo")
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40), width=3, height=1, bg = "teal", fg = "white",
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)

window.mainloop()
