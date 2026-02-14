def is_leap_year(year: int) -> bool:
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def main() -> None:
    year = int(input("Enter year: "))
    if is_leap_year(year):
        print(year, "is a leap year")
    else:
        print(year, "is NOT a leap year")


if __name__ == "__main__":
    main()

