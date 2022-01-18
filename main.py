from tkinter import *
from tkinter import ttk,messagebox,filedialog
import requests

API_KEY = "74cb91ba31960c91d3871be2"
URL_CODES = f"https://v6.exchangerate-api.com/v6/{API_KEY}/codes"

r = requests.get(URL_CODES)
codes = r.json()

currency_codes = {}
currency_name = []
currency_ab = []

for code in codes["supported_codes"]:
    currency_codes[code[1]] = code[0]

    currency_ab.append(code[0])
    currency_name.append(code[1])

root = Tk()
root.title("Currency Convertor")
root.iconphoto(True,PhotoImage(file="icon.png"))
root.geometry("750x400")

def submit():
    URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency_codes[cur1.get()]}/{currency_codes[cur2.get()]}/{amount_entry.get()}"

    r = requests.get(URL)
    res = r.json()

    result = res["conversion_result"]

    messagebox.showinfo("Currency Convertor",f"{amount_entry.get()} {cur1.get()} is {result} {cur2.get()}")

    return result

def swap(): 
    one = cur1.get()
    two = cur2.get()

    cur2.set(one)
    cur1.set(two)

def save():
    f = filedialog.asksaveasfilename(title="Currency Convertor",filetypes=(
        ("Text Files","*.txt"),
    ))

    with open(f"{f}.txt","w") as file:
        file.write(str(submit()))
    
    messagebox.showinfo("Currency Convertor","File Saved!")

Label(root,text="Currency Convertor",font=("Pacifico",24)).grid(row=0,column=0,padx=10)

cur1 = ttk.Combobox(root,values=currency_name,font=("Calibri",15))
cur1.grid(row=1,column=0,padx=10)
cur1.set("Choose one Currency")

Label(root,text="to",font=("Calibri",15)).grid(row=1,column=1)

cur2 = ttk.Combobox(root,values=currency_name,font=("Calibri",15))
cur2.grid(row=1,column=2,padx=10)
cur2.set("Choose one Currency")

img = PhotoImage(file="swap.png")
swap_btn = Button(root,image=img,command=swap)
swap_btn.grid(row=2,column=1)

Label(root,text="Amount: ",font=("Calibri",15)).grid(row=3,column=0,padx=10,pady=10)

amount_entry = Entry(root,font=("Calibri",15))
amount_entry.grid(row=3,column=1,pady=10)

submit_btn = Button(root,text="Convert",font=("Calibri",15),command=submit)
submit_btn.grid(row=4,column=1,pady=20)

save_btn = Button(root,text="Save",font=("Calibri",15),command=save)
save_btn.grid(row=5,column=1,pady=20)

root.mainloop()
