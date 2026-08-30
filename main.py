def add(a, b): return a + b


def subtract(a, b): return a - b


def multiply(a, b): return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate(expression):

    tokens = expression.split()
    if len(tokens) != 3:
        raise ValueError("Expected format: number operator number")

    a, op, b = tokens
    a, b = float(a), float(b)

    operations = {
        '+': add, '-': subtract,
        '*': multiply, '/': divide
    }

    if op not in operations:
        raise ValueError(f"Unknown operator: {op}")

    return operations[op](a, b)


def main():
    print("Python Calculator (type 'quit' to exit)")
    history = []

    while True:
        expr = input("\nEnter calculation (e.g. 5 + 3): ").strip()
        if expr.lower() == 'quit':
            break
        try:
            result = calculate(expr)
            print(f"Result: {result}")
            history.append(f"{expr} = {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero")

    if history:
        print("\n--- History ---")
        for line in history:
            print(line)


if __name__ == "__main__":
    main()
