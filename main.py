import sys

def add(a, b):
    return a + b

if __name__ == "__main__":
    if len(sys.argv) == 3:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        result = add(num1, num2)
        print(f"The result is {result}")
    else:
        print("Usage: python main.py <number1> <number2>")
