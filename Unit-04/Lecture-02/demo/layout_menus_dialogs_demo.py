import tkinter as tk
from tkinter import filedialog, messagebox


def main() -> None:
    root = tk.Tk()
    root.title("Layout + Menus + Dialogs Demo")
    root.geometry("520x260")

    # --- Menu bar ---
    menubar = tk.Menu(root)

    file_menu = tk.Menu(menubar, tearoff=0)

    def open_file() -> None:
        path = filedialog.askopenfilename(title="Select a file")
        if path:
            messagebox.showinfo("Selected", f"Selected file:\n{path}")

    file_menu.add_command(label="Open...", command=open_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="File", menu=file_menu)

    help_menu = tk.Menu(menubar, tearoff=0)
    help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Tkinter demo for Unit-04 Lecture-02"))
    menubar.add_cascade(label="Help", menu=help_menu)

    root.config(menu=menubar)

    # --- Layout with frames ---
    form = tk.LabelFrame(root, text="Student Form")
    form.pack(fill="x", padx=12, pady=12)

    name_var = tk.StringVar()
    age_var = tk.StringVar()

    tk.Label(form, text="Name:").grid(row=0, column=0, sticky="w", padx=6, pady=6)
    tk.Entry(form, textvariable=name_var, width=30).grid(row=0, column=1, sticky="w", padx=6, pady=6)

    tk.Label(form, text="Age:").grid(row=1, column=0, sticky="w", padx=6, pady=6)
    tk.Entry(form, textvariable=age_var, width=10).grid(row=1, column=1, sticky="w", padx=6, pady=6)

    btns = tk.Frame(root)
    btns.pack(pady=10)

    def submit() -> None:
        name = name_var.get().strip()
        age_text = age_var.get().strip()
        if not name:
            messagebox.showwarning("Validation", "Name is required.")
            return
        if not age_text.isdigit():
            messagebox.showwarning("Validation", "Age must be a non-negative integer.")
            return
        messagebox.showinfo("Submitted", f"Saved:\nName={name}\nAge={age_text}")

    tk.Button(btns, text="Submit", command=submit).pack(side="left", padx=6)
    tk.Button(btns, text="Clear", command=lambda: (name_var.set(""), age_var.set(""))).pack(side="left", padx=6)
    tk.Button(btns, text="Quit", command=root.destroy).pack(side="left", padx=6)

    root.mainloop()


if __name__ == "__main__":
    main()

