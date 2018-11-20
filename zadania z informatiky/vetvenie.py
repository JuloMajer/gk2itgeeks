from tkinter import *
from random import *
from math import *


root=Tk()
root.title("tisic_striel")
canvas=Canvas(root,width=600,height=600)
canvas.pack(side=LEFT)
def Clear():
	canvas.delete("all")


def shoot1():
	for x in range (1,1000):
		x1=randint(1,600)
		y1=randint(1,600)
		if x1<300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="red")
		else:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="green")
	print(x)

def shoot2():
	for x in range (1,1000):
		x1=randint(1,600)
		y1=randint(1,600)
		if y1<300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="blue")
		else:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="yellow")
	print(x)

def shoot3():
	for x in range (1,1000):
		x1=randint(1,600)
		y1=randint(1,600)
		if x1<200:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="red")
		elif x1>200 and x1<400:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="yellow")
		elif x1>400:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="green")
	print(x)

def shoot4():
	for x in range (1,1000):
		x1=randint(1,600)
		y1=randint(1,600)
		if x1<300 and y1<300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="red")
		elif x1<300 and y1>300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="green")
		elif x1>300 and y1<300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="blue")
		elif x1>300 and y1>300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="yellow")
	print(x)

def shoot5():
	for x in range (1,1000):
		x1=randint(1,600)
		y1=randint(1,600)
		if x1<200 and y1<300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="red")
		elif x1>200 and x1<400 and y1<300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="white")
		elif x1>400 and y1<300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="green")
		elif x1<300 and y1>300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="blue")
		elif x1>300 and y1>300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="yellow")
	print(x)

def shoot6():
	for x in range(1,1000):
		x1=randint(1,600)
		y1=randint(1,600)
		if x1>y1:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="red")
		else:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="blue")



def shoot7():
	for x in range(1,1000):
		x1=randint(1,600)
		y1=randint(1,600)
	
		if x1+y1>600 :	canvas.create_oval(x1,y1,x1+5,y1+5,fill="red")
		else:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="blue")

def shoot8():
	for x in range(1,1000):
		x1=randint(1,600)
		y1=randint(1,600)
		if x1>y1 and x1+y1<600 :
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="red")
		elif x1>y1 and x1+y1>600 :
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="blue")
		elif x1<y1 and x1+y1<600 :
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="green")
		elif x1<y1 and x1+y1>600 :
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="yellow") 

def shoot9():
	for x in range(1,1000):
		x1=randint(1,600)
		y1=randint(1,600)
		if y1<60:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="red")
		elif y1>60 and y1<120:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="orange")
		elif y1>120 and y1<180:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="yellow")
		elif y1>180 and y1<240:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="green")
		elif y1>240 and y1<300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="blue")
		elif y1>300 and y1<360:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="purple")
		elif y1>360 and y1<420:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="magenta")
		elif y1>420 and y1<480:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="pink")
		elif y1>480 and y1<540:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="white")
		elif y1>540 and y1<600:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="black")

def shoot10():
	canvas.create_oval(300,300,300+5,300+5,fill="black")
	xs=300
	ys=300
	
	for x in range(1,1000):
		x1=randint(1,600)
		y1=randint(1,600)
		d=round(sqrt((x1-xs)*(x1-xs)+(y1-ys)*(y1-ys)))
		if d<100:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="hotpink")
def shoot11():
	xs=300
	ys=300
	for x in range(1,1000):
		x1=randint(1,600)
		y1=randint(1,600)
		d=round(sqrt((x1-xs)*(x1-xs)+(y1-ys)*(y1-ys)))
		if d<100 and d>80:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="black")
		elif d<80 and x1<300 and y1<300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="blue")
		elif d<80 and x1<300 and y1>300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="white")
		elif d<80 and x1>300 and y1<300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="white")
		elif d<80 and x1>300 and y1>300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="blue")
def shoot12():
	canvas.create_polygon((0, 100, 50, 0, 100, 100), fill="red")
	canvas.create_polygon((0, 25, 100, 25, 50, 125), fill="red")
def shoot13():
	xs1=250
	ys1=300
	xs2=350
	ys2=300

	for x in range(1,1000):
			x1=randint(1,600)
			y1=randint(1,600)
			d1=round(sqrt((x1-xs1)*(x1-xs1)+(y1-ys1)*(y1-ys1)))
			if d1<100:
				canvas.create_oval(x1,y1,x1+5,y1+5,fill="red")	


			d2=round(sqrt((x1-xs2)*(x1-xs2)+(y1-ys2)*(y1-ys2)))
			if d2<100:
				canvas.create_oval(x1,y1,x1+5,y1+5,fill="green")


			d3=round(sqrt((x1-xs1)*(x1-xs1)+(y1-ys1)*(y1-ys1)))
			if d1<100 and d2<100:
				canvas.create_oval(x1,y1,x1+5,y1+5,fill="blue")	



def shoot14():
	xs1=300
	ys1=1
	xs2=600
	ys2=300
	for x in range(1,1000):
		x1=randint(1,600)
		y1=randint(1,600)
		d1=round(sqrt((x1-xs1)*(x1-xs1)+(y1-ys1)*(y1-ys1)))
		d2=round(sqrt((x1-xs2)*(x1-xs2)+(y1-ys2)*(y1-ys2)))
		d3=round(sqrt((x1-xs2)*(x1-xs2)+(y1-ys2)*(y1-ys2)))
		
		if d1<300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="blue")
		if d2<300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="red")
		if d1<300 and d2<300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="yellow")
		if d1>300 and d2>300 and d3>300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="green")
		

def shoot15():
	xs=300
	ys=300
	for x in range(1,1000):
		x1=randint(1,600)
		y1=randint(1,600)
		d=round(sqrt((x1-xs)*(x1-xs)+(y1-ys)*(y1-ys)))
		if d<80 and x1<300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="green")
		elif d<80 and x1>300 and y1<300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="blue")
		elif d<80 and x1>300 and y1>300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="yellow")
		if d>80:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="red")


def shoot16():
	for x in range(1,1000):
		x1=randint(1,600)
		y1=randint(1,600)
		if x1<200:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="red")
		elif x1>200 and x1<400 and y1<300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="blue")
		elif x1>200 and x1<400 and y1>300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="green")

		elif x1>400 and y1<200:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="pink")
		elif x1>400 and y1>200 and y1<400:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="white")
		elif x1>400 and y1>400:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="yellow")

def shoot17():
	for x in range(1,1000):
		x1=randint(1,600)
		y1=randint(1,600)
		if x1>300 and y1<300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="red")
		elif x1+y1>600 and y1>300 :
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="green")
		elif  x1+y1<600 and x1<300:
			canvas.create_oval(x1,y1,x1+5,y1+5,fill="yellow")



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
buttonStrely5=Button(root,text="strely5",command=shoot5)
buttonStrely5.pack()
buttonStrely6=Button(root,text="strely6",command=shoot6)
buttonStrely6.pack()
buttonStrely7=Button(root,text="strely7",command=shoot7)
buttonStrely7.pack()
buttonStrely8=Button(root,text="strely8",command=shoot8)
buttonStrely8.pack()
buttonStrely9=Button(root,text="strely9",command=shoot9)
buttonStrely9.pack()
buttonStrely10=Button(root,text="strely10",command=shoot10)
buttonStrely10.pack()
buttonStrely11=Button(root,text="strely11",command=shoot11)
buttonStrely11.pack()
buttonStrely12=Button(root,text="strely12",command=shoot12)
buttonStrely12.pack()
buttonStrely13=Button(root,text="strely13",command=shoot13)
buttonStrely13.pack()
buttonStrely14=Button(root,text="strely14",command=shoot14)
buttonStrely14.pack()
buttonStrely15=Button(root,text="strely15",command=shoot15)
buttonStrely15.pack()
buttonStrely16=Button(root,text="strely16",command=shoot16)
buttonStrely16.pack()
buttonStrely17=Button(root,text="strely17",command=shoot17)
buttonStrely17.pack()



root.mainloop()
