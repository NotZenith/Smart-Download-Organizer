import os
import shutil

# File type categories
FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Code": [".py", ".js", ".java", ".cpp", ".html", ".css"]
}

def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return "Others"


def organize_folder(path):
    if not os.path.exists(path):
        print("Folder does not exist.")
        return

    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)

            category = get_category(ext)
            category_path = os.path.join(path, category)

            # Create folder if not exists
            os.makedirs(category_path, exist_ok=True)

            # Move file
            try:
                shutil.move(file_path, os.path.join(category_path, file))
                print(f"Moved: {file} → {category}")
            except Exception as e:
                print(f"Failed to move {file}: {e}")


if __name__ == "__main__":
    downloads_path = input("Enter folder path to organize: ")
    organize_folder(downloads_path)
