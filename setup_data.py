import os
import django
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'car_rental_system.settings')
django.setup()

from cars.models import Car

def create_cars():
    if Car.objects.count() > 0:
        print("Cars already exist. Skipping creation.")
        return

    data = [
        {
            "make": "Toyota", "model": "Camry", "year": 2023,
            "license_plate": "ABC-1234", "price_per_day": Decimal("50.00"),
            "description": "Reliable and comfortable sedan for city driving.",
            "status": "AVAILABLE"
        },
        {
            "make": "Honda", "model": "CR-V", "year": 2022,
            "license_plate": "XYZ-5678", "price_per_day": Decimal("75.00"),
            "description": "Spacious SUV perfect for family trips.",
            "status": "AVAILABLE"
        },
        {
            "make": "Ford", "model": "Mustang", "year": 2024,
            "license_plate": "FST-9999", "price_per_day": Decimal("120.00"),
            "description": "Experience the power of a classic American muscle car.",
            "status": "AVAILABLE"
        }
    ]

    for item in data:
        Car.objects.create(**item)
        print(f"Created {item['year']} {item['make']} {item['model']}")

if __name__ == "__main__":
    create_cars()
