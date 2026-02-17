import sqlite3
import tkinter as tk
from pathlib import Path
from tkinter import messagebox


def get_connection(db_path: Path) -> sqlite3.Connection:
    con = sqlite3.connect(db_path)
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            name  TEXT NOT NULL,
            sapid TEXT NOT NULL UNIQUE,
            marks INTEGER
        )
        """
    )
    con.commit()
    return con


def main() -> None:
    lecture_root = Path(__file__).resolve().parent.parent
    data_dir = lecture_root / "data"
    data_dir.mkdir(exist_ok=True)
    db_path = data_dir / "students.db"

    con = get_connection(db_path)

    root = tk.Tk()
    root.title("Student Records (Tkinter + SQLite)")
    root.geometry("720x420")

    name_var = tk.StringVar()
    sapid_var = tk.StringVar()
    marks_var = tk.StringVar()

    form = tk.LabelFrame(root, text="Add Student")
    form.pack(fill="x", padx=12, pady=10)

    tk.Label(form, text="Name:").grid(row=0, column=0, sticky="w", padx=6, pady=6)
    tk.Entry(form, textvariable=name_var, width=30).grid(row=0, column=1, sticky="w", padx=6, pady=6)

    tk.Label(form, text="SAP ID:").grid(row=0, column=2, sticky="w", padx=6, pady=6)
    tk.Entry(form, textvariable=sapid_var, width=20).grid(row=0, column=3, sticky="w", padx=6, pady=6)

    tk.Label(form, text="Marks (0-100):").grid(row=1, column=0, sticky="w", padx=6, pady=6)
    tk.Entry(form, textvariable=marks_var, width=10).grid(row=1, column=1, sticky="w", padx=6, pady=6)

    list_frame = tk.LabelFrame(root, text="All Students")
    list_frame.pack(fill="both", expand=True, padx=12, pady=10)

    listbox = tk.Listbox(list_frame, height=10, width=100)
    listbox.pack(fill="both", expand=True, padx=6, pady=6)

    def refresh() -> None:
        listbox.delete(0, "end")
        cur = con.cursor()
        cur.execute("SELECT id, name, sapid, marks FROM students ORDER BY id DESC")
        for row in cur.fetchall():
            listbox.insert("end", f"id={row[0]} | name={row[1]} | sapid={row[2]} | marks={row[3]}")

    def add_student() -> None:
        name = name_var.get().strip()
        sapid = sapid_var.get().strip()
        marks_text = marks_var.get().strip()

        if not name:
            messagebox.showwarning("Validation", "Name is required.")
            return
        if not sapid:
            messagebox.showwarning("Validation", "SAP ID is required.")
            return

        marks = None
        if marks_text:
            if not marks_text.isdigit():
                messagebox.showwarning("Validation", "Marks must be an integer (0-100).")
                return
            marks_val = int(marks_text)
            if not (0 <= marks_val <= 100):
                messagebox.showwarning("Validation", "Marks must be between 0 and 100.")
                return
            marks = marks_val

        try:
            con.execute("INSERT INTO students(name, sapid, marks) VALUES (?, ?, ?)", (name, sapid, marks))
            con.commit()
        except sqlite3.IntegrityError as e:
            messagebox.showerror("DB Error", f"Could not insert record:\n{e}")
            return

        name_var.set("")
        sapid_var.set("")
        marks_var.set("")
        refresh()
        messagebox.showinfo("Saved", "Student saved.")

    btns = tk.Frame(root)
    btns.pack(pady=6)
    tk.Button(btns, text="Add", command=add_student).pack(side="left", padx=6)
    tk.Button(btns, text="Refresh", command=refresh).pack(side="left", padx=6)
    tk.Button(btns, text="Quit", command=root.destroy).pack(side="left", padx=6)

    refresh()

    def on_close() -> None:
        try:
            con.close()
        finally:
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()


if __name__ == "__main__":
    main()

