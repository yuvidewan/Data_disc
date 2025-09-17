def main():
    print("🔎 Open Data Discovery Engine")
    print("Type 'exit' to quit.")

    while True:
        query = input("\nEnter your query: ")
        if query.lower() == "exit":
            print("Goodbye! 👋")
            break
        else:
            print(f"Searching for: {query}")


if __name__ == "__main__":
    main()
