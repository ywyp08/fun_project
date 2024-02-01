import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def add_to_do():
    to_do_text = to_do_text_entry.get()
    to_do_importance = to_do_importance_entry.get()
    date = datetime.today().strftime('%Y-%m-%d')

    with open("to_dos.txt", "a") as file:
        if to_do_text:
            file.write(f"{date}: {to_do_text}: {to_do_importance}\n")
            to_do_text_entry.delete(0, tk.END)
            to_do_importance_entry.delete(0, tk.END)
            messagebox.showinfo("Saved", "Data saved successfully!")
        else:
            messagebox.showerror("Error", "There is no to-do to be saved.")

main_window = tk.Tk()
main_window.title("To-do Manager")
add_frame = tk.Frame(main_window)
add_frame.pack(pady=10)
manager_frame = tk.Frame(main_window)
manager_frame.pack(pady=10)

tk.Label(add_frame, text="To-do").grid(row=0, column=0)
tk.Label(add_frame, text="Importance").grid(row=0, column=1)

to_do_text_entry = tk.Entry(add_frame, width=30)
to_do_text_entry.grid(row=1, column=0)
to_do_importance_entry = tk.Entry(add_frame, width=10)
to_do_importance_entry.grid(row=1, column=1)

tk.Button(add_frame, text="Add to-do", command=add_to_do).grid(row=1, column=3)

tk.Label(manager_frame, text="To-Dos").grid(row=0, column=0)

main_window.mainloop()
