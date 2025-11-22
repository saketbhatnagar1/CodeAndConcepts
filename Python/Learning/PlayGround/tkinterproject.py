from tkinter import *

window = Tk()
window.title("FIRST GUI PROGRAM")
window.geometry("800x600")
#LABEL

my_label = Label(text="I am a Label",font=("Arial",25,"bold"))
my_label.pack(side="right")



def button_click():
    text = input.get()
    my_label.config(text=text)
    
input = Entry(width=10)
input.pack()







button = Button(text="ClcikM<e",command=button_click)
button.pack()

window.mainloop()