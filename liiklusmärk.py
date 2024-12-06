from tkinter import *
raam = Tk()
raam.title("Liiklusmärk")
tahvel = Canvas(raam, width=600, height=600)


tahvel.create_oval(0,0,600,600, fill="red")
tahvel.create_oval(25,25,575,575, fill="white")
tahvel.create_oval(35,35,565,565, fill="red")
tahvel.create_rectangle(100,225,500,375, fill="white")


tahvel.pack()
raam.mainloop()