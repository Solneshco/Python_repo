from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 15 Pro", "+79161234567"))
catalog.append(Smartphone("Samsung", "Galaxy S24 Ultra", "+79262345678"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 13 Pro", "+79373456789"))
catalog.append(Smartphone("Google", "Pixel 8 Pro", "+79484567890"))
catalog.append(Smartphone("OnePlus", "12", "+79595678901"))

print("Каталог смартфонов:")
print("-" * 40)

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}")