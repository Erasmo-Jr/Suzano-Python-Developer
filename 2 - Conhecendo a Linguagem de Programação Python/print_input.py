nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")

print(nome, idade)
print(f"Meu nome é {nome} e eu tenho {idade} anos.")
print(nome, idade, end=".\n")  # O parâmetro end define o que será impresso no final da linha, por padrão é uma quebra de linha (\n)
print(nome, idade, sep=" - ")  # O parâmetro sep define o que será impresso entre os valores, por padrão é um espaço em branco