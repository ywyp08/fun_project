from datetime import datetime
from tkinter import messagebox

def save_day():
    day_date = datetime.today().strftime('%Y-%m-%d')
    try:
        with open("daily_activities.txt", "a") as file:
            for var, text in actions:
                file.write(f"{day_date}: {text}: {var.get()}\n")
        messagebox.showinfo("Day Saved", "Data saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def read_values_from_file(file_name):
    try:
        with open(file_name, "r") as file:
            habits = [line.strip() for line in file.readlines()]
        return habits
    except FileNotFoundError:
        return []