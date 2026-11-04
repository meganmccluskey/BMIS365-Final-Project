# customer names and their pets
customers = {
    101: {"name": "Ryland Grace", "pet": "Rocky",
          "type": "Cat", "breed": "Maine Coon"},

    102: {"name": "Mark Watney", "pet": "Potato",
          "type": "Dog", "breed": "Labrador Retriever"},

    103: {"name": "Spike Spiegel", "pet": "Ein",
          "type": "Dog", "breed": "Corgi"}
}

# Menues
def show_menu():
    print("\n===== PAWS & BUBBLES PET GROOMING =====")
    print("1. View customers and pets")
    print("2. Add or update a customer")
    print("3. Schedule an appointment")
    print("4. View appointments")
    print("5. Record a completed service")
    print("6. Sales report with charts")
    print("7. Run 30-day simulation")
    print("8. Save and exit")


# Customers and Pets
def view_customers():
    print("\n===== CUSTOMER LIST =====")

    for customer_id in customers:
        print("Customer ID:", customer_id)
        print("Customer Name:", customers[customer_id]["name"])
        print("Pet Name:", customers[customer_id]["pet"])
        print("Pet Type:", customers[customer_id]["type"])
        print("Pet Breed:", customers[customer_id]["breed"])


# This adds customers
def add_customer():
    print("\n===== ADD OR UPDATE CUSTOMER =====")

    customer_id = input("Enter customer ID: ")

    valid_id = True

    for number in customer_id:
        if number < "0" or number > "9":
            valid_id = False

    if valid_id == False or customer_id == "":
        print("Invalid ID. Please enter numbers only.")
    else:
        customer_id = int(customer_id)

        if customer_id in customers:
            print("Customer already exists. Updating information.")
        else:
            print("Adding a new customer.")

        name = input("Enter customer name: ")
        pet = input("Enter pet name: ")
        pet_type = input("Enter pet type (Dog or Cat): ")
        breed = input("Enter pet breed: ")

        customers[customer_id] = {
            "name": name,
            "pet": pet,
            "type": pet_type,
            "breed": breed
        }

        print("Customer information saved successfully!")


# This runs the main menu 
def main():
    choice = ""

    while choice != "8":
        show_menu()

        choice = input("\nEnter your choice (1-8): ")

        if choice == "1":
            view_customers()

        elif choice == "2":
            add_customer()

        elif choice == "3":
            print("Coming soon!")

        elif choice == "4":
            print("Coming soon!")

        elif choice == "5":
            print("Coming soon!")

        elif choice == "6":
            print("Coming soon!")

        elif choice == "7":
            print("Coming soon!")

        elif choice == "8":
            print("Thank you for using Paws & Bubbles!")

        else:
            print("Invalid choice. Please select an option from 1-8.")


main()
