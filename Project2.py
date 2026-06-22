def get_expense():
    '''
    Get a valid expense amount from the user.
    Returns float or None if user wants to stop.
'''
    while True:
        user_input = input("Enter expense amount (or type 'done'): ").strip().lower()

        if user_input == "done":
            return None

        try:
            expense = float(user_input)

            if expense < 0:
                print("Expense cannot be negative. Try again.")
                continue

            return expense

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    total_spent = 0.0
    expenses_count = 0

    print("\n===== Expense Tracker =====\n")

    while True:
        expense = get_expense()

        if expense is None:
            break

        total_spent += expense
        expenses_count += 1

        print(f"Added: {expense:.2f} | Current Total: {total_spent:.2f}\n")

    print("\n===== Summary =====")
    print(f"Total Expenses Entered: {expenses_count}")
    print(f"Total Spent: {total_spent:.2f}")
    print("====================\n")


if __name__ == "__main__":
    main()