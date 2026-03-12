import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'car_rental_system.settings')
django.setup()

from cars.models import Car

def update_images():
    updates = {
        "Toyota": "cars/camry.png",
        "Honda": "cars/crv.png",
        "Ford": "cars/mustang.png"
    }

    for make, image_path in updates.items():
        try:
            car = Car.objects.get(make=make)
            car.image = image_path
            car.save()
            print(f"Updated image for {make} {car.model}")
        except Car.DoesNotExist:
            print(f"Car make {make} not found")

if __name__ == "__main__":
    update_images()
