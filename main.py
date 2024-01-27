import tkinter as tk
from tkinter import Checkbutton, IntVar
from data_manipulation import *

def add_action():
    action_text = entry.get()

    if action_text:
        var = IntVar()
        action_checkbox = Checkbutton(frame, text=action_text, variable=var)
        action_checkbox.pack(anchor=tk.W)
        actions.append((var, action_text))
        entry.delete(0, tk.END)

def add_habit():
    habit_text = habit_entry.get()
    with open("habits.txt", "a") as file:
        file.write(f"{habit_text}\n")
    habit_entry.delete(0, tk.END)
    var = IntVar()
    action_checkbox = Checkbutton(frame, text=habit_text, variable=var)
    action_checkbox.pack(anchor=tk.W)

def open_manager():
    global habit_entry
    manager_window = tk.Toplevel(main_window)
    manager_window.title("Action Manager")

    habit_entry_label = tk.Label(manager_window, text="Enter Habit:")
    habit_entry_label.pack()

    habit_entry = tk.Entry(manager_window, width=30)
    habit_entry.pack(pady=10)

    add_habit_button = tk.Button(manager_window, text="Add Habit", command=add_habit)
    add_habit_button.pack()

main_window = tk.Tk()
main_window.title("Action List")

""" entry = tk.Entry(main_window, width=30)
entry.pack(pady=10)

add_action_button = tk.Button(main_window, text="Add Action", command=add_action)
add_action_button.pack()

save_day_button = tk.Button(main_window, text="Save Day", command=save_day)
save_day_button.pack() """

frame = tk.Frame(main_window)
frame.pack(pady=10)

tk.Label(frame, text="Actions").grid(row=0, column=0)
tk.Label(frame, text="Goals").grid(row=0, column=1)

actions = [] 
habits = read_values_from_file("habits.txt")

row = 1
for habit in habits:
    var = IntVar()
    Checkbutton(frame, text=habit, variable=var).grid(row=row, column=0)
    row += 1
    actions.append((var, habit))

open_manager_button = tk.Button(main_window, text="Goal Manager", command=open_manager)
open_manager_button.pack()

main_window.mainloop()
