from tkinter import * #type: ignore
import requests

def get_quote():
    response = requests.get(url = "https://api.kanye.rest")
    kanye_quotes = response.json()["quote"]
    canvas.itemconfig(quote_text, text=f"{kanye_quotes}")

response = requests.get(url = "https://api.kanye.rest")
kanye_quotes = response.json()["quote"]

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="Day-26-Python/kanye_west_quotes_api/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=f"{kanye_quotes}", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="Day-26-Python/kanye_west_quotes_api/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()