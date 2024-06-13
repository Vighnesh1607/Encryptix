import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("500x500")
        self.tasks = []

        # Frame for Task List
        self.frame = tk.Frame(self.root, bg="lightgrey", bd=5)
        self.frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.frame, width=50, height=10, font=("Arial", 12), bg="white", selectbackground="skyblue")
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar for Listbox
        self.task_scrollbar = tk.Scrollbar(self.frame)
        self.task_scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.task_listbox.config(yscrollcommand=self.task_scrollbar.set)
        self.task_scrollbar.config(command=self.task_listbox.yview)

        # Entry widget for new tasks
        self.task_entry = tk.Entry(self.root, width=50, font=("Arial", 12))
        self.task_entry.pack(pady=10, padx=20)

        # Buttons frame
        self.button_frame = tk.Frame(self.root, bg="lightgrey")
        self.button_frame.pack(pady=10)

        # Add Task Button
        self.add_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task, font=("Arial", 12), bg="lightblue", padx=10, pady=5)
        self.add_button.pack(side=tk.LEFT, padx=5)

        # Update Task Button
        self.update_button = tk.Button(self.button_frame, text="Update Task", command=self.update_task, font=("Arial", 12), bg="lightgreen", padx=10, pady=5)
        self.update_button.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task")

    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            updated_task = self.task_entry.get()
            if updated_task:
                self.tasks[selected_task_index] = updated_task
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, updated_task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a task")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
