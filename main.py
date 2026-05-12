import os
from prompt_builder import get_user_input
from formatter import format_prompt

FOLDER_NAME = "AI Ecosystem"

def create_folder():
    if not os.path.exists(FOLDER_NAME):
        os.makedirs(FOLDER_NAME)

def save_prompt(title, content):
    create_folder()

    file_path = os.path.join(FOLDER_NAME, title + ".txt")

    with open(file_path, "w") as file:
        file.write(content)

    print("Prompt saved successfully.")

def load_prompt(title):
    file_path = os.path.join(FOLDER_NAME, title + ".txt")

    if not os.path.exists(file_path):
        print("Prompt not found.")
        return None

    with open(file_path, "r") as file:
        return file.read()

def list_prompts():
    create_folder()

    files = os.listdir(FOLDER_NAME)

    if len(files) == 0:
        print("No saved prompts found.")
        return

    print("\nSaved Prompts:")
    for file in files:
        print("-", file.replace(".txt", ""))
        
def main():

    current_prompt = ""

    while True:
        print("\n========================")
        print(" SIMPLE PROMPT FORMATTER ")
        print("========================")
        print("1. Create new prompt")
        print("2. Load existing prompt")
        print("3. Edit prompt")
        print("4. Export prompt")
        print("5. View current prompt")
        print("6. Quit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            data = get_user_input()
            current_prompt = format_prompt(data)

            print("\nFormatted Prompt:\n")
            print(current_prompt)

        elif choice == "2":
            list_prompts()
            title = input("Enter prompt title to load: ").strip()

            loaded = load_prompt(title)

            if loaded:
                current_prompt = loaded
                print("\nLoaded Prompt:\n")
                print(current_prompt)

        elif choice == "3":
            print("\nRe-enter prompt details:")
            data = get_user_input()
            current_prompt = format_prompt(data)

            print("\nUpdated Prompt:\n")
            print(current_prompt)

        elif choice == "4":
            if current_prompt == "":
                print("No prompt available.")
            else:
                title = input("Enter file name to save: ").strip()

                while title == "":
                    print("Title cannot be empty.")
                    title = input("Enter file name to save: ").strip()

                save_prompt(title, current_prompt)

        elif choice == "5":
            if current_prompt == "":
                print("No current prompt.")
            else:
                print("\nCurrent Prompt:\n")
                print(current_prompt)

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Enter 1 to 6.")
if __name__ == "__main__":
    main()
