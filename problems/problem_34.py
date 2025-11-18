# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
def main():
    digit_factorials = []
    for number in range(3, 250000):
        if sum([factorial(digit) for digit in digits(number)]) == number:
            digit_factorials.append(number)
    print(sum(digit_factorials))

def digits(number):
    return [int(digit) for digit in str(number)]

def factorial(number):
    if number == 0:
        return 1

    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial

if __name__ == "__main__":
    main()
