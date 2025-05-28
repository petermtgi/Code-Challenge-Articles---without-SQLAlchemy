from models.customer import Customer
from models.vehicle import Vehicle
from models.service_record import ServiceRecord
from db import Session, engine
from utils import input_customer_data, input_vehicle_data, input_service_record_data, display_vehicles, display_service_records, display_top_spending_customer
from tabulate import tabulate

def main_menu():
    print("Welcome to AutoMate!")
    while True:
        print("\nPlease choose an option:")
        print("1. Add a customer")
        print("2. Add a vehicle to a customer")
        print("3. Add a service record to a vehicle")
        print("4. View all vehicles for a customer")
        print("5. View all service records for a vehicle")
        print("6. Search for a vehicle by license plate")
        print("7. Show total service cost for a vehicle")
        print("8. Show top-spending customer (optional)")
        print("9. Exit program")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            customer_data = input_customer_data()
            with Session() as session:
                new_customer = Customer(**customer_data)
                session.add(new_customer)
                session.commit()
                print("Customer added successfully.")
        
        elif choice == '2':
            vehicle_data = input_vehicle_data()
            with Session() as session:
                customer = session.query(Customer).filter_by(id=vehicle_data['customer_id']).first()
                if customer:
                    new_vehicle = Vehicle(**vehicle_data)
                    customer.vehicles.append(new_vehicle)
                    session.commit()
                    print("Vehicle added successfully.")
                else:
                    print("Customer not found.")
        
        elif choice == '3':
            service_record_data = input_service_record_data()
            with Session() as session:
                vehicle = session.query(Vehicle).filter_by(id=service_record_data['vehicle_id']).first()
                if vehicle:
                    new_service_record = ServiceRecord(**service_record_data)
                    vehicle.service_records.append(new_service_record)
                    session.commit()
                    print("Service record added successfully.")
                else:
                    print("Vehicle not found.")
        
        elif choice == '4':
            customer_id = input("Enter customer ID: ")
            with Session() as session:
                customer = session.query(Customer).filter_by(id=customer_id).first()
                if customer:
                    display_vehicles(customer.vehicles)
                else:
                    print("Customer not found.")
        
        elif choice == '5':
            vehicle_id = input("Enter vehicle ID: ")
            with Session() as session:
                vehicle = session.query(Vehicle).filter_by(id=vehicle_id).first()
                if vehicle:
                    display_service_records(vehicle.service_records)
                else:
                    print("Vehicle not found.")
        
        elif choice == '6':
            license_plate = input("Enter license plate: ")
            with Session() as session:
                vehicle = session.query(Vehicle).filter_by(license_plate=license_plate).first()
                if vehicle:
                    print(f"Vehicle found: {vehicle}")
                else:
                    print("Vehicle not found.")
        
        elif choice == '7':
            vehicle_id = input("Enter vehicle ID: ")
            with Session() as session:
                vehicle = session.query(Vehicle).filter_by(id=vehicle_id).first()
                if vehicle:
                    total_cost = sum(record.cost for record in vehicle.service_records)
                    print(f"Total service cost for vehicle {vehicle_id}: ${total_cost:.2f}")
                else:
                    print("Vehicle not found.")
        
        elif choice == '8':
            with Session() as session:
                top_customer = display_top_spending_customer(session)
                if top_customer:
                    print(f"Top-spending customer: {top_customer.name} with total spending of ${top_customer.total_spent:.2f}")
        
        elif choice == '9':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()