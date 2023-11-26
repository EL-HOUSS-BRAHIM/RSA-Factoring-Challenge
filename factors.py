import sys

def factorize_number(n):
    for i in range(2, n):
        if n % i == 0:
            return i, n // i
    return n, 1

def factorize_file(file_path):
    with open(file_path, 'r') as file:
        numbers = file.read().splitlines()

    factorizations = []
    for number in numbers:
        n = int(number)
        factors = factorize_number(n)
        factorizations.append(f"{n}={factors[0]}*{factors[1]}")

    return factorizations

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    factorizations = factorize_file(file_path)

    for factorization in factorizations:
        print(factorization)
