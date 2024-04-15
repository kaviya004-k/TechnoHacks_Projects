import tkinter as tk
from tkinter import *
from tkinter import Scrollbar, Listbox, Entry, Button, Checkbutton, IntVar, messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        self.master.geometry("330x330")
        self.master.resizable(False, False)
        self.master.configure(background = "#32405b")
        
        self.tasks = []
        self.task_statuses = []

        self.heading = Label(self.master, height = 1, width = 12, text = "To-Do List", font = "arial 28 bold", fg = "ivory", bg = "#32405b")
        self.heading.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        self.task_var = tk.StringVar()
        self.task_entry = Entry(self.master, textvariable=self.task_var, width=22, font = "arial 14", bg = "floralwhite")
        self.task_entry.grid(row=1, column=0, padx=10, pady=10, columnspan=3)
        
        self.add_button = Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=1, column=2, padx=0, pady=0)
        
        self.task_listbox = Listbox(self.master, width=27, height=6, selectmode=tk.SINGLE,font = "Ivy 15 bold", fg = "wheat", bg = "#32405b")
        self.task_listbox.grid(row=2, column=0, padx=10, pady=0, columnspan=11)
        
        self.scrollbar = Scrollbar(self.master, orient=tk.VERTICAL, command=self.task_listbox.yview, bg = "peachpuff")
        self.scrollbar.grid(row=2, column=3, sticky='ns')
        
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        
        self.complete_button = Button(self.master, text="Complete", command=self.complete_task)
        self.complete_button.grid(row=3, column=0, padx=10, pady=10)
        
        self.delete_button = Button(self.master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=3, column=1, padx=10, pady=10)
        
        self.status_button = Button(self.master, text="Check Status", command=self.check_status)
        self.status_button.grid(row=3, column=2, padx=10, pady=10)

    def add_task(self):
        task = self.task_var.get()
        if task:
            self.tasks.append(task)
            self.task_statuses.append(IntVar())
            self.task_listbox.insert(tk.END, task)
            self.task_var.set("")
    

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.task_statuses.pop(selected_index[0])
            self.task_listbox.delete(selected_index)
            

    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_statuses[selected_index[0]].set(1)
            self.task_listbox.itemconfig(selected_index, {'fg': 'palegreen'})

    def check_status(self):
        total_tasks = len(self.tasks)
        completed_count = sum(status.get() for status in self.task_statuses)
        message = f"Total Tasks: {total_tasks}\nCompleted Tasks: {completed_count}"
        messagebox.showinfo("Task Status", message)

     
    
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
