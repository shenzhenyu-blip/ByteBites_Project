"""Demo runner for the ByteBites project."""

from bytebites.models import Customer, FoodItem, Menu, Order


def build_sample_menu() -> Menu:
    """Create a sample campus menu."""
    menu = Menu()

    menu.add_item(FoodItem("Chicken Rice Bowl", 9.99, "Entree"))
    menu.add_item(FoodItem("Veggie Wrap", 7.49, "Entree"))
    menu.add_item(FoodItem("Iced Tea", 2.99, "Drink"))
    menu.add_item(FoodItem("Chocolate Cookie", 1.99, "Dessert"))

    return menu


def main() -> None:
    """Run a simple ByteBites ordering example."""
    menu = build_sample_menu()

    customer = Customer(name="Alex Chen", email="alex.chen@example.com")
    order = Order(customer=customer)

    rice_bowl = menu.find_item("Chicken Rice Bowl")
    iced_tea = menu.find_item("Iced Tea")

    if rice_bowl:
        order.add_item(rice_bowl)

    if iced_tea:
        order.add_item(iced_tea)

    print("Before placing order:")
    print(order.summary())

    order.place_order()

    print("\nAfter placing order:")
    print(order.summary())

    print(f"\n{customer.name}'s total spent: ${customer.total_spent():.2f}")


if __name__ == "__main__":
    main()
