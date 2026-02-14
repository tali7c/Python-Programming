def main() -> None:
    sentence = input("Enter a sentence: ").strip()
    words = sentence.split()
    print("Words:")
    for w in words:
        print(w)


if __name__ == "__main__":
    main()

