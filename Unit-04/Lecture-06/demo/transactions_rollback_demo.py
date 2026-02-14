import sqlite3
from pathlib import Path


def main() -> None:
    lecture_root = Path(__file__).resolve().parent.parent
    data_dir = lecture_root / "data"
    data_dir.mkdir(exist_ok=True)
    db_path = data_dir / "transactions_demo.db"

    con = sqlite3.connect(db_path)
    con.execute("DROP TABLE IF EXISTS students")
    con.execute(
        """
        CREATE TABLE students (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            sapid TEXT NOT NULL UNIQUE,
            name  TEXT NOT NULL
        )
        """
    )
    con.commit()

    print("DB:", db_path)

    try:
        print("\nBegin transaction: inserting 2 rows (second will fail)...")
        con.execute("INSERT INTO students(sapid, name) VALUES (?, ?)", ("5001", "Asha"))
        # Duplicate sapid -> UNIQUE constraint failure
        con.execute("INSERT INTO students(sapid, name) VALUES (?, ?)", ("5001", "Bilal"))
        con.commit()
        print("Commit succeeded (unexpected).")
    except sqlite3.IntegrityError as e:
        print("IntegrityError occurred:", e)
        print("Rolling back...")
        con.rollback()

    print("\nRows after transaction attempt:")
    cur = con.cursor()
    cur.execute("SELECT id, sapid, name FROM students ORDER BY id")
    rows = cur.fetchall()
    for r in rows:
        print(r)
    if not rows:
        print("(no rows) rollback worked: no partial insert remained")

    con.close()


if __name__ == "__main__":
    main()

