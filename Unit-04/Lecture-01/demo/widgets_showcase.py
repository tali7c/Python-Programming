import tkinter as tk
from tkinter import ttk


def main() -> None:
    root = tk.Tk()
    root.title("Tkinter Widgets Showcase")
    root.geometry("640x420")

    name_var = tk.StringVar()
    agree_var = tk.IntVar(value=0)
    gender_var = tk.StringVar(value="Male")
    dept_var = tk.StringVar(value="CSE")

    header = tk.Label(root, text="Widgets Showcase", font=("Segoe UI", 14, "bold"))
    header.pack(pady=8)

    form = tk.Frame(root)
    form.pack(fill="x", padx=12, pady=6)

    tk.Label(form, text="Name:").grid(row=0, column=0, sticky="w")
    tk.Entry(form, textvariable=name_var, width=30).grid(row=0, column=1, sticky="w", padx=6)

    tk.Checkbutton(form, text="I agree", variable=agree_var).grid(row=1, column=1, sticky="w", padx=6, pady=4)

    gender_frame = tk.LabelFrame(form, text="Gender")
    gender_frame.grid(row=2, column=1, sticky="w", padx=6, pady=4)
    tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").pack(side="left", padx=6)
    tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").pack(side="left", padx=6)

    tk.Label(form, text="Department:").grid(row=3, column=0, sticky="w")
    dept = ttk.Combobox(form, textvariable=dept_var, values=["CSE", "AI&ML", "Cyber", "Data"], width=27, state="readonly")
    dept.grid(row=3, column=1, sticky="w", padx=6, pady=4)

    out = tk.Text(root, height=10, width=80)
    out.pack(padx=12, pady=8, fill="both", expand=True)

    def log(msg: str) -> None:
        out.insert("end", msg + "\n")
        out.see("end")

    def show_values() -> None:
        log(f"Name={name_var.get()!r}, Agree={bool(agree_var.get())}, Gender={gender_var.get()}, Dept={dept_var.get()}")

    btns = tk.Frame(root)
    btns.pack(pady=6)
    tk.Button(btns, text="Show Values", command=show_values).pack(side="left", padx=6)
    tk.Button(btns, text="Clear", command=lambda: out.delete("1.0", "end")).pack(side="left", padx=6)
    tk.Button(btns, text="Quit", command=root.destroy).pack(side="left", padx=6)

    log("Try entering values and click 'Show Values'.")
    root.mainloop()


if __name__ == "__main__":
    main()

