# ByteBites Claude Code Instructions

You are helping with the ByteBites campus food-ordering system.

## Main Rule

Use exactly these four domain classes:

- `Customer`
- `FoodItem`
- `Menu`
- `Order`

Do not add extra domain classes unless the human explicitly asks.

## Design Rules

- Use composition, not inheritance.
- Do not make `FoodItem` inherit from `Menu`.
- Do not make `Order` inherit from `Customer`.
- Do not create `MenuManager`, `OrderManager`, `Restaurant`, or `PaymentProcessor`.
- Keep each class focused on one clear responsibility.
- Match the code to `bytebites_design.md`.

## Expected Relationships

- `Menu` contains many `FoodItem` objects.
- `Order` contains many `FoodItem` objects.
- `Order` belongs to one `Customer`.
- `Customer` stores a purchase history of completed orders.

## Coding Style

- Use readable Python.
- Prefer type hints.
- Keep methods short.
- Add helpful error handling.
- Do not over-engineer the project.
