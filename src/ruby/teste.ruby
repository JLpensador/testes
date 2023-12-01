class Person
  def initialize(nome, idade)
    @nome = nome
    @idade = idade
  end

  def introduce
    "O elemento se chama #{@nome} e tem #{idade} anos, ele está a solta"
  end

  def adult?
    @idade >= 18
  end
end
