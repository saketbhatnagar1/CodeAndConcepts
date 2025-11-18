import tkinter

window = tkinter.Tk()
window.title("First GUI Program")
window.minsize(width=500, height=500)

# Label
mylabel = tkinter.Label(text="I am a label", font=("Arial", 24, "italic"))
mylabel.pack()


def button_click():
    print("I GOT CLICKED")
    mylabel.config(text="I got clicked lol")
    # Change the button text
    button.config(text="LOL")


# Create button and pass the function
button = tkinter.Button(text="Click me", command=button_click)
button.pack()




#ENTRY

input = tkinter.Entry()





window.mainloop()
