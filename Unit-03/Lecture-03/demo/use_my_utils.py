import sys
import time
from pathlib import Path

from my_utils import average, hypotenuse, normalize_spaces, word_count


def main() -> None:
    print("Modules + Packages Demo")

    # sys.argv demo
    if len(sys.argv) >= 2:
        raw = sys.argv[1]
    else:
        raw = "  Hello   UPES   Dehradun  "

    text = normalize_spaces(raw)
    print("\nInput text:", repr(raw))
    print("Normalized:", repr(text))
    print("Word count:", word_count(text))

    # math helpers demo
    a, b = 3.0, 4.0
    print("\nHypotenuse for a=3, b=4:", hypotenuse(a, b))
    print("Average of [10, 20, 30]:", average([10.0, 20.0, 30.0]))

    # time demo
    start = time.time()
    time.sleep(0.2)
    print("\nElapsed time (approx):", round(time.time() - start, 4), "seconds")

    # pathlib demo
    here = Path(__file__).resolve()
    print("\nThis script path:", here)
    print("Parent folder:", here.parent)


if __name__ == "__main__":
    main()

