# shopping_app.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import json


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ProductCollection:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def load_from_json(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            for item in data:
                product = Product(item['name'], item['price'])
                self.add_product(product)


class ShoppingApp(App):
    def build(self):
        self.total = 0.0
        self.product_collection = ProductCollection()
        self.product_collection.load_from_json('products.json')

        # Load the layout from KV file
        root = self.root

        # Add buttons for each product
        for product in self.product_collection.products:
            btn = Button(
                text=f"{product.name}, ${product.price:.2f}",
                on_press=lambda instance, price=product.price: self.add_to_total(price)
            )
            root.add_widget(btn)

        return root

    def add_to_total(self, price):
        self.total += price
        self.update_total_label()

    def clear_total(self):
        self.total = 0.0
        self.update_total_label()

    def update_total_label(self):
        self.root.ids.total_label.text = f"Total: ${self.total:.2f}"


# Run the app
if __name__ == '__main__':
    ShoppingApp().run()
