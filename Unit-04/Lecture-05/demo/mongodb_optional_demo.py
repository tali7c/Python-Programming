def main() -> None:
    print("MongoDB Optional Demo")
    print("This demo requires:")
    print("  1) MongoDB running locally, and")
    print("  2) pymongo installed: pip install pymongo")
    print()

    try:
        from pymongo import MongoClient  # type: ignore
    except Exception as e:
        print("pymongo is not available in this environment.")
        print("Reason:", e)
        return

    client = MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=2000)
    try:
        client.admin.command("ping")
    except Exception as e:
        print("Could not connect to MongoDB (is it running?).")
        print("Reason:", e)
        return

    db = client["college"]
    students = db["students"]

    students.insert_one({"name": "Asha", "sapid": "5001", "marks": 88})
    print("Inserted one document.")

    for doc in students.find({}, {"_id": 0}):
        print(doc)


if __name__ == "__main__":
    main()

