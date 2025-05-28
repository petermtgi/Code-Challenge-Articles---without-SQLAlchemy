# AutoMate

AutoMate is a command-line interface (CLI) application designed for managing customers, their vehicles, and vehicle service records in a car repair shop. This application allows users to efficiently handle various tasks related to customer and vehicle management.

## Features

- **Add and manage customers**: Easily add new customers and keep track of their information.
- **Add and manage vehicles**: Link vehicles to customers and manage vehicle details.
- **Add service records**: Record service history for each vehicle, including costs and descriptions.
- **Search for vehicles**: Quickly find a vehicle by its license plate.
- **View customer vehicles**: Display all vehicles associated with a specific customer, along with their service history.
- **Calculate service costs**: Get the total cost of services performed on a vehicle.
- **Top-spending customer** (optional): Identify the customer who has spent the most on services.

## Technical Requirements

- **Python Version**: 3.11+
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Dependency Management**: Pipenv

## Project Structure

```
AutoMate
├── models
│   ├── __init__.py
│   ├── customer.py
│   ├── vehicle.py
│   └── service_record.py
├── cli.py
├── db.py
├── utils.py
├── seed.py
├── Pipfile
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/AutoMate.git
   cd AutoMate
   ```

2. Install dependencies using Pipenv:
   ```
   pipenv install
   ```

3. Activate the virtual environment:
   ```
   pipenv shell
   ```

## Usage

1. Initialize the database:
   ```
   python db.py
   ```

2. Seed the database with sample data (optional):
   ```
   python seed.py
   ```

3. Run the CLI application:
   ```
   python cli.py
   ```

4. Follow the on-screen menu to manage customers, vehicles, and service records.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.