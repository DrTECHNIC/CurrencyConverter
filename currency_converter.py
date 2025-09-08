import tkinter as tk
from tkinter import ttk


def convert():
    val = float(entry_value.get())
    cur1 = combo_from.get()
    cur2 = combo_to.get()
    currency = {
        "USD": 0.012,
        "EUR": 0.01,
        "RUB": 1,
        "IDR": 202.06,
        "KZT": 6.63,
        "GBP": 0.0091
    } # НА МОМЕНТ 13:45 05.09.2025
    result = val / currency[cur1] * currency[cur2]
    label_result.config(text=f"{val} {cur1} = {result} {cur2}")


root = tk.Tk()
root.title("Конвертер валют")

root.resizable(False, False)

tk.Label(root, text="Сумма:").grid(row=0, column=0, padx=5, pady=5)
entry_value = tk.Entry(root)
entry_value.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Из:").grid(row=1, column=0, padx=5, pady=5)
combo_from = ttk.Combobox(root, values=["USD", "EUR", "RUB", "IDR", "KZT", "GBP"])
combo_from.current(2)
combo_from.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="В:").grid(row=2, column=0, padx=5, pady=5)
combo_to = ttk.Combobox(root, values=["USD", "EUR", "RUB", "IDR", "KZT", "GBP"])
combo_to.current(0)
combo_to.grid(row=2, column=1, padx=5, pady=5)

button_convert = tk.Button(root, text="Конвертировать", command=convert)
button_convert.grid(row=3, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="")
label_result.grid(row=4, column=0, columnspan=2)

root.eval('tk::PlaceWindow . center')
root.mainloop()