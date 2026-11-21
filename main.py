import grooming
import reports


# Displays the menu
def show_menu():
    print("\n===== PAWS & BUBBLES PET GROOMING =====")
    print("1. View customers and pets")
    print("2. Add or update a customer")
    print("3. Schedule an appointment")
    print("4. View appointments")
    print("5. Record a completed service")
    print("6. Sales report")
    print("7. View charts")
    print("8. Save and exit")


# Runs the main menu
def main():
    grooming.load_customers()
    grooming.load_appointments()

    choice = ""

    while choice != "8":
        show_menu()

        choice = input("\nEnter your choice (1-8): ")

        if choice == "1":
            grooming.view_customers()

        elif choice == "2":
            grooming.add_customer()

        elif choice == "3":
            print("Coming soon!")

        elif choice == "4":
            print("Coming soon!")

        elif choice == "5":
            grooming.record_service()

        elif choice == "6":
            reports.sales_report(grooming.appointments)

        elif choice == "7":
            reports.charts(grooming.appointments)

        elif choice == "8":
            grooming.save_customers()
            grooming.save_appointments()
            print("Customer information saved!")
            print("Appointment transactions saved!")
            print("Thank you for using Paws & Bubbles!")

        else:
            print("Invalid choice. Please select an option from 1-8.")


# Start the program.
main()
