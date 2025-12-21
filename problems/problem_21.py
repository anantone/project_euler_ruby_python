def main(up_to):
    return [find_amicable(up_to), sum(find_amicable(up_to))]

def find_amicable(up_to):
    return [x for x in range(1, up_to + 1) if sum_of_divisors(x) != x and
            sum_of_divisors(sum_of_divisors(x)) == x]


def sum_of_divisors(number):
    return sum([x for x in range(1, number) if number % x == 0])

if __name__ == "__main__":
    a = main(10000)
    b, c = a[0], a[1]
    print("The amicable numbers up to 10000 are: " + str(b))
    print("Their sum is " + str(c) + ".")
