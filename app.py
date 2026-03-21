from tkinter import *
import Pathfinding as pp
window = Tk()
window.title("Projet graphe")
window.geometry("400x300")
window.minsize(800, 600)
window.iconbitmap("500px-LogoPrincipalImperiumHumanité.ico")
window.configure(bg="white")
frame = Frame(window)

titre=Label(frame,text="Projet graphe",bg="white",fg="black",font=("Times 20 bold",30))
titre.pack()

titre=Label(frame,text="choisissez un graphe",bg="white",fg="black",font=("Times 20 bold",30))
titre.pack(expand="yes")
frame.pack()
button=Button(window, text="ok")
button.configure(command=pp.click)
button.pack()

window.mainloop()
