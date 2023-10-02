import tkinter as tk
from tkinter import messagebox

def new_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
    except IndexError:
        pass

def clear_tasks():
    task_list.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")
entry = tk.Entry(root, width=90)
entry.pack(pady=10)
new_button = tk.Button(root, text="Add Task", width=30, command=new_task)
new_button.pack()
remove_button = tk.Button(root, text="Remove Task", width=30, command=remove_task)
remove_button.pack()
task_list = tk.Listbox(root, height=30, width=50)
task_list.pack()
clear_button = tk.Button(root, text="Clear All Tasks", width=30, command=clear_tasks)
clear_button.pack()
root.mainloop()
