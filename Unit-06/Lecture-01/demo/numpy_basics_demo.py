import numpy as np


def main() -> None:
    print("NumPy Basics Demo\n")

    a = np.array([1, 2, 3])
    print("a =", a, "dtype=", a.dtype)
    print("a * 2 =", a * 2)
    print("a + 10 =", a + 10)
    print()

    m = np.array([[1, 2, 3], [4, 5, 6]])
    print("m =\n", m)
    print("shape:", m.shape, "ndim:", m.ndim, "size:", m.size)
    print()

    z = np.zeros((2, 3))
    o = np.ones((2, 3))
    r = np.arange(0, 10, 2)
    lin = np.linspace(0, 1, 5)

    print("zeros:\n", z)
    print("ones:\n", o)
    print("arange:", r)
    print("linspace:", lin)
    print()

    # Broadcasting: add vector to each row
    v = np.array([10, 20, 30])
    print("Broadcasting example (m + v):\n", m + v)


if __name__ == "__main__":
    main()

