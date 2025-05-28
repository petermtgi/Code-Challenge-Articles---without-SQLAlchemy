from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.customer import Customer
from models.vehicle import Vehicle
from models.service_record import ServiceRecord
from db import Base

def seed_database():
    engine = create_engine('sqlite:///automate.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Sample customers
    customer1 = Customer(name="John Doe")
    customer2 = Customer(name="Jane Smith")

    # Sample vehicles
    vehicle1 = Vehicle(license_plate="ABC123", customer=customer1)
    vehicle2 = Vehicle(license_plate="XYZ789", customer=customer1)
    vehicle3 = Vehicle(license_plate="LMN456", customer=customer2)

    # Sample service records
    service_record1 = ServiceRecord(date="2023-01-15", description="Oil Change", cost=29.99, vehicle=vehicle1)
    service_record2 = ServiceRecord(date="2023-02-20", description="Tire Rotation", cost=49.99, vehicle=vehicle1)
    service_record3 = ServiceRecord(date="2023-03-10", description="Brake Inspection", cost=89.99, vehicle=vehicle2)
    service_record4 = ServiceRecord(date="2023-01-25", description="Battery Replacement", cost=120.00, vehicle=vehicle3)

    # Add to session
    session.add_all([customer1, customer2, vehicle1, vehicle2, vehicle3, service_record1, service_record2, service_record3, service_record4])
    
    # Commit the session
    session.commit()
    session.close()

if __name__ == "__main__":
    seed_database()