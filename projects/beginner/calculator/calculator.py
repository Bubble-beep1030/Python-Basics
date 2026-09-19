def calculate(op: str, a: float, b: float) -> float:
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b
    raise ValueError("Unsupported operation")


if __name__ == "__main__":
    print(calculate("+", 2, 3))
