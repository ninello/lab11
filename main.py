
def z1():
    class Restaurant:  # создаем класс с помощью метода init с двумя аргументами
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):  # метод describe_restaurant выводит название ресторана и тип кухни
            print(f"The restaurant name is {self.restaurant_name}.")
            print(f"The cuisine type is {self.cuisine_type}.")

        def open_restaurant(self):  # выводит сообщение о том, что ресторан открыт в данный момент
            print("The restaurant is open.")

    newRestaurant = Restaurant(input("name: "), input("tipe: "))  # создаем ресторан с именем pizza palace с типом итальянская
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)
    newRestaurant.describe_restaurant()  # отвечает за описание ресторана
    newRestaurant.open_restaurant()  # выводит сообщение о том, что ресторан открыт

    restaurant1 = Restaurant("Pizza Palace", "Italian")
    restaurant2 = Restaurant("Taco Town", "Mexican")
    restaurant3 = Restaurant("Burger Barn", "American")

    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type,
                     rating):  # в этом классе выводится имя ресторана, тип кухни и рейтинг и инициализирует их как переменные
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):  # здесь также выводится название, тип и рейтинг ресторана
            print(f"The restaurant name is {self.restaurant_name}.")
            print(f"The cuisine type is {self.cuisine_type}.")
            print(f"The rating is {self.rating}.")

        def update_rating(self,
                          new_rating):  # метод update_rating принимает аргумент new_raiting и обновляет рейтинг переменной новым значением
            self.rating = new_rating

    restaurant1 = Restaurant("Pizza Palace", "Italian",
                             4.5)  # создаем экземпляр класса Restaurant с именем restaurant1 с аргументами pizza place, Italian,4.5

    restaurant1.describe_restaurant()  # выводим название, тип и рейтинг

    restaurant1.update_rating(4.8)  # обновляем рейтинг ресторана



def z2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = 0

        def describe_restaurant(self):
            print(f"The restaurant name is {self.restaurant_name}.")
            print(f"The cuisine type is {self.cuisine_type}.")
            print(f"The rating is {self.rating}.")

        def update_rating(self, new_rating):
            self.rating = new_rating
            return self.rating

    restaurant1 = Restaurant("Pizza Palace", "Italian")

    restaurant1.describe_restaurant()

    new_rating = restaurant1.update_rating(4.8)
    print(f"The new rating is {new_rating}.")

z1()
z2()