from fetcher import search_kaggle_datasets

def main():
    print("🔎 Open Data Discovery Engine")
    print("Type 'exit' to quit.")

    while True:
        query = input("\nEnter your query: ")
        if query.lower() == "exit":
            print("Goodbye! 👋")
            break
        else:
            search_kaggle_datasets(query)


if __name__ == "__main__":
    main()
