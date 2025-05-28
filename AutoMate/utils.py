def validate_license_plate(license_plate):
    if not isinstance(license_plate, str) or len(license_plate) == 0:
        raise ValueError("License plate must be a non-empty string.")
    return license_plate

def format_service_record(record):
    return f"Date: {record.date}, Description: {record.description}, Cost: ${record.cost:.2f}"

def format_customer_info(customer):
    return f"Customer ID: {customer.id}, Name: {customer.name}"

def format_vehicle_info(vehicle):
    return f"Vehicle ID: {vehicle.id}, License Plate: {vehicle.license_plate}"

def calculate_total_service_cost(service_records):
    return sum(record.cost for record in service_records)