import sqlite3
from pathlib import Path


def main() -> None:
    lecture_root = Path(__file__).resolve().parent.parent
    data_dir = lecture_root / "data"
    data_dir.mkdir(exist_ok=True)
    db_path = data_dir / "crud_demo.db"

    con = sqlite3.connect(db_path)
    cur = con.cursor()

    cur.execute(
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

    print("DB:", db_path)

    # CREATE (INSERT)
    sample = [("Asha", "5001", 88), ("Bilal", "5002", 76), ("Charu", "5003", 91)]
    for name, sapid, marks in sample:
        try:
            cur.execute("INSERT INTO students(name, sapid, marks) VALUES (?, ?, ?)", (name, sapid, marks))
        except sqlite3.IntegrityError:
            pass
    con.commit()

    # READ (SELECT)
    print("\nAll students:")
    cur.execute("SELECT id, name, sapid, marks FROM students ORDER BY id")
    for row in cur.fetchall():
        print(row)

    # UPDATE
    print("\nUpdate marks of sapid=5002 to 80")
    cur.execute("UPDATE students SET marks = ? WHERE sapid = ?", (80, "5002"))
    con.commit()

    # DELETE
    print("\nDelete sapid=5001")
    cur.execute("DELETE FROM students WHERE sapid = ?", ("5001",))
    con.commit()

    print("\nFinal table:")
    cur.execute("SELECT id, name, sapid, marks FROM students ORDER BY id")
    for row in cur.fetchall():
        print(row)

    con.close()


if __name__ == "__main__":
    main()

