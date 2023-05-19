from tkinter import * #type: ignore

window = Tk()
window.title("Mile To Km")
window.config(padx = 10, pady = 10)

mile_input = Entry(width = 6)
mile_input.grid(row = 1, column = 2)

mile_text = Label(text = "Miles")
mile_text.grid(row = 1, column = 3)

equal_text = Label(text = "Equal to:")
equal_text.grid(row = 2, column = 1)

km_output = Label(text = 0)
km_output.grid(row = 2, column = 2)

km_text = Label(text = "Km")
km_text.grid(row = 2, column = 3)


def convert():
    from_mile = float(mile_input.get())
    to_km = from_mile * 1.60934
    km_output.config(text = to_km)

calculate = Button(text = "Calculate", command = convert)
calculate.grid(row = 3, column = 2)

window.mainloop()