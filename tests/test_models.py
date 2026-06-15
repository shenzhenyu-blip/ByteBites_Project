"""Unit tests for the ByteBites models."""

import unittest

from bytebites.models import Customer, FoodItem, Menu, Order


class TestFoodItem(unittest.TestCase):
    def test_food_item_can_be_marked_unavailable(self):
        item = FoodItem("Pizza Slice", 3.50, "Entree")
        item.mark_unavailable()
        self.assertFalse(item.is_available)

    def test_food_item_price_cannot_be_negative(self):
        with self.assertRaises(ValueError):
            FoodItem("Bad Item", -1.00, "Entree")


class TestMenu(unittest.TestCase):
    def test_menu_can_add_and_find_item(self):
        menu = Menu()
        item = FoodItem("Burger", 8.99, "Entree")

        menu.add_item(item)

        self.assertEqual(menu.find_item("Burger"), item)

    def test_menu_returns_only_available_items(self):
        menu = Menu()
        burger = FoodItem("Burger", 8.99, "Entree")
        soda = FoodItem("Soda", 1.99, "Drink", is_available=False)

        menu.add_item(burger)
        menu.add_item(soda)

        self.assertEqual(menu.available_items(), [burger])


class TestOrder(unittest.TestCase):
    def test_order_calculates_total(self):
        customer = Customer("Taylor", "taylor@example.com")
        order = Order(customer)

        order.add_item(FoodItem("Taco", 4.50, "Entree"))
        order.add_item(FoodItem("Water", 1.25, "Drink"))

        self.assertEqual(order.calculate_total(), 5.75)

    def test_order_adds_to_customer_history_when_placed(self):
        customer = Customer("Jordan", "jordan@example.com")
        order = Order(customer)
        order.add_item(FoodItem("Sandwich", 6.99, "Entree"))

        order.place_order()

        self.assertEqual(order.status, "placed")
        self.assertIn(order, customer.purchase_history)

    def test_unavailable_item_cannot_be_ordered(self):
        customer = Customer("Casey", "casey@example.com")
        order = Order(customer)
        item = FoodItem("Sold Out Cookie", 1.99, "Dessert", is_available=False)

        with self.assertRaises(ValueError):
            order.add_item(item)

    def test_empty_order_cannot_be_placed(self):
        customer = Customer("Morgan", "morgan@example.com")
        order = Order(customer)

        with self.assertRaises(ValueError):
            order.place_order()


class TestCustomer(unittest.TestCase):
    def test_customer_total_spent(self):
        customer = Customer("Riley", "riley@example.com")

        order_one = Order(customer)
        order_one.add_item(FoodItem("Rice Bowl", 9.99, "Entree"))
        order_one.place_order()

        order_two = Order(customer)
        order_two.add_item(FoodItem("Tea", 2.50, "Drink"))
        order_two.place_order()

        self.assertEqual(customer.total_spent(), 12.49)


if __name__ == "__main__":
    unittest.main()
