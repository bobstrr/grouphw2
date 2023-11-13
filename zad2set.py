parking_lot = set()

N = int(input("Enter the number of events: "))

for i in range(N):
    event, car_plate = input().split(", ")

    if event == "IN":
        parking_lot.add(car_plate)
    elif event == "OUT" and car_plate in parking_lot:
        parking_lot.remove(car_plate)

if parking_lot:
    for car in parking_lot:
        print(car)
else:
    print("Parking is Empty")