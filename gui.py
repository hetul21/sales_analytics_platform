import tkinter as tk
from db import Session
from models import Customer

root = tk.Tk()

root.title("Sales Analytics Platform")
root.geometry("900x600")

title= tk.Label(
    root,
    text = 'Sales Analytics Dashboard',
    font= ("Arial",20, "bold")
)


title.pack(pady=20)

def load_customers():
    listbox.delete(0, tk.END)
    session = Session()
    customers = session.query(Customer).all()
    session.close()

    for c in customers:
        listbox.insert(tk.END, f"{c.name} - {c.city}")

listbox = tk.Listbox(root, width=50)
listbox.pack()

btn = tk.Button(root, text="Load Customers", command=load_customers)
btn.pack(pady=10)

root.mainloop()



