import matplotlib.pyplot as plt


# Displays a summary of grooming sales
def sales_report(appointments):
    print("\n===== SALES REPORT =====")

    if len(appointments) == 0:
        print("No transactions recorded yet.")

    else:
        total_sales = 0
        service_totals = {}
        service_counts = {}

        # Goes through each appointment
        for appointment in appointments:
            total_sales = total_sales + appointment["price"]

            service = appointment["service"]

            # Adds the revenue for each service
            if service in service_totals:
                service_totals[service] = service_totals[service] + appointment["price"]
                service_counts[service] = service_counts[service] + 1
            else:
                service_totals[service] = appointment["price"]
                service_counts[service] = 1

        number_of_appointments = len(appointments)
        average_sale = total_sales / number_of_appointments

        # Finds the service with the highest revenue
        top_service = ""
        highest_revenue = 0

        for service in service_totals:
            if service_totals[service] > highest_revenue:
                highest_revenue = service_totals[service]
                top_service = service

        # Finds the service with the lowest revenue
        bottom_service = top_service
        lowest_revenue = highest_revenue

        for service in service_totals:
            if service_totals[service] < lowest_revenue:
                lowest_revenue = service_totals[service]
                bottom_service = service

        print("Appointments recorded:", number_of_appointments)
        print("Total revenue: $", total_sales)
        print("Average sale: $", average_sale)
        print("Top service:", top_service)
        print("Lowest revenue service:", bottom_service)

        print("\nRevenue and appointments by service:")

        for service in service_totals:
            print(service)
            print("Appointments:", service_counts[service])
            print("Revenue: $", service_totals[service])


# Creates two charts for the business
def charts(appointments):

    if len(appointments) == 0:
        print("No transactions available to create charts.")

    else:
        service_revenue = {}
        daily_appointments = {}

        # Collects revenue for each service and appointments by date
        for appointment in appointments:
            service = appointment["service"]
            date = appointment["date"]

            if service in service_revenue:
                service_revenue[service] = service_revenue[service] + appointment["price"]
            else:
                service_revenue[service] = appointment["price"]

            if date in daily_appointments:
                daily_appointments[date] = daily_appointments[date] + 1
            else:
                daily_appointments[date] = 1

        # Prepares the information for the first chart
        services = []
        revenue = []

        for service in service_revenue:
            services.append(service)
            revenue.append(service_revenue[service])

        # Creates the revenue bar chart
        plt.figure()
        plt.bar(services, revenue)
        plt.title("Revenue by Grooming Service")
        plt.xlabel("Grooming Service")
        plt.ylabel("Revenue ($)")
        plt.tight_layout()
        plt.savefig("revenue_by_service.png")
        plt.show()
        plt.close()

        # Prepares the information for the second chart
        dates = []
        appointment_counts = []

        for date in daily_appointments:
            dates.append(date)
            appointment_counts.append(daily_appointments[date])

        # Creates the appointments line chart
        plt.figure()
        plt.plot(dates, appointment_counts, marker="o")
        plt.title("Appointments by Day")
        plt.xlabel("Date")
        plt.ylabel("Number of Appointments")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("appointments_by_day.png")
        plt.show()
        plt.close()
