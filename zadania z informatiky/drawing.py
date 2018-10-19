from tkinter import *
import random

Try=0
vyska=500
sirka=500

root=Tk()
canvas=Canvas(root,width=sirka,height=vyska)
canvas.pack()

leftFrame=Frame(root)
leftFrame.pack()
rightFrame=Frame(root)
rightFrame.pack(side=RIGHT)

def maketarget():
	x1=20
	y1=20
	x2=225
	y2=225
	for x in range(0,5):
		canvas.create_oval(x1,y1,x2,y2,fill="white")
		x1+=20
		y1+=20
		x2-=20
		y2-=20
def canvasclear():

	canvas.delete("all")
def shoot():
	global Try
	R1=random.randint(1,226)
	R2=random.randint(1,226)
	R3=R1-3
	R4=R2-3
	canvas.create_oval(R1,R2,R3,R4,fill="black")
	Try+=1
def Msg():
	global Try
	msg = Tk()
	msg.geometry("250x50+500+300")
	msg.title("Message")
	print(Try)
	label_msg=Label(msg,text=Try).pack()

button1=Button(rightFrame,text="target",command=maketarget)
button1.pack()
button2=Button(rightFrame,text="clear",command=canvasclear)
button2.pack()
button3=Button(rightFrame,text="shoot",command=shoot)
button3.pack()
button4=Button(rightFrame,text="message",command=Msg)
button4.pack()

root.mainloop()
