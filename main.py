import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
from tkinter.scrolledtext import ScrolledText

class SimpleIDE:
    def __init__(self, master):
        self.master = master
        self.master.title("SimpleIDE")
        self.master.configure(bg="#333")  # Set background color to dark

        # Create a frame for buttons
        button_frame = tk.Frame(master, bg="#333")
        button_frame.pack(fill=tk.X)

        # Add image buttons for open, save, new, and run actions
        self.new_img = tk.PhotoImage(file="new.png")
        self.open_img = tk.PhotoImage(file="open.png")
        self.save_img = tk.PhotoImage(file="save.png")
        self.run_img = tk.PhotoImage(file="run.png")

        tk.Button(button_frame, image=self.new_img, command=self.new_file, bg="#333", bd=0).pack(side=tk.LEFT)
        tk.Button(button_frame, image=self.open_img, command=self.open_file, bg="#333", bd=0).pack(side=tk.LEFT)
        tk.Button(button_frame, image=self.save_img, command=self.save_file, bg="#333", bd=0).pack(side=tk.LEFT)
        tk.Button(button_frame, image=self.run_img, command=self.run_script, bg="#333", bd=0).pack(side=tk.LEFT)

        # Create text area with line numbers
        self.text_area = ScrolledText(master, undo=True, bg="#444", fg="white")
        self.text_area.pack(fill=tk.BOTH, expand=True)

        # Create output area
        self.output_area = tk.Text(master, height=8, state=tk.DISABLED, bg="#444", fg="white")
        self.output_area.pack(fill=tk.BOTH, expand=True)


    def new_file(self):
        self.text_area.delete("1.0", tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(filetypes=[("Python Files", "*.py")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_area.get("1.0", tk.END)
                file.write(content)

    def run_script(self):
        script = self.text_area.get("1.0", tk.END)
        try:
            result = subprocess.run(["python", "-c", script], capture_output=True, text=True)
            self.output_area.config(state=tk.NORMAL)
            self.output_area.delete("1.0", tk.END)
            self.output_area.insert(tk.END, result.stdout)
            self.output_area.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    app = SimpleIDE(root)
    root.mainloop()

if __name__ == "__main__":
    main()
