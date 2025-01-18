from tkinter import *
window= Tk()#instantiate window
window.geometry("500x200")
window.title("Anjali's FIRST GUI")
icon=PhotoImage(file='logo.png')
window.iconphoto(True,icon)
window.config(background="sky blue")
window.mainloop()#place window on comp and lusten to events.