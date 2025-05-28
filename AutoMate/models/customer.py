from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    vehicles = relationship("Vehicle", back_populates="customer")

    def __repr__(self):
        return f"<Customer(id={self.id}, name='{self.name}')>"

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)