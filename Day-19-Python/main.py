from tkinter import * #type: ignore

window = Tk()
window.title("Tkinter GUI Program")
window.minsize(width = 500, height = 300)

# Label
label = Label(text = "Button not clicked", font=("Arial", 25, "bold"))
label.grid(row = 1, column = 1)

# Button
def button_clicked():
    user_input = input.get()
    label["text"] = user_input


input = Entry(width = 15)
input.grid(row = 3, column = 4)

button = Button(text = "click me!", command = button_clicked)
button.grid(row = 2, column = 2)

new_button = Button(text = "new button!")
new_button.grid(row = 1, column = 3)


window.mainloop()
