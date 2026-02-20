def main() -> None:
    total_seconds = int(input("Enter seconds (non-negative integer): "))
    if total_seconds < 0:
        print("Seconds must be non-negative.")
        return

    hours = total_seconds // 3600
    rem = total_seconds % 3600
    minutes = rem // 60
    seconds = rem % 60

    print(f"{total_seconds} seconds = {hours} hour(s), {minutes} minute(s), {seconds} second(s)")


if __name__ == "__main__":
    main()

