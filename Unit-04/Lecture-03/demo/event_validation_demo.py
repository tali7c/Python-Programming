import re
import tkinter as tk
from tkinter import messagebox


EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


def main() -> None:
    root = tk.Tk()
    root.title("Event Handling + Validation Demo")
    root.geometry("520x300")

    name_var = tk.StringVar()
    email_var = tk.StringVar()
    age_var = tk.StringVar()
    status_var = tk.StringVar(value="Fill the form.")

    form = tk.LabelFrame(root, text="Registration Form")
    form.pack(fill="x", padx=12, pady=12)

    tk.Label(form, text="Name:").grid(row=0, column=0, sticky="w", padx=6, pady=6)
    name_entry = tk.Entry(form, textvariable=name_var, width=35)
    name_entry.grid(row=0, column=1, sticky="w", padx=6, pady=6)

    tk.Label(form, text="Email:").grid(row=1, column=0, sticky="w", padx=6, pady=6)
    email_entry = tk.Entry(form, textvariable=email_var, width=35)
    email_entry.grid(row=1, column=1, sticky="w", padx=6, pady=6)

    tk.Label(form, text="Age:").grid(row=2, column=0, sticky="w", padx=6, pady=6)
    age_entry = tk.Entry(form, textvariable=age_var, width=10)
    age_entry.grid(row=2, column=1, sticky="w", padx=6, pady=6)

    status = tk.Label(root, textvariable=status_var, fg="blue")
    status.pack(padx=12, pady=6, anchor="w")

    def validate() -> tuple[bool, str]:
        name = name_var.get().strip()
        email = email_var.get().strip()
        age_text = age_var.get().strip()

        if not name:
            return False, "Name is required."
        if not EMAIL_RE.fullmatch(email):
            return False, "Email format is invalid (example: name@example.com)."
        if not age_text.isdigit():
            return False, "Age must be a non-negative integer."
        age = int(age_text)
        if not (0 <= age <= 120):
            return False, "Age must be between 0 and 120."
        return True, "All fields look valid."

    def update_status(event=None) -> None:
        ok, msg = validate()
        status_var.set(msg)
        status.config(fg=("green" if ok else "red"))

    def submit() -> None:
        ok, msg = validate()
        if not ok:
            messagebox.showwarning("Validation", msg)
            return
        messagebox.showinfo("Success", "Registration accepted!")

    # Live validation on typing
    for w in (name_entry, email_entry, age_entry):
        w.bind("<KeyRelease>", update_status)

    btns = tk.Frame(root)
    btns.pack(pady=10)
    tk.Button(btns, text="Submit", command=submit).pack(side="left", padx=6)
    tk.Button(btns, text="Clear", command=lambda: (name_var.set(""), email_var.set(""), age_var.set(""))).pack(
        side="left", padx=6
    )
    tk.Button(btns, text="Quit", command=root.destroy).pack(side="left", padx=6)

    # Shortcut: Ctrl+L clears form
    def clear_shortcut(event=None) -> None:
        name_var.set("")
        email_var.set("")
        age_var.set("")
        status_var.set("Cleared. Fill the form.")
        status.config(fg="blue")

    root.bind("<Control-l>", clear_shortcut)

    name_entry.focus_set()
    root.mainloop()


if __name__ == "__main__":
    main()

