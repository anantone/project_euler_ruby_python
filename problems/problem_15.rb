class LatticePaths

  private

  attr_writer :squares

  def initialize(squares)
    self.squares = squares
  end

  public

  attr_reader :squares

  def count
    factorial(squares*2) / factorial(squares)**2
  end

  def factorial(number)
    (1..number).inject(:*)
  end

end

if __FILE__ == $PROGRAM_NAME
  puts LatticePaths.new(20).count
end
