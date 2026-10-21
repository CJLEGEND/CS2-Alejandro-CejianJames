FARE_RATE = 14

name = input("Enter passenger name: ")

while len(name) == 0:
    print("Invalid passenger name")
    name = input("Enter passenger name: ")

distance = float(input("Enter distance (km): "))

while distance <= 0:
    print("Invalid distance")
    distance = float(input("Enter distance (km): "))
    
passengers = int(input("Enter number of passengers: "))

while passengers <= 0:
    print("Invalid number of passengers")
    passengers = int(input("Enter number of passengers: "))


total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))
