from tkinter import *
vyska=500
sirka=500
sticks=17
x1=75
y1=150
M=20
V=40
H=10
winner=0
mem=0

game=Tk()
game.title("palicky_game")
canvas=Canvas(game,width=sirka,height=vyska)
canvas.pack()


def Restart():
	canvas.delete("all")
	global sticks
	global mem
	sticks=17
	mem=0
	stamprlik()
	windowclose()

def checkB():
	if sticks<=0:
		print("ziadne palicky")
		global winner_window
		winner_window = Tk()
		winner_window.geometry("250x50+500+300")
		winner_window.title("the winner is...")
		labelB=Label(winner_window,text="blue player wins",fg="blue")
		labelB.pack()
		Restartbutton=Button(winner_window,text="Play_again",command=Restart)
		Restartbutton.pack()

def checkR():
	if sticks<=0:
		print("ziadne palicky")
		global winner_window
		winner_window = Tk()
		winner_window.geometry("250x50+500+300")
		winner_window.title("the winner is...")
		labelR=Label(winner_window,text="red player wins",fg="red")
		labelR.pack()
		Restartbutton=Button(winner_window,text="Play_again",command=Restart)
		Restartbutton.pack()
	
def windowclose():
	global winner_window
	winner_window.destroy()

def stamprlik ():
	canvas.delete("all")
	for x in range(0,sticks):
		global x1
		canvas.create_rectangle(x1,y1,x1+H,y1+V,fill="magenta")
		x1+=M
	x1=75

stamprlik()

def Undo(x):
	global sticks
	print(x)
	sticks+=x
	stamprlik()
	buttonUndo.pack_forget()

	

def take1B():
	print("test")
	global sticks
	global mem
	sticks-=1
	mem=1
	checkB()
	stamprlik()
	buttonB1.pack_forget()
	buttonB2.pack_forget()
	buttonB3.pack_forget()
	buttonR1.pack(side=LEFT)
	buttonR2.pack(side=LEFT)
	buttonR3.pack(side=LEFT)
	buttonUndo.pack(side=RIGHT)

def take2B():
	print("test")
	global sticks
	global mem
	sticks-=2
	mem=2
	checkB()
	stamprlik()
	buttonB1.pack_forget()
	buttonB2.pack_forget()
	buttonB3.pack_forget()
	buttonR1.pack(side=LEFT)
	buttonR2.pack(side=LEFT)
	buttonR3.pack(side=LEFT)
	buttonUndo.pack(side=RIGHT)

def take3B():
	print("test")
	global sticks
	global mem
	sticks-=3
	mem=3
	checkB()
	stamprlik()
	buttonB1.pack_forget()
	buttonB2.pack_forget()
	buttonB3.pack_forget()
	buttonR1.pack(side=LEFT)
	buttonR2.pack(side=LEFT)
	buttonR3.pack(side=LEFT)
	buttonUndo.pack(side=RIGHT)

def take1R():
	print("test")
	global sticks
	global mem
	sticks-=1
	mem=1
	checkR()
	stamprlik()
	buttonB1.pack(side=LEFT)
	buttonB2.pack(side=LEFT)
	buttonB3.pack(side=LEFT)
	buttonR1.pack_forget()
	buttonR2.pack_forget()
	buttonR3.pack_forget()
	buttonUndo.pack(side=RIGHT)

def take2R():
	print("test")
	global sticks
	global mem
	sticks-=2
	mem=2
	checkR()
	stamprlik()
	buttonB1.pack(side=LEFT)
	buttonB2.pack(side=LEFT)
	buttonB3.pack(side=LEFT)
	buttonR1.pack_forget()
	buttonR2.pack_forget()
	buttonR3.pack_forget()
	buttonUndo.pack(side=RIGHT)

def take3R():
	print("test")
	global sticks
	global mem
	sticks-=3
	mem=3
	checkR()
	stamprlik()
	buttonB1.pack(side=LEFT)
	buttonB2.pack(side=LEFT)
	buttonB3.pack(side=LEFT)
	buttonR1.pack_forget()
	buttonR2.pack_forget()
	buttonR3.pack_forget()
	buttonUndo.pack(side=RIGHT)

def end_game():
	game.destroy()


buttonB1=Button(game,text="blue_1",command=take1B,fg="blue")
buttonB1.pack(side=LEFT)
buttonB2=Button(game,text="blue_2",command=take2B,fg="blue")
buttonB2.pack(side=LEFT)
buttonB3=Button(game,text="blue_3",command=take3B,fg="blue")
buttonB3.pack(side=LEFT)

buttonR1=Button(game,text="red_1",command=take1R,fg="red")
buttonR2=Button(game,text="red_2",command=take2R,fg="red")
buttonR3=Button(game,text="red_3",command=take3R,fg="red")

buttonQ=Button(game,text="quit",command=end_game)
buttonQ.pack(side=RIGHT)

buttonUndo=Button(game,text="undo",command= lambda: Undo(mem))
buttonUndo.pack(side=RIGHT)


game.mainloop()