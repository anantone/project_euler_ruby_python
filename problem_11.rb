class ProductGrid

  private

  attr_accessor :grid
  attr_writer :products

  def initialize(grid)
    self.grid = File.read(grid).split("\n").map do |line|
      line.split(' ').map { |number| number.to_i }
    end
    self.products = lines(grid) + columns(grid) + diagonals(grid)
  end

  public

  attr_reader :products

  def maximum_product
    products.max
  end

end
