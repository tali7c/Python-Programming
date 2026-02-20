from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    lecture_root = Path(__file__).resolve().parent.parent
    images_dir = lecture_root / "images"
    images_dir.mkdir(exist_ok=True)

    fig, ax = plt.subplots(2, 2, figsize=(9, 6))

    # Line plot
    x = np.arange(1, 6)
    y = np.array([2, 3, 5, 4, 7])
    ax[0, 0].plot(x, y, marker="o")
    ax[0, 0].set_title("Line Plot")
    ax[0, 0].set_xlabel("x")
    ax[0, 0].set_ylabel("y")
    ax[0, 0].grid(True, alpha=0.3)

    # Bar chart
    subjects = ["PDS", "Python", "Chem", "Eng", "Phy"]
    marks = [70, 80, 90, 60, 50]
    ax[0, 1].bar(subjects, marks, color="teal")
    ax[0, 1].set_title("Bar Chart")
    ax[0, 1].set_ylabel("Marks")
    ax[0, 1].tick_params(axis="x", rotation=20)

    # Histogram
    data = np.random.randn(500)
    ax[1, 0].hist(data, bins=20, color="gray", edgecolor="white")
    ax[1, 0].set_title("Histogram")
    ax[1, 0].set_xlabel("Value")
    ax[1, 0].set_ylabel("Frequency")

    # Scatter
    a = np.random.randint(0, 100, size=50)
    b = np.random.randint(0, 100, size=50)
    ax[1, 1].scatter(a, b, color="purple", alpha=0.7)
    ax[1, 1].set_title("Scatter Plot")
    ax[1, 1].set_xlabel("Variable A")
    ax[1, 1].set_ylabel("Variable B")

    fig.suptitle("Matplotlib Plot Types (Subplots)", fontsize=14, fontweight="bold")
    fig.tight_layout()

    out_path = images_dir / "plot_types.png"
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    print("Saved plot to:", out_path)


if __name__ == "__main__":
    main()

