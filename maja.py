from tkinter import *
raam = Tk()
raam.title("Maja")
tahvel = Canvas(raam, width=600, height = 600)

tahvel.create_rectangle(150, 300, 450, 600, fill="gray")
tahvel.create_rectangle(200, 600, 250, 500, fill="black")
tahvel.create_polygon(150,300,450,300,300,150, fill="red",outline="black")
tahvel.create_rectangle(350,500,400,550, fill="lightblue")


tahvel.pack()
raam.mainloop()