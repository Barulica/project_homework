
from models.User import *
from models.Car import *

options = None

car = Car()

while options is None or options == "":
    options = input("Choose one option: "
                    "\n1.Add user"
                    "\n2.Show all users"
                    "\n3.Show rented cars"
                    "\n4.Show available cars"
                    "\n5.Rent a car"
                    "\n6.Exit\n")
    if options == "1":
        user = User()
        full_name = input("Enter your full name: ")
        age = int(input("Enter your age: "))
        user.name = full_name
        user.age = age
        user.add_user()
        options = None
    elif options == "2":
        all_users = User()
        print(all_users.show_all_users())
        options = None
    elif options == "3":
        rented_cars = Car()
        result = rented_cars.show_rented_or_available_cars(3)
        rented_cars.format_cars_table(result)
        options = None
    elif options == "4":
        available_cars = Car()
        result = available_cars.show_rented_or_available_cars(4)
        available_cars.format_cars_table(result)
        options = None
    elif options == "5":
        available_to_rent = Car()
        car_by_id_or_brand = input("Do you want the car by id or brand? ")
        if car_by_id_or_brand == "id":
            id = int(input("Enter the id: "))
            car = (available_to_rent.available_to_rent_by_id(id))
            available_to_rent.brand = car['brand']
            available_to_rent.model = car['model']
            available_to_rent.production_year = car['production_year']
            if car['rented'] is False:
                print(f"You rented {car['brand']} {car['model']} until {available_to_rent.rent_a_car()}")
                available_to_rent.rent_a_car()
                options = None
            else:
                print("This car is already rented")
                options = None
        elif car_by_id_or_brand == "brand":
            available_to_rent.brand = input ("Enter brand: \n")
            available_to_rent.model = input("Enter model: \n")
            available_to_rent.production_year = input("Enter production year: \n")
            is_rented = available_to_rent.available_to_rent_by_brand(available_to_rent.brand, available_to_rent.model, available_to_rent.production_year)
            if is_rented is False:
                print(f"You rented {available_to_rent.brand} {available_to_rent.model} until {available_to_rent.rent_a_car()}")
                available_to_rent.rent_a_car()
                options = None
            else:
                print("This car is already rented")
                options = None
        else:
            print("Invalid option")
            options = None
    elif options == "6":
        print("Thank you for your time! See you again!")
        break
    else:
        print("Invalid option")
        options = None

