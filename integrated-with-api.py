import tkinter as tk
from tkinter import ttk
import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data['rates'][target_currency]

def convert_currency():
    try:
        amount = float(entry_amount.get())
        base_currency = combobox_base_currency.get()
        target_currency = combobox_target_currency.get()
        rate = get_exchange_rate(base_currency, target_currency)
        converted_amount = amount * rate
        label_result.config(text=f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
    except Exception as e:
        label_result.config(text=f"Error: {e}")

root = tk.Tk()
root.title("Aplikasi Konversi Mata Uang")

label_amount = tk.Label(root, text="Jumlah:")
label_amount.grid(column=0, row=0, padx=10, pady=10)
entry_amount = tk.Entry(root)
entry_amount.grid(column=1, row=0, padx=10, pady=10)

label_base_currency = tk.Label(root, text="Dari Mata Uang:")
label_base_currency.grid(column=0, row=1, padx=10, pady=10)
combobox_base_currency = ttk.Combobox(root, values=["USD", "EUR", "IDR", "JPY", "GBP"])
combobox_base_currency.grid(column=1, row=1, padx=10, pady=10)
combobox_base_currency.current(0)

label_target_currency = tk.Label(root, text="Ke Mata Uang:")
label_target_currency.grid(column=0, row=2, padx=10, pady=10)
combobox_target_currency = ttk.Combobox(root, values=["USD", "EUR", "IDR", "JPY", "GBP"])
combobox_target_currency.grid(column=1, row=2, padx=10, pady=10)
combobox_target_currency.current(1)

button_convert = tk.Button(root, text="Konversi", command=convert_currency)
button_convert.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

label_result = tk.Label(root, text="Hasil akan muncul di sini")
label_result.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

root.mainloop()
