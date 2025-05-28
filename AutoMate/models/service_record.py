from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

class ServiceRecord(Base):
    __tablename__ = 'service_records'

    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=False)
    description = Column(String, nullable=False)
    cost = Column(Float, nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=False)

    vehicle = relationship("Vehicle", back_populates="service_records")

    def __init__(self, date, description, cost, vehicle_id):
        self.date = date
        self.description = description
        self.cost = cost
        self.vehicle_id = vehicle_id

    def __repr__(self):
        return f"<ServiceRecord(id={self.id}, date={self.date}, description={self.description}, cost={self.cost})>"