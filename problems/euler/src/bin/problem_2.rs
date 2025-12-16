fn main() {
    println!("{}", sum_evens(generate_fibonacci(4000000)));
}

fn sum_evens(numbers: Vec<u64>) -> u64 {
    numbers.iter().filter(|&x| x % 2 == 0).sum()
}

fn generate_fibonacci(upper_limit: u64) -> Vec<u64> {
    let mut fibonacci = vec![1, 2];
    while *fibonacci.last().unwrap() < upper_limit {
        fibonacci.push(fibonacci[fibonacci.len() - 1] + fibonacci[fibonacci.len() - 2]);
    }
    fibonacci
}
