import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("450x450")
        self.root.configure(bg="#2C3E50")

        # Task List
        self.tasks = []

        # GUI Elements
        self.task_entry = tk.Entry(root, width=35, font=("Arial", 12))
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", width=12, bg="#1ABC9C", fg="white", font=("Arial", 10), command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, height=15, width=45, selectmode=tk.SINGLE, bg="#34495E", fg="white", font=("Arial", 12))
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.update_button = tk.Button(root, text="Update Task", width=15, bg="#3498DB", fg="white", font=("Arial", 10), command=self.update_task)
        self.update_button.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

        self.delete_button = tk.Button(root, text="Delete Task", width=15, bg="#E74C3C", fg="white", font=("Arial", 10), command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=5, sticky=tk.E)

        self.mark_completed_button = tk.Button(root, text="Mark as Completed", width=25, bg="#9B59B6", fg="white", font=("Arial", 10), command=self.mark_completed)
        self.mark_completed_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.view_tasks_button = tk.Button(root, text="View Tasks", width=25, bg="#F39C12", fg="white", font=("Arial", 10), command=self.view_tasks)
        self.view_tasks_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_to_update = selected_task_index[0]
            new_task = simpledialog.askstring("Update Task", "Enter the new task:")
            if new_task:
                self.tasks[task_to_update]["task"] = new_task
                self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_to_remove = selected_task_index[0]
            self.tasks.pop(task_to_remove)
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def mark_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_to_mark = selected_task_index[0]
            self.tasks[task_to_mark]["completed"] = True
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to mark as completed.")

    def view_tasks(self):
        self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = " (Completed)" if task["completed"] else ""
            self.task_listbox.insert(tk.END, task["task"] + status)

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
