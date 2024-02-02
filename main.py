import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def add_to_do(to_do_text):
    to_do_text = text_entry.get()
    date = datetime.today().strftime('%Y-%m-%d')

    with open("to_dos.txt", "a") as file:
        if to_do_text:
            file.write(f"{date}: {to_do_text}: 0: active: 0\n")
            text_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "There is no to-do to be saved.")
    display_to_dos()

def display_to_dos():
    for widget in manager_frame.winfo_children():
        widget.destroy()
    with open("to_dos.txt", "r") as file:
        lines = file.readlines()
        sorted_lines = sorted(lines, key=lambda x: int(x.split(": ")[2]), reverse=True)
    i = 0
    tk.Label(manager_frame, text="To-Do").grid(row=i, column=0)
    tk.Label(manager_frame, text="Importance").grid(row=i, column=1, columnspan=3)
    tk.Label(manager_frame, text="Finish").grid(row=i, column=4, columnspan=2)
    for line in sorted_lines:
        i += 1
        line_list = [x.strip() for x in line.split(':')]
        if line_list[3] == "active":
            tk.Label(manager_frame, text=line_list[1]).grid(row=i, column=0)
            tk.Label(manager_frame, text=line_list[2]).grid(row=i, column=1)
            tk.Button(manager_frame, text="+", command= lambda i=i, sign=1: update_importance(i, sign)).grid(row=i, column=2) 
            tk.Button(manager_frame, text="-", command= lambda i=i, sign=-1: update_importance(i, sign)).grid(row=i, column=3)
            tk.Button(manager_frame, text="done", command= lambda i=i: done_to_do(i)).grid(row=i, column=4)
            tk.Button(manager_frame, text="delete", command= lambda i=i: delete_to_do(i)).grid(row=i, column=5)

def update(index, importance, state):
    with open("to_dos.txt", "r") as file:
        lines = file.readlines()
        sorted_lines = sorted(lines, key=lambda x: int(x.split(": ")[2]), reverse=True)
    line_list = [x.strip() for x in sorted_lines[index - 1].split(':')]
    if (importance == 1 or importance == -1):
        new_importance = int(line_list[2]) + importance
        sorted_lines[index - 1] = f"{line_list[0]}: {line_list[1]}: {new_importance}: {line_list[3]}: {line_list[4]}\n"
    elif state == "done":
        new_date = datetime.today().strftime('%Y-%m-%d')
        sorted_lines[index - 1] = f"{line_list[0]}: {line_list[1]}: -999: done: {new_date}\n"
    elif state == "delete":
        new_date = datetime.today().strftime('%Y-%m-%d')
        sorted_lines[index - 1] = f"{line_list[0]}: {line_list[1]}: -999: deleted: {new_date}\n"
    with open("to_dos.txt", "w") as file:
        file.writelines(sorted_lines)

def update_importance(index, change):
    update(index=index, importance=change, state=0)
    display_to_dos()

def delete_to_do(index):
    update(index=index, importance=0, state="delete")
    display_to_dos()

def done_to_do(index):
    update(index=index, importance=0, state="done")
    display_to_dos()

# Main window and it's properties
main_window = tk.Tk()
main_window.title("To-do Manager")

add_frame = tk.Frame(main_window)
add_frame.pack(pady=10)
manager_frame = tk.Frame(main_window)
manager_frame.pack(pady=10)

tk.Label(add_frame, text="To-do").grid(row=0, column=0)
text_entry = tk.Entry(add_frame, width=30)
text_entry.grid(row=1, column=0)
text_entry.bind('<Return>', add_to_do)
tk.Button(add_frame, text="Add", command=lambda: add_to_do(text_entry.get())).grid(row=1, column=2)

display_to_dos()

main_window.mainloop()
