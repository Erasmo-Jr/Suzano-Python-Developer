MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade =  int(input("Digite sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade")
if idade < MAIOR_IDADE:
    print("Menor de idade")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode tirar a CNH. Porém só pode dirigir com 18 anos.")
else:
    print("Menor de idade, não pode tirar a CNH.")