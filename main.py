import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def add_to_do():
    to_do_text = to_do_text_entry.get()
    to_do_importance = to_do_importance_entry.get()
    date = datetime.today().strftime('%Y-%m-%d')

    with open("to_dos.txt", "a") as file:
        if to_do_text:
            file.write(f"{date}: {to_do_text}: {to_do_importance}: active\n")
            to_do_text_entry.delete(0, tk.END)
            to_do_importance_entry.delete(0, tk.END)
            messagebox.showinfo("Saved", "Data saved successfully!")
        else:
            messagebox.showerror("Error", "There is no to-do to be saved.")
    display_to_dos()  # Update the to-do list display

def display_to_dos():
    for widget in manager_frame.winfo_children():
        widget.destroy()

    tk.Label(manager_frame, text="To-Do").grid(row=0, column=0)
    tk.Label(manager_frame, text="Importance").grid(row=0, column=1, columnspan=3)
    tk.Label(manager_frame, text="Finish").grid(row=0, column=4, columnspan=2)

    with open("to_dos.txt", "r") as file:
        lines = file.readlines()
        sorted_lines = sorted(lines, key=lambda x: int(x.split(": ")[2]), reverse=True)
        for i, line in enumerate(sorted_lines, start=1):
            date, to_do_text, to_do_importance, status = line.strip().split(": ")
            tk.Label(manager_frame, text=to_do_text).grid(row=i, column=0)
            tk.Label(manager_frame, text=to_do_importance).grid(row=i, column=1)
            tk.Button(manager_frame, text="+", command= lambda i=i: importance_plus(i)).grid(row=i, column=2) 
            tk.Button(manager_frame, text="-", command= lambda i=i: importance_minus(i)).grid(row=i, column=3)
            tk.Button(manager_frame, text="done").grid(row=i, column=4)
            tk.Button(manager_frame, text="delete").grid(row=i, column=5)

def importance_plus(index):
    update_importance(index, 1)

def importance_minus(index):
    update_importance(index, -1)

def update_importance(index, change):
    # Read existing to-dos
    with open("to_dos.txt", "r") as file:
        lines = file.readlines()

    # Update the importance of the specific to-do
    date, to_do_text, to_do_importance, state = lines[index - 1].strip().split(": ")
    new_importance = max(int(to_do_importance) + change, 0)
    lines[index - 1] = f"{date}: {to_do_text}: {new_importance}: {state}\n"

    # Write the updated to-dos back to the file
    with open("to_dos.txt", "w") as file:
        file.writelines(lines)

    # Update the display
    display_to_dos()

main_window = tk.Tk()
main_window.title("To-do Manager")

add_frame = tk.Frame(main_window)
add_frame.pack(pady=10)
manager_frame = tk.Frame(main_window)
manager_frame.pack(pady=10)

# filling the add_frame
tk.Label(add_frame, text="To-do").grid(row=0, column=0)
tk.Label(add_frame, text="Importance").grid(row=0, column=1)
to_do_text_entry = tk.Entry(add_frame, width=30)
to_do_text_entry.grid(row=1, column=0)
to_do_importance_entry = tk.Entry(add_frame, width=10)
to_do_importance_entry.grid(row=1, column=1)
tk.Button(add_frame, text="Add", command=add_to_do).grid(row=1, column=3)

display_to_dos()

main_window.mainloop()
