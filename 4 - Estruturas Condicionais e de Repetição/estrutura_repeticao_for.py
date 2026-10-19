texto = input("Informe um texto:")
VOGAIS = "AEIOU"

#iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() #adiciona uma quebra de linha
    print("Executa no final do laço")

#built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")
