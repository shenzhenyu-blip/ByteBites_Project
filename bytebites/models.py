"""Core models for the ByteBites campus food-ordering system.

The project intentionally uses four classes only:
Customer, FoodItem, Menu, and Order.

The relationships use composition instead of inheritance.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class FoodItem:
    """A single food item that can appear on a menu or inside an order."""

    name: str
    price: float
    category: str
    is_available: bool = True

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Food item name cannot be empty.")
        if self.price < 0:
            raise ValueError("Food item price cannot be negative.")
        if not self.category.strip():
            raise ValueError("Food item category cannot be empty.")

    def mark_available(self) -> None:
        """Make this item available to order."""
        self.is_available = True

    def mark_unavailable(self) -> None:
        """Make this item unavailable to order."""
        self.is_available = False


@dataclass
class Customer:
    """A customer with a name, email, and purchase history."""

    name: str
    email: str
    purchase_history: list[Order] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Customer name cannot be empty.")
        if "@" not in self.email:
            raise ValueError("Customer email must contain @.")

    def add_order(self, order: Order) -> None:
        """Add a completed order to the customer's purchase history."""
        if order not in self.purchase_history:
            self.purchase_history.append(order)

    def total_spent(self) -> float:
        """Return the total amount this customer has spent."""
        return sum(order.calculate_total() for order in self.purchase_history)


@dataclass
class Menu:
    """A menu that stores food items customers can order."""

    items: list[FoodItem] = field(default_factory=list)

    def add_item(self, item: FoodItem) -> None:
        """Add a food item to the menu."""
        if self.find_item(item.name) is not None:
            raise ValueError(f"{item.name} is already on the menu.")
        self.items.append(item)

    def remove_item(self, item_name: str) -> FoodItem:
        """Remove and return a food item by name."""
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                return item
        raise ValueError(f"{item_name} was not found on the menu.")

    def find_item(self, item_name: str) -> FoodItem | None:
        """Find a food item by name. Return None if it is not found."""
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def available_items(self) -> list[FoodItem]:
        """Return all currently available food items."""
        return [item for item in self.items if item.is_available]


@dataclass
class Order:
    """An order that belongs to one customer and contains food items."""

    customer: Customer
    items: list[FoodItem] = field(default_factory=list)
    status: str = "cart"

    def add_item(self, item: FoodItem) -> None:
        """Add an available food item to the order."""
        if self.status != "cart":
            raise ValueError("Cannot add items after the order has been placed or cancelled.")
        if not item.is_available:
            raise ValueError(f"{item.name} is currently unavailable.")
        self.items.append(item)

    def remove_item(self, item_name: str) -> FoodItem:
        """Remove and return one item from the order by name."""
        if self.status != "cart":
            raise ValueError("Cannot remove items after the order has been placed or cancelled.")

        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                return item

        raise ValueError(f"{item_name} was not found in the order.")

    def calculate_total(self) -> float:
        """Calculate the total price of the order."""
        return round(sum(item.price for item in self.items), 2)

    def place_order(self) -> None:
        """Place the order and add it to the customer's purchase history."""
        if self.status != "cart":
            raise ValueError("Only orders in cart status can be placed.")
        if not self.items:
            raise ValueError("Cannot place an empty order.")

        self.status = "placed"
        self.customer.add_order(self)

    def cancel_order(self) -> None:
        """Cancel the order if it has not already been placed."""
        if self.status == "placed":
            raise ValueError("Cannot cancel an order after it has been placed.")
        self.status = "cancelled"

    def summary(self) -> str:
        """Return a readable summary of the order."""
        item_names = ", ".join(item.name for item in self.items) if self.items else "No items"
        return (
            f"Customer: {self.customer.name}\n"
            f"Items: {item_names}\n"
            f"Status: {self.status}\n"
            f"Total: ${self.calculate_total():.2f}"
        )
