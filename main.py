from datetime import datetime
import tkinter as tk
from tkinter import Checkbutton, IntVar, messagebox

def add_action():
    action_text = entry.get()

    if action_text:
        var = IntVar()
        action_checkbox = Checkbutton(action_frame, text=action_text, variable=var)
        action_checkbox.pack(anchor=tk.W)
        actions_checkboxes.append((var, action_text))
        entry.delete(0, tk.END)

def add_habit():
    habit_text = habit_entry.get()
    with open("habits.txt", "a") as file:
        file.write(f"{habit_text}\n")
    habit_entry.delete(0, tk.END)
    var = IntVar()
    action_checkbox = Checkbutton(action_frame, text=habit_text, variable=var)
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

def save_day():
    day_date = datetime.today().strftime('%Y-%m-%d')
    try:
        with open("daily_activities.txt", "a") as file:
            for var, text in actions_checkboxes:
                file.write(f"{day_date}: {text}: {var.get()}\n")
        messagebox.showinfo("Day Saved", "Data saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def read_habits_from_file():
    try:
        with open("habits.txt", "r") as file:
            habits = [line.strip() for line in file.readlines()]
        return habits
    except FileNotFoundError:
        return []

main_window = tk.Tk()
main_window.title("Action List")

entry = tk.Entry(main_window, width=30)
entry.pack(pady=10)

add_action_button = tk.Button(main_window, text="Add Action", command=add_action)
add_action_button.pack()
save_day_button = tk.Button(main_window, text="Save Day", command=save_day)
save_day_button.pack()

action_frame = tk.Frame(main_window)
action_frame.pack(pady=10)

actions_checkboxes = []
habits = read_habits_from_file()
for habit in habits:
    var = IntVar()
    habit_checkbox = Checkbutton(action_frame, text=habit, variable=var)
    habit_checkbox.pack(anchor=tk.W)
    actions_checkboxes.append((var, habit))

open_manager_button = tk.Button(main_window, text="Open Action Manager", command=open_manager)
open_manager_button.pack()

main_window.mainloop()
