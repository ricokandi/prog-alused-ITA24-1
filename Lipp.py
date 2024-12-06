from tkinter import *
 
raam = Tk()
raam.title("Kiviõli lipp")

tahvel = Canvas(raam, width=600, height = 350)

tahvel.create_rectangle(0, 0, 600, 150, fill="darkblue")
tahvel.create_rectangle(0, 150, 600, 200, fill="white")
tahvel.create_rectangle(0, 200, 600, 350, fill="saddle brown")


tahvel.pack()
raam.mainloop()