fn main() {
    println!("{}", prime_factors(600851475143).iter().max().unwrap())
}

fn prime_factors(mut number: i64) -> Vec<i64> {
    let mut factors = vec![];
    let mut divisor = 2;
    while number > 1 {
        while number % divisor == 0 {
            factors.push(divisor);
            number /= divisor;
        }
        divisor += 1;
    }
    factors
}