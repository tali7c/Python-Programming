from pathlib import Path


def main() -> None:
    lecture_root = Path(__file__).resolve().parent.parent
    print("Lecture root:", lecture_root)
    print()

    print("Top-level items:")
    for p in sorted(lecture_root.iterdir(), key=lambda x: x.name.lower()):
        kind = "DIR " if p.is_dir() else "FILE"
        print(f"- {kind} {p.name}")

    print("\nPython files under demo/:")
    for p in sorted((lecture_root / "demo").rglob("*.py")):
        rel = p.relative_to(lecture_root)
        print("-", rel.as_posix())

    print("\nLaTeX sources under latex/:")
    for p in sorted((lecture_root / "latex").glob("*.tex")):
        rel = p.relative_to(lecture_root)
        print("-", rel.as_posix())


if __name__ == "__main__":
    main()

