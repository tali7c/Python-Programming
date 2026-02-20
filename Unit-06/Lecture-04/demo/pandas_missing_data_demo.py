from pathlib import Path

import pandas as pd


def main() -> None:
    lecture_root = Path(__file__).resolve().parent.parent
    data_path = lecture_root / "data" / "student_scores.csv"

    df = pd.read_csv(data_path)
    print("Original DataFrame:")
    print(df)

    print("\nMissing values per column:")
    print(df.isna().sum())

    # Fill missing city with a placeholder
    df["city"] = df["city"].fillna("Unknown")

    # Fill missing marks with mean of available marks
    mean_marks = df["marks"].mean()
    df["marks"] = df["marks"].fillna(mean_marks)

    print("\nAfter filling missing values:")
    print(df)

    print("\nAverage marks by city:")
    print(df.groupby("city")["marks"].mean())

    # Merge example: map city -> state
    city_state = pd.DataFrame(
        {
            "city": ["Dehradun", "Delhi", "Unknown"],
            "state": ["Uttarakhand", "Delhi", "NA"],
        }
    )
    merged = pd.merge(df, city_state, on="city", how="left")
    print("\nAfter merge (added state):")
    print(merged)

    out_path = lecture_root / "data" / "cleaned_student_scores.csv"
    merged.to_csv(out_path, index=False)
    print("\nSaved cleaned CSV to:", out_path)


if __name__ == "__main__":
    main()

