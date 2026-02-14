import numpy as np


def main() -> None:
    print("NumPy Functions Demo\n")

    m = np.random.randint(1, 100, size=(3, 3))
    print("Random 3x3 matrix:\n", m)
    print("Row sums:", m.sum(axis=1))
    print("Col sums:", m.sum(axis=0))
    print("Mean:", round(float(m.mean()), 3))
    print("Std:", round(float(m.std()), 3))
    print()

    a = np.arange(1, 10)
    r = a.reshape((3, 3))
    print("Reshape 1..9 to 3x3:\n", r)
    print()

    arr = np.array([10, 6, 8, 90, 12, 56])
    print("Array:", arr)
    print("Sorted:", np.sort(arr))
    print("Argmax:", int(np.argmax(arr)), "Max:", int(arr[np.argmax(arr)]))

    uniq = np.unique(arr)
    uniq.sort()
    print("Second max:", int(uniq[-2]))
    print()

    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])
    print("Dot product x.y =", int(x.dot(y)))

    M = np.arange(1, 10).reshape((3, 3))
    print("\nMatrix multiplication (M @ M):\n", M @ M)


if __name__ == "__main__":
    main()

