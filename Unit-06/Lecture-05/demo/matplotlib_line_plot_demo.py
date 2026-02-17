from pathlib import Path

import matplotlib.pyplot as plt


def main() -> None:
    lecture_root = Path(__file__).resolve().parent.parent
    images_dir = lecture_root / "images"
    images_dir.mkdir(exist_ok=True)

    x = [1, 2, 3, 4, 5]
    y = [2, 5, 4, 7, 9]

    plt.figure(figsize=(6, 4))
    plt.plot(x, y, marker="o", linestyle="--", color="teal", label="sample trend")
    plt.title("Sample Line Plot")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, alpha=0.3)
    plt.legend()

    out_path = images_dir / "line_plot.png"
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    print("Saved plot to:", out_path)


if __name__ == "__main__":
    main()

