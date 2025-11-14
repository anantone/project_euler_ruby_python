def main():
    print(count(20))

def count(squares):
    return int(factorial(squares*2) / factorial(squares)**2)

def factorial(number):
    factorial = 1
    for i in range(1, number+1):
        factorial *= i
    return factorial

if __name__ == "__main__":
    main()

