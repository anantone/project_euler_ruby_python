# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
class DigitFactorials

  private

  def initialize
    @digit_factorials = digit_factorials
  end

  def digit_factorials
    (3..250_000).each_with_object([]) do |number, list|
      list.push(number) if number.digits.map { |digit| factorial(digit) }.compact.sum == number
    end
  end

  def factorial(number)
    return 1 if number == 0

    (1..number).inject(:*)
  end

  public

  def sum
    @digit_factorials.sum
  end

end

