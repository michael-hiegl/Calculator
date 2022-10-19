import tkinter as tk

def write():
    screen.config(text="char")


mainwindow=tk.Tk()

size=60
pixelVirtual=tk.PhotoImage(width=1,height=1)

screen=tk.Label(mainwindow,image=pixelVirtual,text=" ",height=size,compound="c")
screen.grid(row=0,column=0)

button_C=tk.Button(mainwindow,image=pixelVirtual,text="C",height=size,width=size,compound="c")
button_C.grid(row=1,column=0)

button_perc=tk.Button(mainwindow,image=pixelVirtual,text="%",height=size,width=size,compound="c",command=write)
button_perc.grid(row=1,column=1)

button_pot=tk.Button(mainwindow,image=pixelVirtual,text="^",height=size,width=size,compound="c")
button_pot.grid(row=1,column=2)

button_div=tk.Button(mainwindow,image=pixelVirtual,text="/",height=size,width=size,compound="c")
button_div.grid(row=1,column=3)

button_7=tk.Button(mainwindow,image=pixelVirtual,text="7",height=size,width=size,compound="c")
button_7.grid(row=2,column=0)

button_8=tk.Button(mainwindow,image=pixelVirtual,text="8",height=size,width=size,compound="c")
button_8.grid(row=2,column=1)

button_9=tk.Button(mainwindow,image=pixelVirtual,text="9",height=size,width=size,compound="c")
button_9.grid(row=2,column=2)

button_mul=tk.Button(mainwindow,image=pixelVirtual,text="*",height=size,width=size,compound="c")
button_mul.grid(row=2,column=3)

button_4=tk.Button(mainwindow,image=pixelVirtual,text="4",height=size,width=size,compound="c")
button_4.grid(row=3,column=0)

button_5=tk.Button(mainwindow,image=pixelVirtual,text="5",height=size,width=size,compound="c")
button_5.grid(row=3,column=1)

button_6=tk.Button(mainwindow,image=pixelVirtual,text="6",height=size,width=size,compound="c")
button_6.grid(row=3,column=2)

button_sub=tk.Button(mainwindow,image=pixelVirtual,text="-",height=size,width=size,compound="c")
button_sub.grid(row=3,column=3)

button_1=tk.Button(mainwindow,image=pixelVirtual,text="1",height=size,width=size,compound="c")
button_1.grid(row=4,column=0)

button_2=tk.Button(mainwindow,image=pixelVirtual,text="2",height=size,width=size,compound="c")
button_2.grid(row=4,column=1)

button_3=tk.Button(mainwindow,image=pixelVirtual,text="3",height=size,width=size,compound="c")
button_3.grid(row=4,column=2)

button_add=tk.Button(mainwindow,image=pixelVirtual,text="+",height=size,width=size,compound="c")
button_add.grid(row=4,column=3)

button_dec=tk.Button(mainwindow,image=pixelVirtual,text=".",height=size,width=size,compound="c")
button_dec.grid(row=5,column=0)

button_0=tk.Button(mainwindow,image=pixelVirtual,text="0",height=size,width=size,compound="c")
button_0.grid(row=5,column=1)

button_res=tk.Button(mainwindow,image=pixelVirtual,text="=",height=size,width=128,compound="c")
button_res.place(x=136,y=338)











mainwindow.mainloop()










