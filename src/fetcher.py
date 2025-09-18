import subprocess
import zipfile
import os

def show_results(datasets, index):
    curr_dataset_ref = datasets[index-1][0]  # first column = owner/dataset-slug
    print("Downloading:", curr_dataset_ref)

    # Download dataset
    subprocess.run(["kaggle", "datasets", "download", "-d", curr_dataset_ref])

    # Build zip filename
    zip_file = curr_dataset_ref.split("/")[-1] + ".zip"

    # Unzip safely
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall("datasets")

    print("Files extracted:", os.listdir("datasets"))


def search_kaggle_datasets(query, max_results=5):
    try:
        result = subprocess.run(
            ["kaggle", "datasets", "list", "-s", query],
            capture_output=True,
            text=True,
            check=True
        )
        lines = result.stdout.splitlines()

        if len(lines) <= 1:
            print("❌ No datasets found.")
            return

        # Parse lines: each line is a row, first column = dataset ref
        datasets = []
        for line in lines[1:max_results+1]:
            parts = line.split()  # split by whitespace
            if len(parts) > 0:
                datasets.append((parts[0], line))  # (ref, full row)

        print(f"\nTop {len(datasets)} Kaggle results for '{query}':\n")
        for i, ds in enumerate(datasets, start=1):
            print(f"{i}. {ds[1]}")
            print("-" * 50)

        index = int(input("ENTER INDEX TO DOWNLOAD: "))
        show_results(datasets=datasets, index=index)

    except Exception as e:
        print("⚠️ Error searching Kaggle:", e)
