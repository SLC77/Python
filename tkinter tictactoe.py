# import tkinter as tk

# class TicTacToe:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Tic Tac Toe")
#         self.buttons = []
#         for i in range(3):
#             row = []
#             for j in range(3):
#                 button = tk.Button(self.root, width=10, height=5)
#                 button.grid(row=i, column=j)
#                 row.append(button)
#             self.buttons.append(row)
#             self.turn_label = tk.Label(self.root, text="Player X's turn")
#             self.turn_label.grid(row=3, column=0, columnspan=3)

# def button_clicked(self, i, j):
#     button = self.buttons[i][j]
#     button.config(text="X")
#     self.turn_label.config(text="Player O's turn")
#     for i in range(3):
#             for j in range(3):
#                  self.buttons[i][j].config(command=lambda i=i, j=j: self.button_clicked(i, j))

# if __name__ == "__main__":
#      game = TicTacToe()
#      game.root.mainloop

##### IMPORT ###
import tkinter as tk

# ## Players name
# Player_1 = str(input('Name for player 1 as X : '))
# Player_2 = str(input('Name for player 2 as O : '))
# stop_game = False

##Lauching GUI with TK

root = tk.Tk() #Creating the GUI
root.title('Tic Tac Toe Championship')
root.resizable(0,0)

for x in range(3):
    root.columnconfigure(x, weight=1, minsize=100)
    root.rowconfigure(x, weight=1, minsize=75)
    for y in range(3):
        frame = tk.Frame(
            master=root,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=x, column=y, padx=10, pady=10)
        label = tk.Label(master=frame, text=f"\n\nrow {x}\t\t {y}\n\n")
        label.pack()

root.mainloop()




