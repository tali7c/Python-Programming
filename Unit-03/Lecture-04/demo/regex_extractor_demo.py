import re


EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
PHONE_10_DIGIT_PATTERN = r"\b\d{10}\b"


def main() -> None:
    print("Regex Extractor Demo\n")

    sample_text = """
    Contact us:
      support@upes.ac.in
      admissions@upes.ac.in
    Call: 9876543210, 9123456789
    Extra spaces     should   be   cleaned.
    """

    emails = re.findall(EMAIL_PATTERN, sample_text)
    phones = re.findall(PHONE_10_DIGIT_PATTERN, sample_text)
    cleaned = re.sub(r"\s+", " ", sample_text).strip()

    print("Sample text (cleaned to one line):")
    print(cleaned)
    print()

    print("Extracted emails:", emails)
    print("Extracted phones:", phones)
    print()

    user_phone = input("Enter a 10-digit phone number to validate: ").strip()
    if re.fullmatch(r"\d{10}", user_phone):
        print("Valid phone number format.")
    else:
        print("Invalid phone number format.")


if __name__ == "__main__":
    main()

