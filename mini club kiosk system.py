def get_profile():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    member_input = input("Are you a member? (yes/no): ").strip().lower()
    member = (member_input == "yes")
    return name, age, member


def check_pin(expected="1234"):
    unlocked = False
    for attempt in range(3):
        guess = input("Enter 4-digit PIN: ")
        if guess == expected:
            print("Access granted.")
            unlocked = True
            break
        else:
            print("Incorrect PIN.")
    return unlocked


def view_profile(name, age, member):
    print("\n--- PROFILE ---")
    print("Name:", name)
    print("Age:", age)
    print("Member:", member)


def enter_class_grades():
    print("\n--- CLASS GRADEBOOK ---")
    num_students = int(input("How many students? "))
    passed = 0
    failed = 0

    for i in range(num_students):
        student_name = input("\nEnter student name: ")
        marks = -1
        while marks < 0 or marks > 100:
            marks = int(input(f"Enter marks for {student_name} (0-100): "))

        if marks >= 70:
            result = "Distinction"
            passed += 1
        elif marks >= 50:
            result = "Pass"
            passed += 1
        else:
            result = "Fail"
            failed += 1

        print(f"{student_name}: {marks} --- {result}")

    print("\n--- CLASS REPORT ---")
    print("Total Passed:", passed)
    print("Total Failed:", failed)


def main_menu(name, age, member):
    while True:
        print("\n--- CLUB KIOSK ---")
        print("1) View Profile")
        print("2) Enter Class Grades")
        print("3) Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            view_profile(name, age, member)
        elif choice == "2":
            enter_class_grades()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


def run():
    name, age, member = get_profile()
    if not check_pin("1234"):
        print("Too many attempts. Exiting.")
        return
    main_menu(name, age, member)



if __name__ == "__main__":
    run()
