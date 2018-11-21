
from tkinter import *
from random import *
from math import *


root=Tk()
root.title("tisic_striel")
canvas=Canvas(root,width=600,height=400)
canvas.pack(side=LEFT)
def Clear():
	canvas.delete("all")

def shoot1():
	for x in range (1,1000):
		x1=randint(1,600)
		y1=randint(1,600)
		if x1<200:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="red")
		elif x1>200 and x1<400 and y1<200:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="green")
		elif x1>200 and x1<400 and y1>200:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="blue")

		elif x1>400 and y1<133:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="yellow")
		elif x1>400 and y1>133 and y1<266:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="white")
		elif x1>400 and y1>266:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="black")

def shoot2():
	xs=300
	ys=200
	for x in range(1,1000):
		x1=randint(1,600)
		y1=randint(1,600)
		d=round(sqrt((x1-xs)*(x1-xs)+(y1-ys)*(y1-ys)))
		if d<80 and x1<300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="green")
		elif d<80 and x1>300 and y1<200:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="blue")
		elif d<80 and x1>300 and y1>200:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="yellow")
		if d>80:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="red")
def shoot3():
	for x in range(1,1000):
		x1=randint(1,600)
		y1=randint(1,600)
		if x1>300 and y1<200:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="red")
		elif 2*x1+3*y1>1200 and y1>200 :
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="green")
		elif  2*x1+3*y1<1200 and x1<300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="yellow")





def shoot4():
	xs1=300
	ys1=1
	xs2=600
	ys2=200
	for x in range(1,1000):
		x1=randint(1,600)
		y1=randint(1,600)
		d1=round(sqrt((x1-xs1)*(x1-xs1)+(y1-ys1)*(y1-ys1)))
		d2=round(sqrt((x1-xs2)*(x1-xs2)+(y1-ys2)*(y1-ys2)))
		d3=round(sqrt((x1-xs2)*(x1-xs2)+(y1-ys2)*(y1-ys2)))
		
		if d1<300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="blue")
		if d2<200:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="red")
		if d1<300 and d2<200:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="yellow")
		if d1>300 and d2>200 and d3>200:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="green")


buttonClear=Button(root,text="clear",command=Clear)
buttonClear.pack()

buttonStrely1=Button(root,text="strely1",command=shoot1)
buttonStrely1.pack()
buttonStrely2=Button(root,text="strely2",command=shoot2)
buttonStrely2.pack()
buttonStrely3=Button(root,text="strely3",command=shoot3)
buttonStrely3.pack()

buttonStrely4=Button(root,text="strely4",command=shoot4)
buttonStrely4.pack()





root.mainloop()