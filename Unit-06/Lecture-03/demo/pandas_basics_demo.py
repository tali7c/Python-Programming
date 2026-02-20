import pandas as pd


def main() -> None:
    print("Pandas Basics Demo\n")

    df = pd.DataFrame(
        {
            "name": ["Asha", "Bilal", "Charu", "Deep", "Esha"],
            "marks": [88, 76, 91, 45, 67],
        }
    )

    print("DataFrame:")
    print(df)

    print("\nHead(3):")
    print(df.head(3))

    print("\nTail(2):")
    print(df.tail(2))

    df["cgpa"] = df["marks"] / 10
    df["passed"] = df["marks"] >= 50

    print("\nAfter adding cgpa and passed columns:")
    print(df)

    print("\nOnly passed students:")
    print(df[df["passed"]])


if __name__ == "__main__":
    main()

