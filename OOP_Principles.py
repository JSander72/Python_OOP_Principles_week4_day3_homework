from helper import d

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

    def get_category_name(self):
        return self.__category_name

    def get_allocated_budget(self):
        return self.__allocated_budget

    def get_remaining_budget(self):
        return self.__remaining_budget

    def set_category_name(self, category_name):
        self.__category_name = category_name

    def set_allocated_budget(self, allocated_budget):
        if allocated_budget > 0:
            self.__allocated_budget = allocated_budget
            self.__remaining_budget = allocated_budget  

    def add_expense(self, amount):
        if amount > 0 and amount <= self.__remaining_budget:
            self.__remaining_budget -= amount
        else:
            print("Invalid expense amount.")

    def display_category_summary(self):
        print(f"Category: {self.get_category_name()}")
        print(f"Allocated Budget: ${self.get_allocated_budget():.2f}")
        print(f"Remaining Budget: ${self.get_remaining_budget():.2f}")

food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()

d()

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")

class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")

# Example usage
my_book = Book("123", "Python Essentials", 29.99, "J. Doe")
my_book.display_info()





