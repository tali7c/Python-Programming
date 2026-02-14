def is_leap_year(year: int) -> bool:
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def days_in_month(year: int, month: int) -> int:
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month in (4, 6, 9, 11):
        return 30
    if month == 2:
        return 29 if is_leap_year(year) else 28
    return 0  # invalid


def main() -> None:
    day = int(input("Enter day: "))
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))

    dim = days_in_month(year, month)
    if dim == 0:
        print("Invalid month.")
        return
    if day < 1 or day > dim:
        print("Invalid day for the given month/year.")
        return

    # Compute next date
    day += 1
    if day > dim:
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1

    print("Next date:")
    print("day =", day, "month =", month, "year =", year)


if __name__ == "__main__":
    main()

