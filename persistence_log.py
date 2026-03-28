# team daily status system

import os

file_name = "database.txt"

# -----------------------------
# save blocker (append)
# -----------------------------
def save_blocker():
    blocker = input("Enter your Daily Blocker: ")

    with open(file_name, "a") as file:
        file.write(blocker + "\n")

    print("Blocker saved\n")


# -----------------------------
# show blockers (read)
# -----------------------------
def show_blockers():

    if os.path.exists(file_name):

        with open(file_name, "r") as file:
            lines = file.readlines()

        if len(lines) == 0:
            print("No blockers saved\n")
        else:
            print("\n--- BLOCKERS LIST ---")

            counter = 1
            for line in lines:
                print(counter, "-", line.strip())
                counter += 1

            print()

    else:
        print("File does not exist, please save a blocker first\n")


# -----------------------------
# delete file (overwrite)
# -----------------------------
def delete_data():

    if os.path.exists(file_name):

        option = input("⚠️ This will delete everything. Are you sure? (yes/no): ")

        if option == "yes":
            with open(file_name, "w") as file:
                file.write("")
            print("Data deleted\n")
        else:
            print("Operation cancelled\n")

    else:
        print("No file to delete\n")


# -----------------------------
# main menu
# -----------------------------
option = ""

while option != "4":

    print("----- TEAM DAILY STATUS -----")
    print("1. Save blocker")
    print("2. Show blockers")
    print("3. Delete data")
    print("4. Exit")

    option = input("Choose an option: ")

    if option == "1":
        save_blocker()

    elif option == "2":
        show_blockers()

    elif option == "3":
        delete_data()

    elif option == "4":
        print("Exiting system...")

    else:
        print("Invalid option\n")


# -----------------------------
# ENGLISH PRACTICE
# -----------------------------

# Protocol Selection (3-C Rule)
# 1. I will reach out via Slack because the issue is urgent and blocks the workflow.
# 2. I will send an email if the problem needs formal documentation.
# 3. I will create a Jira ticket to track the issue and assign responsibility.
