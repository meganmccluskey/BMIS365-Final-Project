
# Paws & Bubbles Pet Grooming Manager

# Customer names and their pets
customers = {
    101: {"name": "Ryland Grace", "pet": "Rocky",
          "type": "Cat", "breed": "Maine Coon"},

    102: {"name": "Mark Watney", "pet": "Potato",
          "type": "Dog", "breed": "Labrador Retriever"},

    103: {"name": "Spike Spiegel", "pet": "Ein",
          "type": "Dog", "breed": "Corgi"}
}

# List storing completed grooming transactions
appointments = []


# This loads customer information from the CSV file.
def load_customers():
    with open("customers.csv", "r") as f:
        line_number = 0

        for line in f:
            line = line.strip()
            line_number += 1

            if line_number > 1 and line != "":
                values = line.split(",")

                customer_id = int(values[0].strip())

                customers[customer_id] = {
                    "name": values[1].strip(),
                    "pet": values[2].strip(),
                    "type": values[3].strip(),
                    "breed": values[4].strip()
                }


# This saves customer information to the CSV file.
def save_customers():
    with open("customers.csv", "w") as f:
        f.write("customer_id,customer_name,pet_name,pet_type,pet_breed\n")

        for customer_id in customers:
            f.write(str(customer_id) + ",")
            f.write(customers[customer_id]["name"] + ",")
            f.write(customers[customer_id]["pet"] + ",")
            f.write(customers[customer_id]["type"] + ",")
            f.write(customers[customer_id]["breed"] + "\n")


# This loads appointment transactions from the CSV file.
def load_appointments():
    with open("appointments.csv", "r") as f:
        line_number = 0

        for line in f:
            line = line.strip()
            line_number += 1

            if line_number > 1 and line != "":
                values = line.split(",")

                appointment = {
                    "date": values[0].strip(),
                    "customer_id": int(values[1].strip()),
                    "pet_name": values[2].strip(),
                    "service": values[3].strip(),
                    "price": float(values[4].strip())
                }

                appointments.append(appointment)


# This saves appointment transactions to the CSV file.
def save_appointments():
    with open("appointments.csv", "w") as f:
        f.write("date,customer_id,pet_name,service,price\n")

        for appointment in appointments:
            f.write(appointment["date"] + ",")
            f.write(str(appointment["customer_id"]) + ",")
            f.write(appointment["pet_name"] + ",")
            f.write(appointment["service"] + ",")
            f.write(str(appointment["price"]) + "\n")


# This records a completed grooming service.
def record_service():
    print("\n===== RECORD COMPLETED SERVICE =====")

    date = input("Enter service date: ")
    customer_id = input("Enter customer ID: ")

    valid_id = True

    for number in customer_id:
        if number < "0" or number > "9":
            valid_id = False

    if valid_id == False or customer_id == "":
        print("Invalid customer ID.")
        return

    customer_id = int(customer_id)

    if customer_id not in customers:
        print("Customer not found. Please add the customer first.")
        return

    pet_name = customers[customer_id]["pet"]

    service = input("Enter grooming service: ")
    price = input("Enter service price: ")

    valid_price = True
    decimal_count = 0

    for number in price:
        if number == ".":
            decimal_count += 1
        elif number < "0" or number > "9":
            valid_price = False

    if price == "" or valid_price == False or decimal_count > 1:
        print("Invalid price. Please enter a number.")
        return

    price = float(price)

    if date == "" or service == "" or price <= 0:
        print("Please enter a date, service, and positive price.")
        return

    appointment = {
        "date": date,
        "customer_id": customer_id,
        "pet_name": pet_name,
        "service": service,
        "price": price
    }

    appointments.append(appointment)

    print("Completed service recorded successfully!")
    print("Appointments:", appointments)


# This adds or updates customers.
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

        if name == "" or pet == "" or pet_type == "" or breed == "":
            print("Please fill in all customer information.")

        else:
            customers[customer_id] = {
                "name": name,
                "pet": pet,
                "type": pet_type,
                "breed": breed
            }

            print("Customer information added successfully!")


# This displays all customers and their pets.
def view_customers():
    print("\n===== CUSTOMER LIST =====")

    for customer_id in customers:
        print("-----------------------------")
        print("Customer ID:", customer_id)
        print("Customer Name:", customers[customer_id]["name"])
        print("Pet Name:", customers[customer_id]["pet"])
        print("Pet Type:", customers[customer_id]["type"])
        print("Pet Breed:", customers[customer_id]["breed"])


# This displays the menu.
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


# This runs the main menu.
def main():
    load_customers()
    load_appointments()

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
            record_service()

        elif choice == "6":
            print("Coming soon!")

        elif choice == "7":
            print("Coming soon!")

        elif choice == "8":
            save_customers()
            save_appointments()
            print("Customer information saved!")
            print("Appointment transactions saved!")
            print("Thank you for using Paws & Bubbles!")

        else:
            print("Invalid choice. Please select an option from 1-8.")


# Start the program.
main()
