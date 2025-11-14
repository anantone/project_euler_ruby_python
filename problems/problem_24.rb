class LexicographicPermutations

  private

  attr_writer :digits

  def initialize(up_to)
    self.digits = (0..up_to).to_a
  end

  public

  attr_reader :digits

  def lexicographic_permutations
    digits.permutation.sort
  end

end

if __FILE__ == $PROGRAM_NAME
  puts LexicographicPermutations.new(9).lexicographic_permutations[999999]
end
