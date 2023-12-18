class BugTracker:
    def __init__(self):
        self.bugs = []

    def log_bug(self, error, assigned_to):
        bug = {"error": error, "assigned_to": assigned_to, "status": "Open"}
        self.bugs.append(bug)
        return f"Bug logged: {error} (Assigned to: {assigned_to})"

    def display_bugs(self):
        if not self.bugs:
            return "No bugs to display."

        for index, bug in enumerate(self.bugs, start=1):
            print(f"{index}. {bug['error']} (Assigned to: {bug['assigned_to']}, Status: {bug['status']})")

    def prioritize_and_test(self):
        # In a real-world scenario, you might implement logic to prioritize and test bugs.
        return "Bugs prioritized and tested."

    def deploy_fixes(self):
        # In a real-world scenario, you might implement logic to deploy fixes.
        return "Fixes deployed."

    def delete_bug(self, bug_index):
        if 1 <= bug_index <= len(self.bugs):
            del self.bugs[bug_index - 1]
            return f"Bug {bug_index} deleted."
        else:
            return "Invalid bug index."

# Function to get user input
def get_user_input(prompt):
    return input(prompt).strip()

# Example usage with user input
bug_tracker = BugTracker()

while True:
    print("\nCommands:")
    print("1. Log Bug")
    print("2. Display Bugs")
    print("3. Prioritize and Test Bugs")
    print("4. Deploy Fixes")
    print("5. Delete Bug")
    print("6. Exit")

    choice = get_user_input("Enter your choice (1-6): ")

    if choice == "1":
        error = get_user_input("Enter bug description: ")
        assigned_to = get_user_input("Assign to (team member): ")
        print(bug_tracker.log_bug(error, assigned_to))

    elif choice == "2":
        bug_tracker.display_bugs()

    elif choice == "3":
        print(bug_tracker.prioritize_and_test())

    elif choice == "4":
        print(bug_tracker.deploy_fixes())

    elif choice == "5":
        bug_index = int(get_user_input("Enter the index of the bug to delete: "))
        print(bug_tracker.delete_bug(bug_index))

    elif choice == "6":
        print("Exiting the Bug Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
