from dataclasses import dataclass


@dataclass
class Expense:
    category: str
    amount: float


def add_expense(expenses: list[Expense], category: str, amount: float) -> None:
    if amount <= 0:
        raise ValueError("Amount must be positive")
    expenses.append(Expense(category=category.strip().lower(), amount=amount))


def category_totals(expenses: list[Expense]) -> dict[str, float]:
    totals: dict[str, float] = {}
    for item in expenses:
        totals[item.category] = totals.get(item.category, 0.0) + item.amount
    return totals


if __name__ == "__main__":
    data: list[Expense] = []
    add_expense(data, "food", 15)
    add_expense(data, "travel", 40)
    print(category_totals(data))
