class Cars:
    def __init__(self, id, first_name, last_name, gender, brand, year, color, country):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.brand = brand
        self.year = year
        self.color = color
        self.country = country

    def find_gender_ratio(self):
        total_count = 0
        female_count = 0
        male_count = 0

        for car in cars_list:
            total_count += 1
            if car.gender == 'female':
                female_count += 1
            elif car.gender == 'male':
                male_count += 1

        female_ratio = (female_count / total_count) * 100
        male_ratio = (male_count / total_count) * 100

        return f"Erkaklar ayollar bo'yicha {male_ratio}% nisbatda, Ayollar erkaklar bo'yicha {female_ratio}% nisbatda."


    def most_popular_brand(cars_list):
        brand_counts = {}
        for car in cars_list:
            brand = car.brand
            if brand in brand_counts:
                brand_counts[brand] += 1
            else:
                brand_counts[brand] = 1

        most_popular_brand = max(brand_counts, key=brand_counts.get)
        most_popular_count = brand_counts[most_popular_brand]

        return f"{most_popular_brand} brendi {most_popular_count} ta mashinaga egadir."

    def prepare_message(self):
        if self.year < 2005:
            return f"Kimdan: Auto Test Corp. Kimga: {self.first_name} {self.last_name} Joriy davlat: {self.country}\n" \
                   f"Hurmatli {self.first_name} {self.last_name}! {self.brand} tomonidan {self.year}da ishlab chiqarilgan " \
                   f"{self.color} rangli avtoulovingiz Texnik Holatini tekshirtirsh maqsadida mahalliy Auto Test Corp. " \
                   f"ofisiga murojaat qilishingizni so'raymiz!"


car1 = Cars(1, "John", "Doe", "male", "Toyota", 2000, "blue", "USA")
car2 = Cars(2, "Alice", "Smith", "female", "Honda", 2010, "red", "Japan")
car3 = Cars(3, "Bob", "Johnson", "male", "Toyota", 2008, "silver", "Japan")
car4 = Cars(4, "Eva", "Brown", "female", "Ford", 2015, "black", "USA")

cars_list = [car1, car2, car3, car4]

print(car1.find_gender_ratio())
print(Cars.most_popular_brand(cars_list))
print(car1.prepare_message())
