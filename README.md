# ByteBites Campus Food Ordering System

ByteBites is a small object-oriented design project for a campus food-ordering system.  
The project focuses on designing the system before writing code.

## Project Goal

The goal is to model a simple food-ordering system using four main classes:

- `Customer`
- `FoodItem`
- `Menu`
- `Order`

The system uses composition instead of inheritance. For example, a `Menu` has many `FoodItem` objects, and an `Order` has a `Customer` and many `FoodItem` objects.

## Folder Structure

```text
ByteBites_Project/
├── .github/
│   └── agents/
│       └── bytebites_design_agent.md
├── bytebites/
│   ├── __init__.py
│   ├── main.py
│   └── models.py
├── tests/
│   └── test_models.py
├── bytebites_design.md
├── CLAUDE.md
├── README.md
└── requirements.txt
```

## How to Run the Demo

From the main project folder, run:

```bash
python -m bytebites.main
```

## How to Run the Tests

This project uses Python's built-in `unittest`, so no extra packages are needed.

```bash
python -m unittest discover -s tests
```

## Design Notes

This project avoids inheritance because the class relationships are mostly "has-a" relationships:

- A `Menu` has `FoodItem` objects.
- An `Order` has a `Customer`.
- An `Order` has `FoodItem` objects.
- A `Customer` has an order history.

This keeps the system easier to read, test, and maintain.
