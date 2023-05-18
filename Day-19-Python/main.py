import tkinter

window = tkinter.Tk()
window.title("Tkinter GUI Program")
window.minsize(width = 500, height = 300)

label = tkinter.Label(text = "Hello", font=("Arial", 25, "bold"))
label.pack()






window.mainloop()