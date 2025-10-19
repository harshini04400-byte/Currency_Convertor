import tkinter as tk

# Conversion rates
USD_TO_INR = 83.0
INR_TO_USD = 1 / USD_TO_INR

def convert():
    amount = entry.get()
    if not amount:
        result_label.config(text="Enter amount")
        return

    try:
        value = float(amount)
    except ValueError:
        result_label.config(text="Invalid input")
        return

    if var.get() == "USD to INR":
        converted = value * USD_TO_INR
        result_label.config(text=f"{converted:.2f} INR")
    else:
        converted = value * INR_TO_USD
        result_label.config(text=f"{converted:.2f} USD")

# Create main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("300x200")

# Entry for amount
tk.Label(root, text="Enter amount:").pack(pady=5)
entry = tk.Entry(root)
entry.pack()

# Option menu
var = tk.StringVar(value="USD to INR")
options = ["USD to INR", "INR to USD"]
tk.OptionMenu(root, var, *options).pack(pady=5)

# Convert button
tk.Button(root, text="Convert", command=convert).pack(pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()