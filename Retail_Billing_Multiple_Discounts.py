
# Railway Fare and Reservation Calculator

# Number of passengers
n = int(input("Enter number of passengers: "))

# Lists to store passenger details
passenger_names = []
final_fares = []
ticket_status = []

for i in range(n):

    print("\nEnter details of Passenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter passenger age: "))
    distance = float(input("Enter travel distance in km: "))

    print("\nTravel Classes:")
    print("1. Sleeper")
    print("2. AC 3 Tier")
    print("3. AC 2 Tier")

    travel_class = int(input("Enter travel class (1-3): "))

    # Validate passenger details
    if age < 0 or distance <= 0:
        print("Invalid passenger details!")
        continue

    # Calculate base fare using distance slabs
    if distance <= 100:
        base_fare = distance * 2

    elif distance <= 300:
        base_fare = 100 * 2 + (distance - 100) * 3

    else:
        base_fare = 100 * 2 + 200 * 3 + (distance - 300) * 4

    # Apply travel class charges
    if travel_class == 1:
        class_rate = 1.0
        reservation_fee = 20

    elif travel_class == 2:
        class_rate = 1.5
        reservation_fee = 40

    elif travel_class == 3:
        class_rate = 2.0
        reservation_fee = 60

    else:
        print("Invalid travel class!")
        continue

    # Calculate class fare
    class_fare = base_fare * class_rate

    # Calculate age-based concession
    if age < 5:
        concession = class_fare

    elif age >= 60:
        concession = class_fare * 20 / 100

    else:
        concession = 0

    # Calculate final fare
    total_fare = class_fare - concession + reservation_fee

    print("\nCancellation Details:")
    print("1. Cancel Ticket")
    print("2. Continue Journey")

    choice = int(input("Enter your choice (1-2): "))

    # Apply cancellation penalty
    if choice == 1:

        cancellation_penalty = total_fare * 25 / 100
        final_fare = total_fare - cancellation_penalty
        status = "Cancelled"

    elif choice == 2:

        cancellation_penalty = 0
        final_fare = total_fare
        status = "Confirmed"

    else:
        print("Invalid choice!")
        continue

    # Store passenger details
    passenger_names.append(name)
    final_fares.append(final_fare)
    ticket_status.append(status)

    # Display ticket details
    print("\n========== RAILWAY TICKET ==========")

    print("Passenger Name:", name)
    print("Age:", age)
    print("Distance:", distance, "km")
    print("Base Fare: Rs.", round(base_fare, 2))
    print("Class Fare: Rs.", round(class_fare, 2))
    print("Age Concession: Rs.", round(concession, 2))
    print("Reservation Fee: Rs.", reservation_fee)
    print("Total Fare: Rs.", round(total_fare, 2))
    print("Cancellation Penalty: Rs.",
          round(cancellation_penalty, 2))
    print("Final Amount: Rs.", round(final_fare, 2))
    print("Ticket Status:", status)


# Display final passenger summary
print("\n========== RAILWAY RESERVATION SUMMARY ==========")

for i in range(len(passenger_names)):

    print("\nPassenger:", passenger_names[i])
    print("Final Amount: Rs.", round(final_fares[i], 2))
    print("Status:", ticket_status[i])

print("\nRailway Fare Calculation Completed!")