import tkinter as tk

root = tk.Tk()
root.title("PoC Window")
root.geometry("300x150")

label = tk.Label(root, text="PoC", font=("Arial", 40))
label.pack(expand=True)

root.mainloop()