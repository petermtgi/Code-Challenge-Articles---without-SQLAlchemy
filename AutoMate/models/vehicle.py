from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

class Vehicle(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    license_plate = Column(String, unique=True, nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)

    customer = relationship("Customer", back_populates="vehicles")
    service_records = relationship("ServiceRecord", back_populates="vehicle")

    def __init__(self, license_plate, customer_id):
        self.license_plate = license_plate
        self.customer_id = customer_id

    def __repr__(self):
        return f"<Vehicle(id={self.id}, license_plate='{self.license_plate}', customer_id={self.customer_id})>"