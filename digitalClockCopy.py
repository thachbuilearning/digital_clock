
from tkinter import Tk, Label

window = Tk()
window.title("Digital Clock")
window.geometry("600x300")
window.configure(bg="green")

label = Label(window, text="ThachClone29 - Newmember : Hello !", font=("Arial Black", 78, "bold"), bg="green", fg="white")
label.pack(pady=100)

window.mainloop()
